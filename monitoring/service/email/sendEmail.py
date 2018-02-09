#!/opt/python3/bin/python3
# -*- coding: UTF-8 -*-
__doc__ = "check spark job heathy state"
__author__ = "bigdata supprot zhongyin.miao with l3 team"

import smtplib
from email.mime.text import MIMEText
from email.header import Header


class SmtpConfig(object):

    def __init__(self, host,port, user, passwd, sender, receivers):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.sender = sender
        self.receivers = receivers


class MessageInfo(object):
    def __init__(self, mine, sender, receiver, subject, ):
        self.mine = mine
        self.sender = sender
        self.receiver = receiver
        self.subject = subject


    def set_message(self):
        message = MIMEText(self.mine, 'plain', 'utf-8')
        message['From'] = Header(self.sender, 'utf-8')
        message['To'] = Header(self.receiver, 'utf-8')
        message['Subject'] = Header(self.subject, 'utf-8')
        return message.as_string()




def sendEmail(smtp,message):
    try:
         smtpObj = smtplib.SMTP_SSL(smtp.host, smtp.port)
         smtpObj.login(smtp.user, smtp.passwd)
         smtpObj.sendmail(smtp.sender, smtp.receivers, message)
         return "邮件发送成功"
    except (smtplib.SMTPException) as e:
         return "Error: 无法发送邮件" + str(e)

#smtp_config = SmtpConfig(host="smtp.qq.com",port=465,user="853945306@qq.com",passwd="qyrdbvgcjngrbcaa",sender="853945306@qq.com",receivers=["853945306@qq.com"])
#messageinfo = MessageInfo(mine="Python 邮件发送测试...",sender="starbucks CDH platform",receiver="starbucks team",subject="starbucks cdh platform")
#messages = messageinfo.set_message()

#if __name__ == "__main__":
    #sendEmail(smtp_config,messages)
