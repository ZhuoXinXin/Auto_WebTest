from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr
import smtplib
import unittest
import time
import os


#  定义发送邮件
def send_mail(file_new):
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()

    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['Subject'] = Header('自动化测试报告', 'utf-8')
    msg['From'] = formataddr(['自动化测试报告', '844715250@qq.com'], 'utf-8')

    smtp = smtplib.SMTP()
    smtp.connect('smtp.qq.com')
    smtp.login('844715250@qq.com', 'ufnrkzofxjwmbcgb')
    smtp.sendmail('844715250@qq.com', 'zhuoxinxin@vip.qq.com', msg.as_string())
    smtp.quit()
    print('emil has send out !')

# 查找测试报告目录，找到最新生成的测试报告文件
def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getmtime(testreport + '\\' + fn))
    file_new = os.path.join(testreport, lists[-1])
    print(file_new)
    return file_new

if __name__ == '__main__':
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    filename = './CM/report/' + now + 'result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='CM自动化测试报告',
                            description='环境win10 浏览器:chrome')
    discover = unittest.defaultTestLoader.discover('./CM/test_case',
                                                   pattern='*_sta.py')
    runner.run(discover)
    fp.close()
    file_path = new_report('./CM/report/')
    send_mail(file_path)

