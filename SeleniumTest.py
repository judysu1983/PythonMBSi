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
browser.get('https://onboard.talent.int.dynamics.com')
delay = 300
firstdelay=600
#waiting for home page
try:
    Elem=WebDriverWait(browser, firstdelay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="onboarding-hire-cards"]/div/button')))
    print('Page is ready')
except TimeoutException:
    print('Try again')
        
def langswitching(browser,i,lang):
    #i is the language dropdown index
    settingbutton=browser.find_element_by_xpath('//*[@id="onboarding-header"]/header/div/div[5]/div[1]/div/div[1]/button')
    settingbutton.click()
    time.sleep(2)
    settingmenu=browser.find_element_by_xpath('//*[@id="onboarding-header"]/header/div/div[5]/div[1]/div/div[2]/ul/li[1]/button')
    settingmenu.click()

    #waiting for apply button to appear
    try:
        Applybutton=WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/app-root/div/div[2]/ng-component/div/section/button')))
        print('Setting page is ready')
    except TimeoutException:
        print('Setting page Try again')

    browser.refresh()
    time.sleep(5)
    #select the 5th langauge in the dropdown and click apply 
    langs=Select(browser.find_element_by_xpath('//*[@id="ms-select-0"]'))
    langs.select_by_index(i)
    Applybutton=browser.find_element_by_xpath('/html/body/div[2]/app-root/div/div[2]/ng-component/div/section/button')
    Applybutton.click()
    time.sleep(5)
    #wait for language switching and page reloading
    langfolder='Onboarding\\{0}'.format(lang)
    if not os.path.exists(langfolder):
        os.makedirs(langfolder)
	
    
    try:
        Elem=WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/app-root/div/div[2]/ng-component/button/span')))
        print('Language Page is ready')
    except TimeoutException:
        print('language page Try again')
    pyautogui.screenshot('Onboarding\\{0}\\{1}.png'.format(lang,'0'))
    Closesettingbutton=browser.find_element_by_xpath('/html/body/div[2]/app-root/div/div[2]/ng-component/button/span')
    Closesettingbutton.click()
    
def onboardingss(browser,lang):
    
    li=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    delay = 300
    firstdelay=600

    #wait for home page to load again
    try:
        Elem=WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="onboarding-hire-cards"]/div/button')))
        print('Home Page is ready')
    except TimeoutException:
        print('home page Try again')
       

    ##    print('new guide button Try again')
    pyautogui.screenshot('Onboarding\\{0}\\{1}.png'.format(lang,li[0]))

