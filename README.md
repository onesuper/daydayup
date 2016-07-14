# DayDayUp

Daydayup 是一个给 Baixingers 用 Markdown 来编写（发送）日报的简单工具

## 快速开始

```shell
# 下载，安装依赖
$ git clone https://github.com/onesuper/daydayup.git
$ sudo pip install -r requirements.txt 

# 配置账号和昵称
$ cp config.yaml.template config.yaml
$ vi config.yaml

# 新建今日日报
$ ./day.py     
$ ./day.py -f (overwite)

# day.py 会在当前目录下生成格式为 yyyy-mm-dd.md 的文件
# 使用 Markdown 编辑它
$ emacs 2016-01-01.md

# 通过邮件发送日报
$ ./day_up.py 
$ ./day_up.py -v (with preview)
```

## 模板参数

Daydayup 提供了一些参数可以在日报模板（template.md）中引用：

* 所有日报文件总数：`{{ report.files | length}} `


* 所有日报文件列表：`{{ report.files }} `
* github 的最近提交：`{% for commit in commits %}`
* 每次提交的属性: `{{ commit.url }}`, `{{ commit.msg }}`, `{{ commit.sha}}`

## 配置

```yaml
nickname: onesuper
server:
  name: smtp.partner.outlook.cn
  email: chengyichao@baixing.com
  passwd: 123456
dl:
  - daily@baixing.com
  - daily_engineer@baixing.com
github:
  enable: false
  username: onesuper
  password: 123456
```

## 依赖

* PyYaml
* Python-Markdown
* Jinja2


## TODO

* 集成在一个命令行工具中
* setup.py 打包
* ~~模板参数引用。例如：{{ reports.count }}~~ 
* 发送请假的邮件
* 编译成周报、月报
* ~~从 github 同步当日的 commit~~
* 支持通过 {{ name#1 }} 直接生成一个 github 的 issue link
* 支持 Python3
* 接收别人的日报，并提取出@自己的条目 (via Billy)
* 支持在日报中 @someone