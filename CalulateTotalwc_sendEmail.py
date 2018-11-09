import smtplib
import csv
import datetime,os,shutil
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email.utils import COMMASPACE
from email import encoders

COMMASPACE = ', '

def totalwc(wcfile):
    with open(wcfile) as wc:
        headerline=wc.next()
        total = 0
        for row in csv.reader(wc):
            total += float(row[-1])
        return total

fromaddr = "v-judysu@microsoft.com"
toaddr = ["v-judysu@microsoft.com", "ejcho@microsoft.com"]
td=datetime.datetime.now()
td=td.strftime("%Y%m%d%H%M")

print(td)
newfilename=td+'_TWAnalyze_HCMApps.csv'
shutil.copy2(r'C:\test\TWAnalyze_HCMApps.csv',r'C:\test\DailyWC\%s' % newfilename)

msg = MIMEMultipart()
 
msg['From'] = fromaddr
msg['To'] = COMMASPACE.join(toaddr)
msg['Subject'] = str(td)+ " HCMApp word count"

totalwcHCM=totalwc(r'C:\test\TWAnalyze_HCMApps.csv')

body = "Based on the latest source in git repo, HCMApp total ajusted word count is " + str(totalwcHCM)
 
msg.attach(MIMEText(body, 'plain'))
 
filename = "TWAnalyze_HCMApps.csv"
attachment = open(r'C:\test\TWAnalyze_HCMApps.csv', 'rb')
 
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
msg.attach(part)
 
server = smtplib.SMTP('smtp.office365.com', 587)
server.starttls()
server.login(fromaddr, "niki999(")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()


