#!/usr/bin/env python
# -*- coding: UTF-8 -*-
 
from email.mime.multipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.utils import COMMASPACE,formatdate
from email import encoders
 

def md_to_html(s):
    import markdown
    return markdown.markdown(s.decode('utf-8'))

def send_mail(server, fro, to, subject, text): 
    assert type(server) == dict 
    assert type(to) == list 
 
    msg = MIMEMultipart() 
    msg['From'] = fro 
    msg['Subject'] = subject 
    msg['To'] = COMMASPACE.join(to)
    msg['Date'] = formatdate(localtime=True) 
    msg.attach(MIMEText(text, 'html', 'utf-8'))

    import smtplib 
    smtp = smtplib.SMTP(server['name']) 
    smtp.starttls()
    smtp.login(server['email'], server['passwd']) 
    smtp.sendmail(fro, to, msg.as_string()) 
    smtp.close()

with open('config.yaml') as f:
    import yaml
    dataMap = yaml.safe_load(f)

    from datetime import date
    subject = '-'.join(['DailyReport', str(date.today()), dataMap['nickname']])

    with open(str(date.today()) + '.md') as f:
        content = md_to_html('\n'.join(f.readlines()))
        send_mail(dataMap['server'], dataMap['server']['email'], dataMap['dl'], subject, content)