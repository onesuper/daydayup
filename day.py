#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from datetime import date
import os
import sys


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


def render_from_file(name, vars_ = {}):
  from jinja2 import Environment, FileSystemLoader
  from jinja2.exceptions import TemplateNotFound
  from datetime import date
  try:
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template(name) 
  except TemplateNotFound:
    raise IOError('Run day.py to gen today\'s report first\n')
  return template.render(**vars_)


def get_files():
  import glob
  reports = {}
  reports['files'] = (glob.glob1('.','*-*-*.md'))
  return reports

def get_config(name):
  with open(name) as f:
    import yaml
    return yaml.safe_load(f)

if __name__ == '__main__':

  mdfile = str(date.today()) + '.md'

  if os.path.isfile(mdfile):
    if len(sys.argv) > 1 and sys.argv[1] == '-f':
      sys.stderr.write('overwrite!\n')
    else:
      sys.stderr.write(mdfile + ' already exists. (Use -f)\n')
      sys.exit(2)  

  commits = []
  conf = get_config('config.yaml')
  if conf['github']['enable']:
    commits = get_github_commits(conf['github']['username'], conf['github']['password'])

  report = {}
  report.update(get_files())
  s = render_from_file('template.md', {'report': report, 'commits': commits})

  with open(mdfile, 'w') as f:
    f.write(s)
    sys.stderr.write(os.getcwd() + '/' + mdfile + '\n')
