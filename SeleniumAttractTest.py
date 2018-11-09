from selenium import webdriver
import pyautogui
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
import time,sys,os



##print(sys.argv)
##if len(sys.argv)>1:
##    lang=''.join(sys.argv[1])
browser=webdriver.Chrome()
browser.get('https://attract.talent.dynamics.com/dashboard')
delay = 300
firstdelay=600

try:
    Elem=WebDriverWait(browser, firstdelay).until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/div/div[2]/div/app-welcome/ms-nav-pane/mat-drawer-container/mat-drawer-content/ng-component/main/article/activity-tracker/section/div/ms-calendar')))
    print('Page is ready')
except TimeoutException:
    print('Try again')
        
def langswitching(browser,i,lang):
    #i is the language dropdown index //*[@id="talent-header"]/header/div/div[6]/div[1]/div/div[1]/button
    settingbutton=browser.find_element_by_xpath('//*[@id="talent-header"]/header/div/div[6]/div[1]/div/div[1]/button')
    settingbutton.click()
    time.sleep(2)
    settingmenu=browser.find_element_by_xpath('//*[@id="talent-header"]/header/div/div[6]/div[1]/div/div[2]/ul/li[1]/button')
    settingmenu.click()

    try:
        langbutton=WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/div/div[2]/div/ng-component/ms-settings/main/div/nav/div/ul/li[2]/button')))
        print('Setting page is ready')
    except TimeoutException:
        print('Setting page Try again')

    langbutton=browser.find_element_by_xpath('/html/body/app-root/div/div[2]/div/ng-component/ms-settings/main/div/nav/div/ul/li[2]/button').click()
    browser.refresh()
	langbutton=browser.find_element_by_xpath('/html/body/app-root/div/div[2]/div/ng-component/ms-settings/main/div/nav/div/ul/li[2]/button').click()
    
    langs=Select(browser.find_element_by_xpath('//*[@id="ms-select-0"]'))
    langs.select_by_index(i)
    #//*[@id="settings-viewport"]/app-language-settings/div/div/button
    Applybutton=browser.find_element_by_xpath('//*[@id="settings-viewport"]/app-language-settings/div/div/button')
    Applybutton.click()
    time.sleep(5)

    langfolder='Attract\\{0}'.format(lang)
    if not os.path.exists(langfolder):
        os.makedirs(langfolder)

    #link menu /html/body/div[2]/app-root/div/div[2]/div/ng-component/ms-settings/main/div/nav/div/ul/li[1]/button
    try:
        Elem=WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/app-root/div/div[2]/div/ng-component/ms-settings/main/div/nav/div/ul/li[1]/button')))
        print('Link Page is ready')
    except TimeoutException:
        print('Link page Try again')
    pyautogui.screenshot('Attract\\{0}\\{1}.png'.format(lang,'0_link'))

    
    langbutton=browser.find_element_by_xpath('/html/body/app-root/div/div[2]/div/ng-component/ms-settings/main/div/nav/div/ul/li[2]/button').click()
    pyautogui.screenshot('Attract\\{0}\\{1}.png'.format(lang,'0_language'))

    Closesettingbutton=browser.find_element_by_xpath('/html/body/div[2]/app-root/div/div[2]/ng-component/button/span')
    Closesettingbutton.click()


 langs=['zh-Hans', 'zh-HK']
i=3
for l in langs:
    langswitching(browser,i,l)
    onboardingss(browser,l)
    i=i+1
browser.quit()