from selenium import webdriver
import pyautogui
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
import time,sys,os
import random, string


##print(sys.argv)
##if len(sys.argv)>1:
##    lang=''.join(sys.argv[1])
browser=webdriver.Chrome()
browser.get('https://attract.talent.dynamics.com/dashboard')
delay = 300
firstdelay=600

#/html/body/div[2]/app-root/div/div[2]/div/app-welcome/ms-nav-pane/mat-drawer-container/mat-drawer-content/ng-component/main/article/activity-tracker/section/div/ms-calendar/div
try:
    Elem=WebDriverWait(browser, firstdelay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="talent-header"]/header/div/div[6]/div[1]/div/div[1]/button')))
    print('Setting button is ready')
except TimeoutException:
    print('Try again')
        
def langswitching(browser,i,lang):
    #i is the language dropdown index //*[@id="talent-header"]/header/div/div[6]/div[1]/div/div[1]/button
    settingbutton=browser.find_element_by_xpath('//*[@id="talent-header"]/header/div/div[6]/div[1]/div/div[1]/button')
    settingbutton.click()
    time.sleep(2)
    settingmenu=browser.find_element_by_xpath('//*[@id="talent-header"]/header/div/div[6]/div[1]/div/div[2]/ul/li[1]/button')
    settingmenu.click()
    time.sleep(2)

    pyautogui.click(149,335)

    #language menu /html/body/div[2]/app-root/div/div[2]/div/ng-component/ms-settings/main/div/nav/div/ul/li[2]/button
    #               /html/body/app-root/div/div[2]/div/ng-component/ms-settings/main/div/nav/div/ul/li[2]/button
##    try:
##        langbutton=WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/app-root/div/div[2]/div/ng-component/ms-settings/main/div/nav/div/ul/li[2]/button')))
##        print('Setting page is ready')
##    except TimeoutException:
##        print('Setting page Try again')
##    langbutton=browser.find_element_by_xpath('/html/body/app-root/div/div[2]/div/ng-component/ms-settings/main/div/nav/div/ul/li[2]/button').click()
    browser.refresh()
    time.sleep(3)
    print('==================Start taking screenshots for '+str(i)+' '+lang+'==================')
    pyautogui.click(149,335)
    try:
        langbutton=WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="settings-viewport"]/app-language-settings/div/div/button')))
        print('Apply button is ready')
    except TimeoutException:
        print('Setting page Try again')
    langbutton=browser.find_element_by_xpath('/html/body/app-root/div/div[2]/div/ng-component/ms-settings/main/div/nav/div/ul/li[2]/button').click()
    
    langs=Select(browser.find_element_by_xpath('//*[@id="ms-select-0"]'))
    langs.select_by_index(i)
    #//*[@id="settings-viewport"]/app-language-settings/div/div/button
    Applybutton=browser.find_element_by_xpath('//*[@id="settings-viewport"]/app-language-settings/div/div/button')
    Applybutton.click()


    langfolder='Attract\\{0}'.format(lang)
    if not os.path.exists(langfolder):
        os.makedirs(langfolder)

    #connect menu pyautogui.click(156,303)
    pyautogui.click(156,303)
    try:
        Elem=WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="settings-viewport"]/app-connection-settings/div/div[1]/div[3]/button')))
        print('Connect button is ready')
    except TimeoutException:
        print('connect button Try again')
    time.sleep(5)
    pyautogui.screenshot('Attract\\{0}\\{1}.png'.format(lang,'0_Connect'))
    time.sleep(2)
    # langauge menu pyautogui.click(149,335)
    pyautogui.click(149,335)
    try:
        Elem=WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="settings-viewport"]/app-language-settings/div/div/button')))
        print('Apply button is ready')
    except TimeoutException:
        print('Apply button Try again')
    time.sleep(5)
    pyautogui.screenshot('Attract\\{0}\\{1}.png'.format(lang,'1_language'))
    #close button /html/body/app-root/div/div[2]/div/ng-component/ms-settings/main/header/button
    try:
        Elem=WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/div/div[2]/div/ng-component/ms-settings/main/header/button')))
        print('Close button is ready')
    except TimeoutException:
        print('Close page Try again')

    Closesettingbutton=browser.find_element_by_xpath('/html/body/app-root/div/div[2]/div/ng-component/ms-settings/main/header/button')
    Closesettingbutton.click()