##    # page should be fully loaded
##
##    try:
##        Elem=WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="onboarding-header"]/header/div/div[5]/div[1]/div/div[1]/button')))
##        print('Waiting for setting button')
##    except TimeoutException:
##        print('setting button Try again')
##
##                                                                                 
    # press setting and take a screenshot
    settingbutton=browser.find_element_by_xpath('//*[@id="onboarding-header"]/header/div/div[5]/div[1]/div/div[1]/button')
    settingbutton.click()                                                                      
    pyautogui.screenshot('Onboarding\\{0}\\{1}.png'.format(lang,li[1]))
    time.sleep(2)

    aboutbutton=browser.find_element_by_xpath('//*[@id="onboarding-header"]/header/div/div[5]/div[2]/div/div[1]/button')                                                                             
    aboutbutton.click()
    time.sleep(1)
    pyautogui.screenshot('Onboarding\\{0}\\{1}.png'.format(lang,li[2]))

    creatorbutton=browser.find_element_by_xpath('/html/body/div[2]/app-root/div/div[2]/ng-component/ms-nav-pane/mat-drawer-container/mat-drawer-content/div/div[1]/div[2]/button[1]')
    creatorbutton.click()
    time.sleep(1)
    pyautogui.screenshot('Onboarding\\{0}\\{1}.1.png'.format(lang,li[2]))
    pyautogui.click(48,661)

    activebutton=browser.find_element_by_xpath('/html/body/div[2]/app-root/div/div[2]/ng-component/ms-nav-pane/mat-drawer-container/mat-drawer-content/div/div[1]/div[2]/button[2]').click()
    time.sleep(1)
    pyautogui.screenshot('Onboarding\\{0}\\{1}.2.png'.format(lang,li[2]))
    pyautogui.click(48,661)
    
    sortbutton=browser.find_element_by_xpath('/html/body/div[2]/app-root/div/div[2]/ng-component/ms-nav-pane/mat-drawer-container/mat-drawer-content/div/div[1]/div[2]/button[3]').click()
    time.sleep(1)
    pyautogui.screenshot('Onboarding\\{0}\\{1}.3.png'.format(lang,li[2]))
    pyautogui.click(48,661)
    
    Newguidebutton=browser.find_element_by_xpath('//*[@id="onboarding-hire-cards"]/div/button')
    Newguidebutton.click()
    time.sleep(5)
    pyautogui.screenshot('Onboarding\\{0}\\{1}.png'.format(lang,li[3]))


    #add now link
    Addpeoplolink=browser.find_element_by_xpath('//*[@id="web-form"]/div/ms-people-picker/button/span/a').click()
    time.sleep(2)
    pyautogui.screenshot('Onboarding\\{0}\\{1}.png'.format(lang,li[4]))


    #cancel add now window
    pyautogui.click(1086,848)

    #reopen add guide form
    Addbutton=browser.find_element_by_xpath('//*[@id="onboarding-hire-cards"]/div/button').click()
    time.sleep(1)

    #add more link
    Addmorelink=browser.find_element_by_xpath('//*[@id="web-form"]/div/div/a').click()
    time.sleep(2)
    pyautogui.screenshot('Onboarding\\{0}\\{1}.png'.format(lang,li[5]))

    #cancel add now window
    pyautogui.click(1100,779)
    time.sleep(1)

    try:
        Elem=WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="onboarding-hire-cards"]/div/button')))
        print('Home Page is ready')
    except TimeoutException:
        print('home page Try again')

    #reopen add guide form
    Addbutton=browser.find_element_by_xpath('//*[@id="onboarding-hire-cards"]/div/button').click()
    time.sleep(1)


    ##onboardingwhoInput=browser.find_element_by_xpath('//*[@id="web-form"]/ms-date-picker/div[1]/mat-form-field/div/div[1]/div/div/button').click()
    ##onboardingwhoInput.send_keys('Judy Su (Pactera Technologies Inc)')
    ##onboardingwhoInput.send_keys('Enter')
    pyautogui.click(859,479);pyautogui.typewrite("v-judysu@microsoft.co");pyautogui.press('m');time.sleep(5);pyautogui.click(1044,510);time.sleep(5)
    pyautogui.click(859,479);time.sleep(2)
    pyautogui.click(936,600);time.sleep(5);pyautogui.click(948,695)
    #date selector
    #onboardingdate=browser.find_element_by_xpath('//*[@id="web-form"]/ms-date-picker/div[1]/mat-form-field/div/div[1]/div/div/button').click()
    #pyautogui.typewrite('2018/11/22');time.sleep(2);pyautogui.click(1128,525)
    #pyautogui.click(936,600);time.sleep(2);pyautogui.click(948,695)
    #pyautogui.screenshot('Onboarding\\zh-cn\\%s.png' % 5)
    time.sleep(5)

    #click next page button
    pyautogui.click(931,744)
    time.sleep(2)
    pyautogui.screenshot('Onboarding\\{0}\\{1}.png'.format(lang,li[6]))


    #click next next page button on email template page
    pyautogui.click(1150,812)
    pyautogui.screenshot('Onboarding\\{0}\\{1}.1.png'.format(lang,li[6]))

    #cancel button
    pyautogui.click(1280,819);time.sleep(2)




    #######################go through the second menu Template###################
    #click template menu //*[@id="nav-pane-7"]/nav/ms-nav-pane-content/ms-nav-pane-select-option[2]/div[1]/div
    #templatemenu=onboardingdate=browser.find_element_by_xpath('//*[@id="nav-pane-20"]/nav/ms-nav-pane-content/ms-nav-pane-select-option[2]/div[1]/div').click()
    pyautogui.click(100,250)
    time.sleep(2)
    pyautogui.screenshot('Onboarding\\{0}\\{1}.png'.format(lang,li[7]))


    try:
        Elem=WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/app-root/div/div[2]/ng-component/ms-nav-pane/mat-drawer-container/mat-drawer-content/div/div[2]/div[2]/div/button')))
        print('New tempalte button ready')
    except TimeoutException:
        print('new template button Try again')
    time.sleep(1)
    pyautogui.screenshot('Onboarding\\{0}\\{1}.png'.format(lang,li[8]))

    #click new template button
    newtemplatebutton=browser.find_element_by_xpath('/html/body/div[2]/app-root/div/div[2]/ng-component/ms-nav-pane/mat-drawer-container/mat-drawer-content/div/div[2]/div[2]/div/button').click()


    time.sleep(2)
    pyautogui.screenshot('Onboarding\\{0}\\{1}.png'.format(lang,li[9]))

    #close create new template form
    pyautogui.click(1067,655)
    time.sleep(1)

    #... button of the template                /html/body/div[2]/app-root/div/div[2]/ng-component/ms-nav-pane/mat-drawer-container/mat-drawer-content/div/div[2]/div[2]/div/onboarding-template-card[1]/div/button
    morebutton=browser.find_element_by_xpath('/html/body/div[2]/app-root/div/div[2]/ng-component/ms-nav-pane/mat-drawer-container/mat-drawer-content/div/div[2]/div[2]/div/onboarding-template-card[1]/div/button').click()
    time.sleep(3)
    pyautogui.screenshot('Onboarding\\{0}\\{1}.png'.format(lang,li[10]))

    # share menu under ... button
    #moresharemenu=browser.find_element_by_xpath('//*[@id="cdk-overlay-12"]/div/div/button[4]').click()
    pyautogui.click(1240,784)

    #waiting sharing form to load //*[@id="mat-dialog-4"]/ng-component/div/ms-dialog-content/div/div/manage-person-v2/ms-dialog-content/div/div/ms-pivot/div/button[1]
    try:
        Elem=WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mat-dialog-4"]/ng-component/div/ms-dialog-content/div/div/manage-person-v2/ms-dialog-content/div/div/ms-pivot/div/button[1]')))
        print('Sharing page ready')
    except TimeoutException:
        print('share page Try again')
    time.sleep(1)
    pyautogui.screenshot('Onboarding\\{0}\\{1}.png'.format(lang,li[11]))

    #cancel share form
    #//*[@id="mat-dialog-4"]/ng-component/div/ms-dialog-content/div/div/manage-person-v2/ms-dialog-content/div/div/ms-pivot/div/button[1]
    cancelbutton=browser.find_element_by_xpath('//*[@id="mat-dialog-4"]/ng-component/div/ms-dialog-actions/div/button[2]').click()
    time.sleep(2)

    #open to edit test template
    #/html/body/div[2]/app-root/div/div[2]/ng-component/ms-nav-pane/mat-drawer-container/mat-drawer-content/div/div[2]/div[2]/div/onboarding-template-card[1]/div/div
    newtemplatebutton=browser.find_element_by_xpath('/html/body/div[2]/app-root/div/div[2]/ng-component/ms-nav-pane/mat-drawer-container/mat-drawer-content/div/div[2]/div[2]/div/onboarding-template-card[1]/div/div').click()

    #waiting for intro menu to load /html/body/div[2]/app-root/div/div[2]/ng-component/div[1]/ms-header/div/div[2]/ms-pivot/div/button[1]
    try:
        Elem=WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/app-root/div/div[2]/ng-component/div[1]/ms-header/div/div[2]/ms-pivot/div/button[1]')))
        print('Introduction page ready')
    except TimeoutException:
        print('introduction page Try again')
    time.sleep(2)
    pyautogui.screenshot('Onboarding\\{0}\\{1}.png'.format(lang,li[12]))


    activitybutton=browser.find_element_by_xpath('/html/body/div[2]/app-root/div/div[2]/ng-component/div[1]/ms-header/div/div[2]/ms-pivot/div/button[2]').click()
    time.sleep(2)
    pyautogui.screenshot('Onboarding\\{0}\\{1}.png'.format(lang,li[13]))

    #/html/body/div[2]/app-root/div/div[2]/ng-component/div[1]/ms-header/div/div[2]/ms-pivot/div/button[3]/span
    contactbutton=browser.find_element_by_xpath('/html/body/div[2]/app-root/div/div[2]/ng-component/div[1]/ms-header/div/div[2]/ms-pivot/div/button[3]').click()
    time.sleep(2)
    pyautogui.screenshot('Onboarding\\{0}\\{1}.png'.format(lang,li[14]))

    resourcebutton=browser.find_element_by_xpath('/html/body/div[2]/app-root/div/div[2]/ng-component/div[1]/ms-header/div/div[2]/ms-pivot/div/button[4]').click()
    time.sleep(2)
    pyautogui.screenshot('Onboarding\\{0}\\{1}.png'.format(lang,li[15]))

    #new resource + button

    projectresourcebutton=browser.find_element_by_xpath('/html/body/div[2]/app-root/div/div[2]/ng-component/div[1]/div/project-resources/div/div[2]/div/button').click()
    time.sleep(2)
    pyautogui.screenshot('Onboarding\\{0}\\{1}.png'.format(lang,li[16]))

    #go back to home page!
    browser.back()

    try:
        Elem=WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/app-root/div/div[2]/ng-component/ms-nav-pane/mat-drawer-container/mat-drawer-content/div/div[2]/div[2]/div/button')))
        print('New tempalte button ready')
    except TimeoutException:
        print('new template button Try again')
    time.sleep(1)
    #//*[@id="mat-dialog-4"]/add-resources-dialog/ms-dialog-content/div/div/ms-pivot/div/button[2]/span
    #click on task menu
    #//*[@id="nav-pane-5"]/nav/ms-nav-pane-content/ms-nav-pane-select-option[3]/div[1]/div//*[@id="nav-pane-0"]/nav/ms-nav-pane-content/ms-nav-pane-select-option[3]/div[1]/div
    pyautogui.click(20,300)
    time.sleep(5)
    pyautogui.screenshot('Onboarding\\{0}\\{1}.png'.format(lang,li[17]))

    print('Finish taking screenshots for {} ============================='.format(lang))

#browser.quit()
#langs=['eu-ES', 'bg', 'ca-ES', 'zh-Hans-CN', 'zh-Hant-HK', 'zh-Hant-TW', 'hr', 'cs', 'da', 'nl-BE', 'nl', 'en-US', 'en-CA', 'en-GB', 'en-AU', 'en-IE', 'en-IN', 'en-MY', 'en-NZ', 'en-SG', 'en-ZA', 'et', 'fi', 'fr-BE', 'fr-CA', 'fr', 'fr-CH', 'de', 'de-AT', 'de-CH', 'gl-ES', 'el', 'hi', 'hu', 'it', 'it-CH', 'id', 'is', 'ja', 'kk', 'ko', 'lt', 'lv', 'ms', 'nb', 'pl', 'pt-BR', 'pt', 'ro', 'ru', 'sr-Cyrl-RS', 'sr-Latn-RS', 'sk', 'sl', 'es', 'es-MX', 'sv', 'th', 'tr', 'uk', 'vi']
langs=['en-IE', 'en-IN', 'en-MY', 'en-NZ', 'en-SG', 'en-ZA']
i=15
for l in langs:
    langswitching(browser,i,l)
    onboardingss(browser,l)
    i=i+1
browser.quit()
