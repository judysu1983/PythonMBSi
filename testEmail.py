import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email.utils import COMMASPACE
from email import encoders

COMMASPACE = ', '

fromaddr = "v-judysu@microsoft.com"
toaddr = ["v-judysu@microsoft.com", "suli2921@gmail.com"]
 
msg = MIMEMultipart()
 
msg['From'] = fromaddr
msg['To'] = COMMASPACE.join(toaddr)
msg['Subject'] = "SUBJECT OF THE EMAIL"
 
body = "Today's word count for HCMApps"
 
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
server.login(fromaddr, "lina555%")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
