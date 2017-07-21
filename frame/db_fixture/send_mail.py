# -*- coding:utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart


#发送邮件服务器
smtpserver = 'smtp.qq.com'
#发送邮箱用户及密码
user = '531474715@qq.com'
password = 'ghykefzmdlwtbiec'
#发送邮箱
sender = '531474715@qq.com'
#接收邮箱
receiver = '531474715@163.com'
#发送邮件主题
subject = '自动化测试报告'
#构建带有附件的邮箱实例
msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = subject
msgRoot['From'] = Header("淘海房", 'utf-8')
# 邮件正文
msgRoot.attach(MIMEText('<html><body><h2>你好</h2></body></html>', 'html', 'utf-8'))
# msg['Subject'] = Header(subject, 'utf-8')

sendfile = open('C:\\Users\\js\\Desktop\\guest-master\\frame\\report\\log.txt','rb').read()  #发送的附件

att = MIMEText(sendfile,'base64', 'utf-8')
att["Content-Type"] = "application/octet-stream"
att["Content-Disposition"] = "attachment; filename='log.txt'"
msgRoot.attach(att)

#连接发送邮件
try:
    smtp = smtplib.SMTP_SSL()
    smtp.connect(smtpserver,465)
    smtp.login(user,password)
    smtp.sendmail(sender, receiver,msgRoot.as_string())
    smtp.close()
    print("邮件发送成功！")
except smtplib.SMTPException:
    print("Error:无法发送邮件")

