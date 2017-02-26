#!/usr/bin/env python3
# -*- coding:utf-8 -*-


import smtplib
from email.mime.text import MIMEText


mail_host = 'smtp.qq.com'
mail_user = '770362426'
mail_pass = ''
mail_postfix = 'qq.com'


def send_mail(to_list, sub, content):
    me = '<' + mail_user + "@" + mail_postfix + '>'
    msg = MIMEText(content, _subtype='plain', _charset='utf8')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        server = smtplib.SMTP()
        server.connect(mail_host)
        server.login(mail_user, mail_pass)
        server.sendmail(me, to_list, msg.as_string())
        server.close()
        return True
    except Exception as e:
        print(e)
        return False
