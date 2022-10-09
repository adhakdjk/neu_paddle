from email import header
import smtplib
from email.mime.text import MIMEText
from email.header import Header
text='''付哲
付哲
付哲 '''
msg=MIMEText(text,'plain','utf-8')
msg['From']=Header('最帅')
msg['To']=Header('最美')
msg['Subject']=Header('python test')

server=smtplib.SMTP_SSL('smtp.qq.com')
server.connect('smtp.qq.com',465)
server.login('645835997@qq.com','smheqwfgdymbbbhg')
server.sendmail('645835997@qq.com','645835997@qq.com',msg.as_string())
server.quit() 