# DayDayUp

Daydayup 是一个给 Baixingers 发送日报的工具，它可以让你用 Markdown 来书写日报

## 安装 & 使用

从 PyPi 安装：

```
$ pip install daydayup
```

配置账号、昵称和邮件账号

```
$ cp config.yaml.template config.yaml
$ vi config.yaml
```

创建日报

```
$ daydayup new
```

发送邮件

```
$ daydayup send
```

## Miscellaneous


### Template Variables

Daydayup 提供了一些默认参数可以在模板（template.md）中引用：

* 所有日报文件总数：`{{ report.files | length}} `
* 所有日报文件列表：`{{ report.files }} `
* github 的最近提交：`{% for commit in commits %}`
* github commit: `{{ commit.url }}`, `{{ commit.msg }}`, `{{ commit.sha}}`

## TODO

* ~~命令行工具集成~~
* ~~setup.py 打包~~
* ~~模板参数引用。例如：{{ reports.count }}~~ 
* 发送请假的邮件
* 编译成周报、月报
* ~~从 github 同步当日的 commit~~
* 支持通过 project#1 直接生成一个 github 的 issue link
* 支持 Python3
* ~~@someone~~