import time, sys, os
sys.path.append('./interface')
sys.path.append('./db_fixture')
sys.path.append('./report')
from frame.HTMLTestRunner import HTMLTestRunner
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
import unittest
from frame.db_fixture import test_data
import smtplib

#=========定义发送邮件==========
def send_mail(file_new):
    f = open(file_new,'rb')
    mail_body = f.read()
    f.close()

    # msg = MIMEText(mail_body,'html','utf-8')
    # msg["Subject"] = Header("自动化测试报告", 'utf-8')
    #=============================================================
    message = MIMEMultipart()
    message['From'] = Header("THF project",'utf-8')
    message['To'] = Header("Teammate", 'utf-8')
    subject = '接口测试报告'
    message['Subject'] = Header(subject,'utf-8')


    message.attach(MIMEText(mail_body,'html','utf-8'))

    att1 = MIMEText(open(file_new,'rb').read(),'base64','utf-8')
    att1["Content-Type"] = "application/octet-stream"
    att1["Content-Disposition"] = "attachment; filename=test_report.html"
    message.attach(att1)

    #=============================================================
    try:
        smtp = smtplib.SMTP_SSL()
        smtp.connect("smtp.qq.com",465)
        smtp.login("xxx@qq.com","xxx")
        smtp.sendmail("xxx@qq.com","531474715@163.com", message.as_string())
        smtp.quit()
        print('email has send out!')
    except smtplib.SMTPException:
        print('email send fild!')


#=========查找测试报告路径，找到最新的测试报告文件并返回=========
def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getmtime(testreport + "\\" + fn))
    file_new = os.path.join(testreport, lists[-1])
    print(file_new)
    return file_new




if __name__ == '__main__':
    test_dir = './interface'
    test_report = 'C:\\Users\\js\\Desktop\\guest-master\\frame\\report'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='*_test.py')  # 递归查找指定目录（start_dir）及其子目录下的全部测试模块，将这些测试模块放入一个TestSuite 对象并返回。只有匹配pattern的测试文件才会被加载到TestSuite中
    test_data.init_data()
    now = time.strftime("%Y-%m-%d %H%M%S")
    filename = test_report + '\\' + now + 'result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(
        stream=fp,
        title='测试报告',
        description='用例执行情况:'
    )
    runner.run(discover)
    fp.close()

    new_report = new_report(test_report)
    send_mail(new_report)



