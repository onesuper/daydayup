#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from datetime import date
import os
import sys

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

if __name__ == '__main__':

  mdfile = str(date.today()) + '.md'

  if os.path.isfile(mdfile):
    if len(sys.argv) > 1 and sys.argv[1] == '-f':
      sys.stderr.write('overwrite!\n')
    else:
      sys.stderr.write(mdfile + ' already exists. (Use -f)\n')
      sys.exit(2)  
  
  report = {}
  report.update(get_files())
  s = render_from_file('template.md', {'report': report})

  with open(mdfile, 'w') as f:
    f.write(s)
    sys.stderr.write(os.getcwd() + '/' + mdfile + '\n')
