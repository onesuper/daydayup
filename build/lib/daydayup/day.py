#!/usr/bin/env python
# -*- coding: UTF-8 -*-


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
