# DayDayUp

Daydayup 是一个给 Baixingers 用 Markdown 来编写（发送）日报的简单工具

## 开始

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

# 通过邮件发送日报
$ ./day_up.py 
$ ./day_up.py -v (with preview)
```

## 参数

Daydayup 提供了一些参数可以在日报模板（template.md）中引用：

* 所有日报文件总数：`{{ report.files | length}} `


* 所有日报文件列表：`{{ report.files }} `

## 依赖

* PyYaml
* Python-Markdown
* Jinja2


## TODO

* 集成在一个命令行工具中
* 打包
* ~~模板参数引用。例如：{{ reports.count }}~~ 
* 发送请假的邮件
* 编译成周报、月报
* 从 github 同步当日的 commit
* 支持通过 {{ name#1 }} 直接生成一个 github 的 issue link