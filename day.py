#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from datetime import date
import os.path
import sys

MD_FILE=str(date.today()) + '.md'

if os.path.isfile(MD_FILE):
  if len(sys.argv) > 1 and sys.argv[1] == '-f':
    print 'overwrite!'
  else:
  	print MD_FILE + ' already exists. (Use -f)'   
  	sys.exit(2)  

with open('template.md') as t:
  with open(MD_FILE, 'w') as f:
    f.writelines(t.readlines())
    print  os.getcwd() + '/' + MD_FILE