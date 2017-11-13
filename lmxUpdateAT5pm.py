#https://www.udemy.com/the-python-mega-course/learn/v4/t/lecture/4775192?start=0
#http://strftime.org/
#http://stackoverflow.com/questions/3043849/use-regular-expression-with-fileinput
import re
import datetime
import fileinput

#format the month and day of the current date
now=datetime.datetime.now()
utc=now+datetime.timedelta(hours=7)
utc=utc.strftime("%b.%d")
if utc[4]=="0":
    utc=utc[:3]+"."+utc[5:]
    print(utc)
else:
    print(utc)

###############################
#update mobile-App UI
for line in fileinput.input("C:\\Depots\\MBSI\\Projects\\D365App\\UI\\UI.lmx", inplace=True):
    line=re.sub(r"^.*?_Monthly.*?\n", "Custom 3	Equals	D365App_Monthly."+utc,line)
    print(line.strip('\n'))
    
#update lmx for CDM
for line in fileinput.input(r'C:\Depots\MBSI\Projects\CDM\UI\UI.lmx', inplace=True):
    line=re.sub(r"^.*?_Weekly.*?\n", "Custom 3	Equals	CDM_Weekly."+utc,line)
    print(line.strip('\n'))

#update lmx for officeApp
for line in fileinput.input("C:\\Depots\\MBSI\\Projects\\AX\\7.x_OfficeApps\\UI\\UI.lmx", inplace=True):
    line=re.sub(r"^.*?_Weekly.*?\n", "Custom 3	Equals	OfficeApp_Weekly."+utc,line)
    print(line.strip('\n'))

#update lmx for shellUI
for line in fileinput.input("C:\\Depots\\MBSI\\Projects\\D365Shell\\UI\\UI.lmx", inplace=True):
    line=re.sub(r"^.*?_Weekly.*?\n", "Custom 3	Equals	D365Shell_Weekly."+utc,line)
    print(line.strip('\n'))

#update lmx for D365HCMApp UI
for line in fileinput.input("C:\\Depots\\MBSI\\Projects\\OOB\\UI\\OOBAppsUI.lmx", inplace=True):
    line=re.sub(r"^.*?_Weekly.*?\n", "Custom 3	Equals	D365HCMApp_Weekly."+utc,line)
    print(line.strip('\n'))

###update lmx for D365HCMApp UA
##for line in fileinput.input("C:\\Depots\\MBSI\\Projects\\OOB\\UA\\Field_Descriptions\\OOBAppsUA.lmx", inplace=True):
##    line=re.sub(r"^.*?_Weekly.*?\n", "Custom 3	Equals	D365HCMApp_FD_Weekly."+utc,line)
##    print(line.strip('\n'))

 


