import smtplib
import time
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText 
from email.mime.application import MIMEApplication 
_user = "204893985@qq.com"
_pwd = "XXXXXxxxxx"
now = time.strftime('%Y-%m-%d_%H_%M_%S')#获取时间戳

class sendEmail:
    def send_email(self,email_to,filepath):
        #如名字所示Multipart就是分多个部分
        msg = MIMEMultipart()
        msg["Subject"] = now+"华华的测试报告"
        msg["From"]  = _user
        msg["To"]   = email_to

        #---这是文字部分---
        part = MIMEText("这次是自动化测试结果，请查收！")
        msg.attach(part)

        #---这是附件部分---
        #xlsx类型附件
        part = MIMEApplication(open(filepath,'rb').read())
        part.add_header('Content-Disposition', 'attachment', filename=filepath)
        msg.attach(part)
        s = smtplib.SMTP_SSL("smtp.qq.com", timeout=30)#连接smtp邮件服务器,端口默认是25
        s.login(_user, _pwd)#登陆服务器
        s.sendmail(_user, email_to, msg.as_string())#发送邮件
        s.close()

#测试代码
if __name__=="__main__":
    email_to='1255811581@qq.com'
    filepath='kq_data_1'
    sendEmail().send_email(email_to,filepath)
