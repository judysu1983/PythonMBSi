from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

browser = webdriver.Firefox()
browser.get('https://msdyneng.visualstudio.com/PowerApps%20Runtime/_git/PowerApps-Runtime-Metadata')
# wait until sign in and the page loaded
browser.implicitly_wait(10)

browser.find_element_by_partial_link_text('Pull Requests').click()
browser.find_element_by_partial_link_text('Create a pull request').click()
browser.find_element_by_css_selector('div.vc-branches-container:nth-child(3)').click()

#select from dropdown merge into Master branch
browser.find_element_by_css_selector('li.filtered-list-item:nth-child(2)').click()

#add reviewers
e=browser.find_element_by_id('reviewers-edit')
e.send_keys('Eun Ji Cho; Ilhyuk Kim; Ping Yin; Judy Su;')

#add work items
e= browser.find_element_by_css_selector('.vc-pullrequest-view-details-relatedartifacts-addartifactbox')
e.send_keys('11667')
e.click()
e.send_keys(Keys.RETURN)


#click Create button

#click pull-request-vote-button
browser.find_element_by_id('pull-request-vote-button').click()

#click pull-request-complete-button
browser.find_element_by_id('pull-request-complete-button').click()

#click complete merge button
browser.find_element_by_css_selector('span.ms-Dialog-action:nth-child(1) > button:nth-child(1)').click()
