#!/usr/bin/env python
# -*- coding: UTF-8 -*-
 
import sys
import os

def markdown2html(s):
  import markdown
  return markdown.markdown(s)

def send_mail(server, fro, to, subject, text): 
  from email.mime.multipart import MIMEMultipart
  from email.MIMEText import MIMEText
  from email.utils import COMMASPACE,formatdate
  from email import encoders

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


def yes_or_no(question, default="no"):
  valid = {"yes": True, "y": True, "ye": True,
           "no": False, "n": False}
  if default is None:
      prompt = " [y/n] "
  elif default == "yes":
      prompt = " [Y/n] "
  elif default == "no":
      prompt = " [y/N] "
  else:
      raise ValueError("invalid default answer: '%s'" % default)

  while True:
    sys.stdout.write(question + prompt)
    choice = raw_input().lower()
    if default is not None and choice == '':
      return valid[default]
    elif choice in valid:
      return valid[choice]
    else:
      sys.stdout.write("Please respond with 'yes' or 'no' "
                       "(or 'y' or 'n').\n")

def preview(content):
  if len(sys.argv) > 1 and sys.argv[1] == '-v':
    sys.stdout.write(content)
    sys.stdout.write('\n\n')


def string_from_file():
  from datetime import date
  mdfile = str(date.today()) + '.md'
  with open(mdfile) as f:
    return '\n'.join(f.readlines())

def get_config(name):
  with open(name) as f:
    import yaml
    return yaml.safe_load(f)


if __name__ == '__main__':
  conf = get_config('config.yaml')
  s = string_from_file()
  html = markdown2html(s)
  preview(html)

  from datetime import date

  subject = '-'.join(['DailyReport', str(date.today()), conf['nickname']])
  mail_from = conf['server']['email']
  mail_to   = conf['dl']

  if yes_or_no('to: '+ ','.join(mail_to) + '\n'+ 'r u sure?'):
    send_mail(conf['server'], mail_from, mail_to, subject, content)

