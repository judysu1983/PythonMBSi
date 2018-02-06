#https://www.udemy.com/the-python-mega-course/learn/v4/t/lecture/4775192?start=0
#http://strftime.org/
#http://stackoverflow.com/questions/3043849/use-regular-expression-with-fileinput
import re
import datetime
import fileinput

#format the month and day of the current date
now=datetime.datetime.now()
utc=now+datetime.timedelta(hours=8)
utc=utc.strftime("%b.%d")
if utc[4]=="0":
    utc=utc[:3]+"."+utc[5:]
    print(utc)
else:
    print(utc)
 

for line in fileinput.input("UI.lmx", inplace=True):
    line=re.sub(r"^.*?CDM_Weekly.*?\n", "Custom 3	Equals	CDM_Weekly."+utc,line)
    print(line.strip('\n'))