def attractss(browser,lang):
    
    #li=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    delay = 300
    firstdelay=600
    try:
        Elem=WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="talent-header"]/header/div/div[6]/div[1]/div/div[1]/button')))
        print('Home Page is ready')
    except TimeoutException:
        print('home page Try again')
       
    i=2
    ##    print('new guide button Try again')
    pyautogui.screenshot('Attract\\{0}\\{1}.png'.format(lang,i))
    i=i+1

    settingbutton=browser.find_element_by_xpath('//*[@id="talent-header"]/header/div/div[6]/div[1]/div/div[1]/button').click()
    time.sleep(1)
    pyautogui.screenshot('Attract\\{0}\\{1}.png'.format(lang,i))
    i=i+1
    
    aboutbutton=browser.find_element_by_xpath('//*[@id="talent-header"]/header/div/div[6]/div[2]/div/div[1]/button').click()
    time.sleep(1)
    pyautogui.screenshot('Attract\\{0}\\{1}.png'.format(lang,i))
    i=i+1

    pyautogui.click(90,500)
    time.sleep(2)

    jobmenu=browser.find_element_by_xpath('//*[@id="nav-pane-1"]/nav/ms-nav-pane-content/ms-nav-pane-select-option[2]').click()
    time.sleep(3)
    pyautogui.screenshot('Attract\\{0}\\{1}.png'.format(lang,i))
    i=i+1

    #click new job button==================
    newjobbutton=browser.find_element_by_xpath('//*[@id="newJobButton"]').click()

    try:
        Elem=WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="job-title"]')))
        print('Home Page is ready')
    except TimeoutException:
        print('home page Try again')
    time.sleep(2)
    pyautogui.screenshot('Attract\\{0}\\{1}.png'.format(lang,i))
    i=i+1

    importfexcelbutton=browser.find_element_by_xpath('//*[@id="mat-dialog-0"]/add-job-opening-dialog/ms-dialog-content/div/div/ms-pivot/div/button[2]').click()
    time.sleep(3)
    pyautogui.screenshot('Attract\\{0}\\{1}.png'.format(lang,i))
    i=i+1

    onepersonbutton=browser.find_element_by_xpath('//*[@id="mat-dialog-0"]/add-job-opening-dialog/ms-dialog-content/div/div/ms-pivot/div/button[1]').click()
    titleinput=browser.find_element_by_xpath('//*[@id="job-title"]').click()
    pyautogui.typewrite("Tester")
    time.sleep(1)
    #select my role hiring manager?
    pyautogui.click(900,667)
    time.sleep(1)
    pyautogui.click(900,699)
    pyautogui.click(947,726) # add button

    try:
        Elem=WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mat-dialog-1"]/ng-component/ms-dialog-actions/div/button[1]')))
        print('Choose template Page is ready')
    except TimeoutException:
        print('Choose template page Try again')
    time.sleep(2)
    pyautogui.screenshot('Attract\\{0}\\{1}.png'.format(lang,i))
    i=i+1

    pyautogui.click(931,600) #click default template
    #click complet button to create the draft job
    completecreatebutton=browser.find_element_by_xpath('//*[@id="mat-dialog-1"]/ng-component/ms-dialog-actions/div/button[1]').click()
    time.sleep(2)
    pyautogui.screenshot('Attract\\{0}\\{1}_newjob.png'.format(lang,i))
    i=i+1
    #end of creating new job ================

    # editing a draft job ====================
    browser.back()# go back to job page
    time.sleep(2)
    browser.refresh() 
    time.sleep(3)
    try:
        Elem=WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="job-filter-3"]')))
        print('Choose template Page is ready')
    except TimeoutException:
        print('Choose template page Try again')

    filterbutton=browser.find_element_by_xpath('//*[@id="job-filter-3"]').click()
    time.sleep(2)
    pyautogui.screenshot('Attract\\{0}\\{1}.png'.format(lang,i))
    i=i+1
    
    pyautogui.click(1773,270) #click draft in the menu

    #click on the first draft job
    pyautogui.click(700,370)  #details page
    time.sleep(4)
    pyautogui.screenshot('Attract\\{0}\\{1}.png'.format(lang,i))
    i=i+1

    pyautogui.click(1704,196) #try delete the job
    time.sleep(4)
    pyautogui.screenshot('Attract\\{0}\\{1}.png'.format(lang,i))
    i=i+1
    pyautogui.click(1072,631) #cancel delete the job

    pyautogui.click(417,330) # hiring team page
    time.sleep(5)
    pyautogui.click(414,334) # hiring team page
    time.sleep(5)

    pyautogui.screenshot('Attract\\{0}\\{1}.png'.format(lang,i))
    i=i+1
    time.sleep(5)

    try:
        Elem=WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/div/div[2]/div/app-welcome/ms-nav-pane/mat-drawer-container/mat-drawer-content/job-hub/job-hub-header/main/article/div/content-container/hiring-team/div[2]/table/tbody/tr/td[3]/button')))
        print('Deletebutton is ready')
    except TimeoutException:
        print('Deletebutton Try again')

    #delete contact
    browser.find_element_by_xpath('/html/body/app-root/div/div[2]/div/app-welcome/ms-nav-pane/mat-drawer-container/mat-drawer-content/job-hub/job-hub-header/main/article/div/content-container/hiring-team/div[2]/table/tbody/tr/td[3]/button').click()
    time.sleep(2)
    pyautogui.screenshot('Attract\\{0}\\{1}.png'.format(lang,i))
    i=i+1

    #cancel delete
    browser.refresh()
    time.sleep(5)
    
    pyautogui.click(504,321) # process  page
    time.sleep(2)
    try:
        Elem=WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/div/div[2]/div/app-welcome/ms-nav-pane/mat-drawer-container/mat-drawer-content/job-hub/job-hub-header/header/div/ms-pivot/div/button[3]')))
        print('Deletebutton is ready')
    except TimeoutException:
        print('Deletebutton Try again')
    browser.find_element_by_xpath('/html/body/app-root/div/div[2]/div/app-welcome/ms-nav-pane/mat-drawer-container/mat-drawer-content/job-hub/job-hub-header/header/div/ms-pivot/div/button[3]').click()
    pyautogui.screenshot('Attract\\{0}\\{1}.png'.format(lang,i))
    i=i+1

    talentpoolpage=browser.find_element_by_xpath('//*[@id="nav-pane-0"]/nav/ms-nav-pane-content/ms-nav-pane-select-option[3]').click()
    time.sleep(2)
    pyautogui.screenshot('Attract\\{0}\\{1}.png'.format(lang,i))
    i=i+1

    #click ... button of the pool
    browser.find_element_by_xpath('/html/body/app-root/div/div[2]/div/app-welcome/ms-nav-pane/mat-drawer-container/mat-drawer-content/ng-component/talent-pool-cards/main/article/content-container/mat-card/mat-card-actions/span/button').click()
    time.sleep(2)
    pyautogui.screenshot('Attract\\{0}\\{1}.png'.format(lang,i))
    i=i+1

    pyautogui.click(1152,853);time.sleep(2) #cancel edit
    #try search in talent pool
    #browser.find_element_by_xpath('//*[@id="ms-chips-auto-3"]').click()
    pyautogui.click(427,249);time.sleep(2);pyautogui.press('m');time.sleep(5)

    pyautogui.screenshot('Attract\\{0}\\{1}.png'.format(lang,i))
    i=i+1

    pyautogui.click(1455,875)
    #go back to job menu
    jobmenu=browser.find_element_by_xpath('//*[@id="nav-pane-0"]/nav/ms-nav-pane-content/ms-nav-pane-select-option[2]').click()
    time.sleep(3)
    pyautogui.screenshot('Attract\\{0}\\{1}.png'.format(lang,i))
    i=i+1

    pyautogui.click(731,372) #click an active job to add candidate
    time.sleep(2)

    addnewcandidate=browser.find_element_by_xpath('//*[@id="newCandidateTooltip"]').click()
    time.sleep(2)
    pyautogui.screenshot('Attract\\{0}\\{1}.png'.format(lang,i))
    i=i+1

    #click import from excel button
    browser.find_element_by_xpath('//*[@id="mat-dialog-0"]/add-candidate-dialog/ms-dialog-content/div/div/ms-pivot/div/button[2]').click()
    time.sleep(2)
    pyautogui.screenshot('Attract\\{0}\\{1}.png'.format(lang,i))
    i=i+1

    browser.find_element_by_xpath('//*[@id="mat-dialog-0"]/add-candidate-dialog/ms-dialog-content/div/div/ms-pivot/div/button[1]').click()
    time.sleep(2)
    pyautogui.screenshot('Attract\\{0}\\{1}.png'.format(lang,i))
    i=i+1

    pyautogui.click(888,478) #click the internal candidate input
    pyautogui.press('m')
    time.sleep(5)
    pyautogui.screenshot('Attract\\{0}\\{1}.png'.format(lang,i))
    i=i+1
    pyautogui.click(1048,383);time.sleep(2)
    #emailinput=browser.find_element_by_xpath('//*[@id="email-12"]').click()
    pyautogui.click(900,541);time.sleep(2)

    pyautogui.typewrite('suli2921@hotmail.com')
    #givennameinput=browser.find_element_by_xpath('//*[@id="givenName-12"]').click()
    pyautogui.click(851,600);time.sleep(2)
    pyautogui.typewrite('Jack')
    #firstnameinput=browser.find_element_by_xpath('//*[@id="surname-12"]').click()
    pyautogui.click(823,668);time.sleep(2)
    surname=''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
    pyautogui.typewrite(surname)
    #click add button
    Addbutton=browser.find_element_by_xpath('//*[@id="mat-dialog-0"]/add-candidate-dialog/ms-dialog-actions/div/button[1]').click()

    try:
        Elem=WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/div/div[2]/div/app-welcome/ms-nav-pane/mat-drawer-container/mat-drawer-content/job-hub/candidate-application/main/article/content-container/div/div[4]/div/button[2]')))
        print('Choose template Page is ready')
    except TimeoutException:
        print('Choose template page Try again')
    time.sleep(2)
    pyautogui.screenshot('Attract\\{0}\\{1}.png'.format(lang,i))
    i=i+1

    #click stagedorpdownbutton
    stagedorpdownbutton=browser.find_element_by_xpath('/html/body/app-root/div/div[2]/div/app-welcome/ms-nav-pane/mat-drawer-container/mat-drawer-content/job-hub/candidate-application/main/article/content-container/div/div[4]/div/button[2]').click()
    time.sleep(2)
    pyautogui.screenshot('Attract\\{0}\\{1}.png'.format(lang,i))
    i=i+1
    pyautogui.click(823,668);time.sleep(2) #cancel

    #click advancestage button
    advancestagebutton=browser.find_element_by_xpath('/html/body/app-root/div/div[2]/div/app-welcome/ms-nav-pane/mat-drawer-container/mat-drawer-content/job-hub/candidate-application/main/article/content-container/div/div[4]/div/button[1]').click()
    time.sleep(2)
    pyautogui.screenshot('Attract\\{0}\\{1}.png'.format(lang,i))
    i=i+1

    #createschedulebutton=browser.find_element_by_xpath('//*[@id="activity-container-5"]/application-participant-activity[1]/schedule-summary/interview-schedule-summary/mat-card/mat-card-actions/div/button[1]').click()
    pyautogui.click(476,959)
    time.sleep(5)
    pyautogui.screenshot('Attract\\{0}\\{1}.png'.format(lang,i))
    i=i+1

    #add interview button
    #addinterviewbutton=browser.find_element_by_xpath('//*[@id="mat-dialog-0"]/interview-template/ms-dialog-actions/div/button[1]').click()
    pyautogui.click(1138,796)
    time.sleep(3)
    pyautogui.screenshot('Attract\\{0}\\{1}.png'.format(lang,i))
    i=i+1    

    #take a sc of the schedule main page
    time.sleep(5)
    pyautogui.screenshot('Attract\\{0}\\{1}.png'.format(lang,i))
    i=i+1 

    #/html/body/app-root/div/div[2]/div/application-activity-runtime/application-participant-activity/interview-schedule-runtime/main/application-interview-schedule-v3/ms-scheduler/div/div/scheduler-day-calendar/div/div/div[1]/div[2]/table/thead/tr/td[4]/div/div[1]
    pyautogui.click(784,311) #add interview button
    time.sleep(5)
    pyautogui.screenshot('Attract\\{0}\\{1}.png'.format(lang,i))
    i=i+1
    pyautogui.click(1507,825) #click random place to cancel

    pyautogui.click(1317,192) #click suggestion button
    time.sleep(3)
    pyautogui.screenshot('Attract\\{0}\\{1}.png'.format(lang,i))
    i=i+1

    pyautogui.click(1507,825) #click random place to cancel

    pyautogui.click(1901,245) #click the time zone dropdown
    time.sleep(3)
    pyautogui.screenshot('Attract\\{0}\\{1}.png'.format(lang,i))
    i=i+1

    pyautogui.click(1659,188) #click sent to interviewer button
    time.sleep(5)
    pyautogui.screenshot('Attract\\{0}\\{1}.png'.format(lang,i))
    i=i+1

    #wait for the email content
    try:
        Elem=WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/div/div[2]/div/application-activity-runtime/application-participant-activity/final-schedule-runtime/main/section[2]/section[2]/email-content/form/div/label')))
        print('Email template Page is ready')
    except TimeoutException:
        print('Email template page Try again')
    time.sleep(2)
    pyautogui.screenshot('Attract\\{0}\\{1}.png'.format(lang,i))
    i=i+1

    #click preview button
    pyautogui.click(1577,188) #click sent to interviewer button
    time.sleep(5)
    pyautogui.screenshot('Attract\\{0}\\{1}.png'.format(lang,i))
    i=i+1

    pyautogui.click(1507,825) #click random place to cancel

    pyautogui.click(1870,188) #click close button
    time.sleep(5)
    try:
        Elem=WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/div/div[2]/div/app-welcome/ms-nav-pane/mat-drawer-container/mat-drawer-content/job-hub/candidate-application/main/article/content-container/div/div[4]/div/button[1]')))
        print('advancestagebutton is ready')
    except TimeoutException:
        print('advancestagebutton Try again')
    time.sleep(2)

    browser.refresh()
    try:
        Elem=WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/div/div[2]/div/app-welcome/ms-nav-pane/mat-drawer-container/mat-drawer-content/job-hub/candidate-application/main/article/content-container/div/div[4]/div/button[1]')))
        print('advancestagebutton is ready')
    except TimeoutException:
        print('advancestagebutton Try again')
    time.sleep(2)   
    #click advance stage button to intervew stage
    #advancestagebutton=browser.find_element_by_xpath('/html/body/app-root/div/div[2]/div/app-welcome/ms-nav-pane/mat-drawer-container/mat-drawer-content/job-hub/candidate-application/main/article/content-container/div/div[4]/div/button[1]').click()
    pyautogui.click(1825,400)
    time.sleep(5)
    pyautogui.screenshot('Attract\\{0}\\{1}.png'.format(lang,i))
    i=i+1

    #click feedback button
    pyautogui.click(1912,1003)
    time.sleep(2)
    #feedbackbuttons=browser.find_elements_by_xpath("//*[contains(text(), 'Provide feedback')]")
    pyautogui.click(1430,852) #click feedback button
    time.sleep(5)
    pyautogui.screenshot('Attract\\{0}\\{1}.png'.format(lang,i))
    i=i+1

    browser.back()
    time.sleep(5)

        #click advance stage button to offer stage
    #advancestagebutton=browser.find_element_by_xpath('/html/body/app-root/div/div[2]/div/app-welcome/ms-nav-pane/mat-drawer-container/mat-drawer-content/job-hub/candidate-application/main/article/content-container/div/div[4]/div/button[1]').click()
    pyautogui.click(1825,400)
    time.sleep(2)
    pyautogui.screenshot('Attract\\{0}\\{1}.png'.format(lang,i))
    i=i+1

    #profilepage
    profilepage=browser.find_element_by_xpath('/html/body/app-root/div/div[2]/div/app-welcome/ms-nav-pane/mat-drawer-container/mat-drawer-content/job-hub/candidate-application/header/div/ms-pivot/div/button[2]').click()
    time.sleep(2)
    pyautogui.screenshot('Attract\\{0}\\{1}.png'.format(lang,i))
    i=i+1

    #notes page
    notepage=browser.find_element_by_xpath('/html/body/app-root/div/div[2]/div/app-welcome/ms-nav-pane/mat-drawer-container/mat-drawer-content/job-hub/candidate-application/header/div/ms-pivot/div/button[3]').click()
    time.sleep(2)
    pyautogui.screenshot('Attract\\{0}\\{1}.png'.format(lang,i))
    i=i+1

    #documents page
    docpage=browser.find_element_by_xpath('/html/body/app-root/div/div[2]/div/app-welcome/ms-nav-pane/mat-drawer-container/mat-drawer-content/job-hub/candidate-application/header/div/ms-pivot/div/button[4]').click()
    time.sleep(2)
    pyautogui.screenshot('Attract\\{0}\\{1}.png'.format(lang,i))
    i=i+1

    #add a document
    adddocbutton=browser.find_element_by_xpath('/html/body/app-root/div/div[2]/div/app-welcome/ms-nav-pane/mat-drawer-container/mat-drawer-content/job-hub/candidate-application/main/article/content-container/application-documents/section[2]/div/div/button').click()
    time.sleep(2)
    pyautogui.screenshot('Attract\\{0}\\{1}.png'.format(lang,i))
    i=i+1

    #pyautogui.click(990,563) #click to add a doc

    pyautogui.click(1667,870)#cancel

    addtalentpoolbutton=browser.find_element_by_xpath('/html/body/app-root/div/div[2]/div/app-welcome/ms-nav-pane/mat-drawer-container/mat-drawer-content/job-hub/candidate-application/header/applicant-banner/div/div[2]/button').click()
    time.sleep(2)
    pyautogui.screenshot('Attract\\{0}\\{1}.png'.format(lang,i))
    i=i+1

    pyautogui.click(1685,687)#cancel
          
