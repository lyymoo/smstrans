### python语言
1. python面向对象
2. [python设计模式](https://github.com/faif/python-patterns)
3. python源码阅读
4. 编译原理（解释器cPython、pypy）
5. 包管理pip、virtualenv、setuptools(easy_install)、venv、conda（OS-agnostic, system-level binary package manager and ecosystem，anaconda发行版的包管理工具）
- PyPI – the Python Package Index · PyPI 是python官方的软件库
- Python Packaging Authority — PyPA documentation python第三方包的工作组，是一个社群组织，负责维护python的包
- Anaconda是一种Python语言的免费增值 开源发行版，用于进行大规模数据处理, 预测分析, 和科学计算, 致力于简化包的管理和部署。 Anaconda使用软件包管理系统Conda进行包管理。
- wheel - [The official binary distribution format for Python](https://github.com/pypa/wheel)
6. [数据结构](https://www.zhihu.com/question/21318658)
7. [算法](https://github.com/linyiqun/DataMiningAlgorithm) 数据挖掘18大算法
8. [应用-机器学习](https://github.com/josephmisiti/awesome-machine-learning#python)
- Computer Vision计算机视觉
- Natural Language Processing自然语言处理
- General-Purpose Machine Learning通用机器学习
- Data Analysis / Data Visualization数据分析与数据可视化
- Misc Scripts / iPython Notebooks / Codebases其他脚本/iPython笔记本/代码库
- Neural Networks神经网络
- Kaggle Competition Source Code kaggle比赛源代码
- Reinforcement Learning强化学习
- [统计学知识](http://open.163.com/special/opencourse/statistics.html)
9. 应用-GUI图形界面
- Tkinter : Tkinter
- wxPython: wxPython
- PyGTK: PyGTK
- PyQt: PyQt、PyQt5、PyQt5-sip
- PySide: PySide、PySide2
10. 应用-Web框架
- django： django
- web2py：web2py
- flask： flask
- bottle： bottle
- tornadoweb ：tornadoweb
- webpy： webpy
- cherrypy： cherrypy（感谢@钢琴手 提供信息）
- jinjs： jinja（感谢@钢琴手 提供信息）
11. 应用-数据采集
- scrapy： scrapy
- pyspider： pyspider
- portia： portia
- html2text： html2text
- BeautifulSoup： BeautifulSoup
- lxml： lxml
- selenium：selenium
- mechanize： mechanize
- PyQuery： pyquery
- creepy： creepy
12. [应用-实用轮子](https://github.com/vinta/awesome-python)
- （https://zhuanlan.zhihu.com/p/21563130）
- elasticsearch弹性搜索
13. hls流媒体传输协议（m3u8）
- HLS(http Live Streaming)是Apple的动态码率自适应技术


### C语言
- [memcached分布式高速缓存系统](https://github.com/memcached/memcached)
- [redis键值对存储数据库](https://github.com/antirez/redis)
- LevelDB
- Mongodb
- Mysql
- [mTCP用于多核系统的高度可扩展的用户级TCP堆栈](https://github.com/eunyoung14/mtcp)
### GO语言
- [FastDFS 分布式文件存储系统](https://github.com/happyfish100/fastdfs)
- [codis基于代理的Redis集群解决方案，支持管道和动态扩展](https://github.com/CodisLabs/codis)

### job direction-python高性能web开发
- [cpython](https://github.com/python/cpython)
- [django](https://github.com/django/django) 20050721
- [tornado](https://github.com/tornadoweb/tornado) 2009
- [webpy](https://github.com/webpy/webpy) 23 Feb 2006
- [flask](https://github.com/pallets/flask) 2010年4月1日
- [twisted](https://github.com/twisted/twisted) event-driven 2000
- [sqlalchemy ORM](https://github.com/zzzeek/sqlalchemy)
- [peewee](https://github.com/coleifer/peewee)
- [SQLObject](https://github.com/sqlobject/sqlobject)
- [Storm A simple ORM for Tornado](https://github.com/ccampbell/storm)
- [The Jinja2 template engine](http://jinja.pocoo.org/)pallets/jinja](https://github.com/pallets/jinja)
- [Asynchronous HTTP client/server framework for asyncio and Python](https://github.com/aio-libs/aiohttp)
- [odoo](https://github.com/odoo/odoo) ERP
- [gunicorn](https://github.com/benoitc/gunicorn)
- [python-ngrok](https://github.com/hauntek/python-ngrok)
- [python-ngrokd](https://github.com/hauntek/python-ngrokd)
- [wechatpy](https://github.com/messense/wechatpy)
- [requests](https://github.com/requests/requests)
- [mysqlclient](https://github.com/PyMySQL/mysqlclient-python)
- [django channels](https://github.com/django/channels)
- [Accounts for Django](https://github.com/bread-and-pepper/django-userena)
- [celery](https://github.com/celery/celery)
- [salt](https://github.com/saltstack/salt)
- [redis-py](https://github.com/andymccurdy/redis-py)
- [alipay](https://github.com/lxneng/alipay)
- [python-oauth2](https://github.com/joestump/python-oauth2)
- [XlsxWriter](https://github.com/jmcnamara/XlsxWriter)
- [qrcode](https://github.com/sylnsfar/qrcode)
- [jupyter](https://github.com/jupyter/jupyter)
### 服务开发：同步事件循环、异步事件循环
> IO复用、I/O事件通知机制 even loop/deamon：select (Unix)、poll、epoll、kqueue
> https://zh.wikipedia.org/wiki/Select_(Unix)
- [shadowsocks](https://github.com/shadowsocks/shadowsocks)
- [python-proxy](https://github.com/qwj/python-proxy)
### person research-数据搜集、处理与分析
- [scipy/scipy](https://github.com/scipy/scipy)
- [scikit-learn](https://github.com/scikit-learn/scikit-learn)
- [numpy](https://github.com/numpy/numpy)
- [pandas](https://github.com/pandas-dev/pandas)
- [matplotlib](https://github.com/matplotlib/matplotlib)
### 高性能微服务python后端异步方案
- [基于 Sanic 的微服务基础架构](https://www.v2ex.com/t/417601)
```
Feature:
使用sanic异步框架，简单，轻量，高效。
使用uvloop为核心引擎，使sanic在很多情况下单机并发甚至不亚于Golang。
使用asyncpg为数据库驱动，进行数据库连接，执行sql语句执行。
使用aiohttp为Client，对其他微服务进行访问。
使用peewee为ORM，但是只是用来做模型设计和migration。
使用opentracing为分布式追踪系统。
使用unittest做单元测试，并且使用mock来避免访问其他微服务。
使用swagger做API标准，能自动生成API文档。
```
- [sanic](https://github.com/huge-success/sanic)
- [sanic-ms](https://github.com/songcser/sanic-ms)
- 使用[asyncpg](https://github.com/MagicStack/asyncpg)为数据库驱动，进行数据库连接，执行 sql 语句执行。
- [aiomysql](https://github.com/aio-libs/aiomysql)
- [slim web framework based on aiohttp and peewee/asyncpg](https://github.com/fy0/slim)
- [WTForms](https://github.com/wtforms/wtforms/) is a flexible forms validation and rendering library for Python web development
- [aiohttp](https://github.com/aio-libs/aiohttp)
- [msgpack-python]serialization(https://github.com/msgpack/msgpack-python)
- aiosmtplib异步邮件客户端
- [aioauth-client](https://github.com/klen/aioauth-client)异步认证
- aioredis异步redis

### python 先01
1. python official document
2. python基础教程、入门教程、核心编程
3. python源码分析影印版
4. python源码分析文字版
5. python的面向对象
6. python的设计模式

### github awesome 进阶学习
- [利用Python进行数据分析](https://github.com/BrambleXu/pydata-notebook)
- [The Flask Mega-Tutorial教程](https://github.com/luhuisicnu/The-Flask-Mega-Tutorial-zh)
- [数据挖掘18大算法实现以及其他相关经典DM算法](https://github.com/linyiqun/DataMiningAlgorithm)
- [python-patterns设计模式](https://github.com/faif/python-patterns)
- [设计模式](https://github.com/me115/design_patterns)
- [open-source-mac-os-apps](https://github.com/serhii-londar/open-source-mac-os-apps)
- [收集所有区块链(BlockChain)技术开发相关资料](https://github.com/chaozh/awesome-blockchain-cn)
- [A curated list of awesome Machine Learning](https://github.com/josephmisiti/awesome-machine-learning)
- [Awesome Deep Learning](https://github.com/ChristosChristofidis/awesome-deep-learning)
- [后端架构师技术图谱](https://github.com/xingshaocheng/architect-awesome)
- [中文版 Apple 官方 Swift 教程](https://github.com/numbbbbb/the-swift-programming-language-in-chinese)
- [深度学习专项课程](https://github.com/HuangCongQing/deeplearning.ai-note)
- [经典编程书籍大全](https://github.com/jobbole/awesome-programming-books)
- [后端开发面试题](https://github.com/monklof/Back-End-Developer-Interview-Questions)
- [前端开发面试问题及答案整理](https://github.com/BearD01001/front-end-QA-to-interview)
- [GitHub最全的前端资源汇总仓库](https://github.com/helloqingfeng/Awsome-Front-End-learning-resource)
- [《The AWK Programming Language》中文翻译](https://github.com/youngsterxyf/The-AWK-Book-cn)
- [全栈增长工程师指南](https://github.com/phodal/growth-ebook)
- [一本关于排序算法的 GitBook 在线书籍 《十大经典排序算法》](https://github.com/hustcc/JS-Sorting-Algorithm)
- [免费的计算机编程类中文书籍](https://github.com/justjavac/free-programming-books-zh_CN)
- [设计模式：PHP和Go语言实现](https://github.com/hoohack/DesignPattern)
- [PHP 资源大全中文版](https://github.com/jobbole/awesome-php-cn)
- [RESTful API 设计参考文献列表](https://github.com/aisuhua/restful-api-design-references)
- [优秀REST风格 API的设计原则](https://blog.csdn.net/houjixin/article/details/54315835)

### ipython/jupyter notebook/data science
- [Ipython](https://github.com/ipython/ipython)
- [数据科学Python笔记本](https://github.com/donnemartin/data-science-ipython-notebooks)
- [IPython-Dashboard](https://github.com/litaotao/IPython-Dashboard)
- [IPython in-depth Tutorial](https://github.com/ipython/ipython-in-depth)
- [%%sql magic for IPython](https://github.com/catherinedevlin/ipython-sql)
- [IPython Notebooks](https://github.com/jdwittenauer/ipython-notebooks)
- [Various ipython notebooks](https://github.com/julienr/ipynb_playground)
- [使用python进行科学计算讲座，作为IPython笔记本。](https://github.com/jrjohansson/scientific-python-lectures)
- [Python Data Science Handbook](https://github.com/jakevdp/PythonDataScienceHandbook)

### python量化资料
- [TuShare stock历史数据](https://github.com/waditu/tushare)
- [匠芯量化](https://github.com/kzil88/JXQuant)
- [tushare金融大数据社区](https://tushare.pro/document/1)

### BSD操作系统家族
> [BSD]](https://www.bsd.org/) Apple Mac OS X、The DragonFly BSD Project、FreeBSD、m0n0wall、The NetBSD Project、
> The OpenBSD Project、OpenDarwin、PC-BSD、PicoBSD、TrustedBSD
> [BSD家族](https://zh.wikipedia.org/wiki/BSD)
> [offical site]](https://www.freebsd.org/)
> FreeBSD is an operating system used to power modern servers, desktops, and embedded platforms. 
> A large community has continually developed it for more than thirty years. Its advanced networking, 
> security, and storage features have made FreeBSD the platform of choice for many of the busiest web sites 
> and most pervasive embedded networking and storage devices.
> BSD变种的用户比例条形图: FreeBSD 77%, OpenBSD 32.8%, NetBSD 16.3%, DragonFly BSD 2.6%, Other 6.6%
- [FreeBSD](https://zh.wikipedia.org/wiki/FreeBSD) [中文手册](https://www.freebsd.org/doc/zh_CN/books/handbook/)
- [TrueOS](https://www.trueos.org/) PC-BSD evolves into TrueOS
- [DesktopBSD]](https://zh.wikipedia.org/wiki/DesktopBSD)
- [GhostBSD](https://zh.wikipedia.org/wiki/GhostBSD)
- FreeNAS，一个基于FreeBSD的NAS轻量级服务器




