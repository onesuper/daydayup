# -*- coding: UTF-8 -*-

from daydayup import __version__
from daydayup.exception import DayDayUpException
from daydayup.filesystem import File, Directory

import os
import sys
from argparse import ArgumentParser

from datetime import date
TODAY_REPORT_FNAME = str(date.today()) + '.md'

import yaml
with open('config.yaml') as f:
  CONF = yaml.safe_load(f)

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
      raise ValueError("无效输入: '%s'" % default)

  while True:
    sys.stdout.write(question + prompt)
    choice = raw_input().lower()
    if default is not None and choice == '':
      return valid[default]
    elif choice in valid:
      return valid[choice]
    else:
      sys.stdout.write("请回答 'yes' 或 'no' (或 'y' 或 'n').\n")


def send_mail(server, fro, to, subject, text): 
  from email.mime.multipart import MIMEMultipart
  from email.MIMEText import MIMEText
  from email.utils import COMMASPACE,formatdate
  from email import encoders

  assert type(server) == dict 
  assert type(to) == list 

  tos = COMMASPACE.join(to)

  prompt = '一封主题为"' + subject.encode('utf-8') + '"的邮件将发送给 '+ tos
  if yes_or_no(prompt + '\n你真的确定要发送吗?'):
    msg = MIMEMultipart() 
    msg['From'] = fro 
    msg['Subject'] = subject 
    msg['To'] = tos
    msg['Date'] = formatdate(localtime=True) 
    msg.attach(MIMEText(text, 'html', 'utf-8'))

    import smtplib 
    smtp = smtplib.SMTP(server['name']) 
    smtp.starttls()
    smtp.login(server['email'], server['passwd']) 
    smtp.sendmail(fro, to, msg.as_string()) 
    smtp.close()


def get_github_commits(github_id, github_password):
  from github import GitHub
  gh = GitHub(username=github_id, password=github_password)
  sys.stderr.write('fetch data from github...\n')
  events = gh.users(github_id).events.get()
  commits = []
  for e in events:
    commit = {}
    try:
      commit['msg'] = e['payload']['commits'][0]['message']
      commit['url'] = e['payload']['commits'][0]['url']
      commit['sha'] = e['payload']['commits'][0]['sha'][:6]
      commits.append(commit)
    except KeyError:
      pass
  return commits


def render_template(name, vars_ = {}):
  """
  根据变量和模板文件生成内容
  """
  from jinja2 import Environment, FileSystemLoader
  env = Environment(loader=FileSystemLoader('.'))
  template = env.get_template(name) 
  return template.render(**vars_)


class DayDayUp(object):

  def __init__(self, args = None):
    self.opts = self._get_opts(args)
    self.opts['func']()

  """今日生成日报"""
  def _new(self):

    outf = File(self.opts['output'])
    if outf.exists:
      if self.opts['force']:
        sys.stderr.write('强制覆盖老的日报!\n')
        outf.rm()
      else:
        raise DayDayUpException(str(outf) + ' 已经存在. (强制覆盖请使用 --force)\n')

    # github commits
    commits = []
    if CONF['github']['enable']:
      commits = get_github_commits(CONF['github']['username'], CONF['github']['password'])

    # report
    import glob
    report = {}
    report['files'] = (glob.glob1('.','*-*-*.md'))

    # render and make file
    content = render_template(self.opts['template'], {'report': report, 'commits': commits})
    outf.content = content
    outf.mk()
    sys.stderr.write('请认真编辑今天的日报: '+ str(outf) + '\n') 
          
  """发送今日日报"""  
  def _send(self):
    inf = File(self.opts['file'])

    import markdown
    html = markdown.markdown(inf.content)

    if self.opts['preview']:
      sys.stdout.write(html)
      sys.stdout.write('\n\n')
    else:
      sys.stdout.write('友情提示：使用 --preview 检查一遍错别字哦 ^_^\n')

    # 主题 
    subject = '-'.join(['DailyReport', str(date.today()), CONF['nickname']])
    mail_from = CONF['server']['email']
    mail_to   = CONF['dl']

    send_mail(CONF['server'], mail_from, mail_to, subject, html)

  def _get_opts(self, args):
    opts = {}
    parser = ArgumentParser()
    subparser = parser.add_subparsers()
    parser.add_argument('-v', '--version', action = 'version', version = '{0}'.format(__version__),
                        help = 'show %(prog)s\'s version')
    
    new = subparser.add_parser('new')
    new.set_defaults(func = self._new)
    new.add_argument('--force', '-f', action = 'store_true', help = '覆盖已经存在的日报')
    new.add_argument('--template', '-t', default = 'daily.md', help = '指定日报的模板')
    new.add_argument('--output', '-o', default = TODAY_REPORT_FNAME, help = '要生成的日报文件')


    send = subparser.add_parser('send')
    send.set_defaults(func = self._send)
    send.add_argument('--preview', action = 'store_true', help = '预览发送的内容')
    send.add_argument('--file', '-f', default = TODAY_REPORT_FNAME, help = '指定要发送的文件')


    # process the opts
    for option, value in vars(parser.parse_args(args)).iteritems():
      if value is not None:
        if isinstance(option, str):
          option = option.decode('utf-8')
        if isinstance(value, str):
          value = value.decode('utf-8')
        opts[option] = value
    
    return opts
