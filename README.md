# DayDayUp

Daydayup 是一个给 Baixingers 发送日报的工具，它可以让你用 Markdown 来书写日报

## 使用

从 Pip 安装：

```
$ pip install daydayup
```

从源代码安装：

```
$ git clone <git clone URL>
$ cd daydayup
$ python setup.py install
```

配置你的账号、昵称和邮件账号

```
$ cp config.yaml.template config.yaml
$ vi config.yaml
```

创建今天的日报

```
$ daydayup new
```

上面这条命令会在当前目录下生成 `yyyy-mm-dd.md` 的日报文件，用你喜欢的 markdown 编辑器编辑它，编辑完毕以后使用如下命令发送邮件

```
$ daydayup send
```

## 模板参数

Daydayup 提供了一些默认参数可以在模板（template.md）中引用：

* 所有日报文件总数：`{{ report.files | length}} `


* 所有日报文件列表：`{{ report.files }} `
* github 的最近提交：`{% for commit in commits %}`
* github commit: `{{ commit.url }}`, `{{ commit.msg }}`, `{{ commit.sha}}`

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

* ~~命令行工具集成~~
* ~~setup.py 打包~~
* ~~模板参数引用。例如：{{ reports.count }}~~ 
* 发送请假的邮件
* 编译成周报、月报
* ~~从 github 同步当日的 commit~~
* 支持通过 project#1 直接生成一个 github 的 issue link
* 支持 Python3
* 支持在日报中 @someone