##    #offerbutton=browser.find_element_by_xpath('//*[@id="activity-container-8"]/application-participant-activity/offer-summary/section/div[2]/section/button').click()
##    #time.sleep(10)
##   # pyautogui.click(369,21) #click offer tab
##    #time.sleep(2)
##    #pyautogui.screenshot('Attract\\{0}\\{1}.png'.format(lang,i))
##    #i=i+1

#langs=['en-US', 'en-CA']
#langs=['eu-ES', 'bg', 'ca-ES', 'zh-Hans-CN', 'zh-Hant-HK', 'zh-Hant-TW', 'hr', 'cs', 'da', 'nl-BE', 'nl', 'en-US', 'en-CA', 'en-GB', 'en-AU', 'en-IE', 'en-IN', 'en-MY', 'en-NZ', 'en-SG', 'en-ZA', 'et', 'fi', 'fr-BE', 'fr-CA', 'fr', 'fr-CH', 'de', 'de-AT', 'de-CH', 'gl-ES', 'el', 'hi', 'hu', 'it', 'it-CH', 'id', 'is', 'ja', 'kk', 'ko', 'lt', 'lv', 'ms', 'nb', 'pl', 'pt-BR', 'pt', 'ro', 'ru', 'sr-Cyrl-RS', 'sr-Latn-RS', 'sk', 'sl', 'es', 'es-MX', 'sv', 'th', 'tr', 'uk', 'vi']
langs=['gl-ES', 'el', 'hi', 'hu', 'it', 'it-CH', 'id', 'is', 'ja', 'kk', 'ko', 'lt', 'lv', 'ms', 'nb', 'pl', 'pt-BR', 'pt', 'ro', 'ru', 'sr-Cyrl-RS', 'sr-Latn-RS', 'sk', 'sl', 'es', 'es-MX', 'sv', 'th', 'tr', 'uk', 'vi']

i=30
for l in langs:
    langswitching(browser,i,l)
    attractss(browser,l)
    i=i+1
browser.quit()
