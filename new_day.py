#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from datetime import date
import os.path
import sys

MD_FILE=str(date.today()) + '.md'

if os.path.isfile(MD_FILE):
  print MD_FILE + ' already exists' 
  sys.exit(2)  

with open('template.md') as t:
  with open(MD_FILE, 'w') as f:
    f.writelines(t.readlines())
