# 官方文档+cpython开源github工程目录结合阅读

## what's new in python3.6
### summary release highlights
- new syntax features
- new library modules
- cpython implementation improvements
- significant improvements in the standard library
- security improvements
- windows improvements
### new features
- "f" function
- variable annotations
- >>> 1_000_000_000_000_000
- asynchronous
- pathlib
- disambiguation
- change windows filesystem/console encoding to UTF8
- presering order
- frame evaluation
- pythonmalloc
- probing support
- other language changes
### new modules
- secrets
### improved modules
- array,ast,asyncio,binascii,cmath,collections,concurrent,contextlib,datetime,decimal
- distutils,email,encoding,enum,faulthandle,fileinput,hashlib,http.client,idlelib,
- importlib,inspact,json,logging,math,mutiprocessing,os,pathlib,pickle,pickletools
- ~ pickle(serialization,marshalling:save from memory to disk or send to network) ~
- pydoc,random,re,readline,rlcompleter,shlex,sqlite3,socket,socketserver,ssl,statistics
- struct,subprocess,sys,telnetlib,time,timeit,tkinter,taceback,tracemalloc,typing,
- unicodedata,unittest.mock,urllib.request,urllib.robotparser,venv,warnings,winreg,
- winsound,xmlrpc.client,zipfile,zlib
### optimizations
### build and c api changes
### other improvements
### deprecated
- deprecated modules,function,methods:
- asynchat,asyncore,dbm,distutils,grp,importlib,os,re,ssl,tkinter,venv
### removed
### porting to python 3.6
### Notable changes in Python 3.6.2

## Tutorial
### whetting your appetite
- high-level language
### using the python interpreter
- invoking the interpreter type:run python
- python -c or python -m
- interactive mode:">>>"
- interpreter and environment
- # -*- coding: encoding -*-
- #!/usr/bin/env python3
### an infomal introduction to python
- use python as a calculator
- first steps towards programming
### more control flow tools
- if,for,range,break,continue,else,pass,while
- defining functions
- default argument(a="" form),keyword argument(a,b,c form)
- arbitrary argument list(*args form)
- unpacking argument list(unpack *args form)
- lambda expressions,documentation strings description
- function annotations
- intermezzo:PEP8(python coding style)
### data structures
- list
- tuple
- sets
- dictionary
### modules
- package,object,dir()
### input and output
- console,write to file,graph,human-readable form,or some of the possibilities.
### errors and exceptions
- exceptions
- handling exceptions
- raising exceptions
- user-defined exceptions
- defining clean-up actions
- predefined clean-up actions: about "with" statement
### classes
- scopes and namespaces
- class objects
- inheritance
- multiple inheritance
- private variables
### brief tour of the standard library
- operating system interface:os package,sys package
- directory file wildcard searches:glob package
- mathematics
- internet access:urllib,smtplib
- date and time:datetime,time
- data compression:zlib, gzip, bz2, lzma, zipfile and tarfile.
- python running time cost:timeit.Time
- python code quality:doctest,unittest
- batteries included:xmlrpc.client,xmlrpc.server(XML Remote Procedure Call),email,json,xml,csv,sqlite3,gettext,locale,codecs
- output formatting:reprlib,pprint,textwrap
- the string module Templating
- binary data record layouts:struct,unpack,
- multi-threading
- logging:critical error,use in multiprocess:ConcurrentLogHandler 0.9.1,pip install ConcurrentLogHandler==0.9.1
- week references:weakref,gc(garbage collection)
- working lists tool:array,collections.deque(),bisect(sorted lists),heapq
- Decimal Floating Point Arithmetic:decimal,round,sum
### virtual environments and packages
- internal module:venv; third module: virtualenv etc.
- managing packages with pip; third module: Anaconda(conda)
### What Now?
- python resources
- more python resources
- frequently asked questions
### interactive input and history subsititution
- tab completion and history editing
- alternatives to interactive interpreter
- enhanced interactive environment is IPython and bpython
### floating point arithmetic: Issues and limitations
- float in computer hardware as base 2 fractions
- representation error
### appendix
- error handing: control-c
- executable python script: #!/usr/bin/env python3.5, $ chmod +x myscript.py
- the interactive startup file
- the customization modules

## The Python Standard Library
### introduction
### built-in function
- [that are now builtin modules](https://github.com/python/cpython/tree/master/Modules)
- about mathematical
- about sequence
- about object
- about string and character
- about binary conversion
- about data structure
- about sequence process
### built-in constants
- False, True, None, NotImplemented, Ellipsis
- module site: this module is automatically imported during initialization
### built-in types
- true value testing/boolean operation/comparisons
- numeric type - integer float complex
- iterator type - __iter__() __next__()
- sequence type - list tuple range
- text sequence type - str
- binary sequence type - bytes bytearray memoryview
- set type - set frozenset
- mapping type - dict
- context manager type - with statement
- other built-in type - modules, class, functions, methods, code object,
- type object, the null object, the ellipsis objects, the noimplatemented
- object, boolean values, internal objects
- special attributes
### built-in exceptions
- base classes: BaseException, Exception...
- concrete exception: usually exceptions, Os exceptions
- warnings
- exception hierarchy
### text processing services
- string: common string operations - constants/custom string formatting and syntax
- re: regular expression operations - syntax/function/expression
- difflib: helpers for computing deltas - SequenceMatcher/Diff object
- textwrap: text wrapping and filling
- unicodedata: Unicode Database
- string prep: internet string preparation
- readline: GNU readline interface
- rlcomplete: completion function for GNU readline
### binary data services
- struct — Interpret bytes as packed binary data
- codecs — Codec registry and base classes
### data types
- datetime — Basic date and time types
- calendar — General calendar-related functions
- collections — Container datatypes
- collections.abc — Abstract Base Classes for Containers
- heapq — Heap queue algorithm
- bisect — Array bisection algorithm
- array — Efficient arrays of numeric values
- types — Dynamic type creation and names for built-in types
- copy — Shallow and deep copy operations
- pprint — Data pretty printer
- reprlib — Alternate repr() implementation
- enum — Support for enumerations
### numeric and mathematical modules
- numbers — Numeric abstract base classes
- math — Mathematical functions
- cmath — Mathematical functions for complex numbers
- decimal — Decimal fixed point and floating point arithmetic
- fractions — Rational numbers
- random — Generate pseudo-random numbers
- statistics — Mathematical statistics functions
### functional programming modules
- itertools — Functions creating iterators for efficient looping
- functools — Higher-order functions and operations on callable objects
- operator — Standard operators as functions
### file and directory access
- pathlib — Object-oriented filesystem paths
- os.path — Common pathname manipulations
- fileinput — Iterate over lines from multiple input streams
- stat — Interpreting stat() results
- filecmp — File and Directory Comparisons
- tempfile — Generate temporary files and directories
- glob — Unix style pathname pattern expansion
- fnmatch — Unix filename pattern matching
- linecache — Random access to text lines
- shutil — High-level file operations
- macpath — Mac OS 9 path manipulation functions
### data persistence
- pickle — Python object serialization
- copyreg — Register pickle support functions
- shelve — Python object persistence
- marshal — Internal Python object serialization
- dbm — Interfaces to Unix “databases”
- sqlite3 — DB-API 2.0 interface for SQLite databases
### data compression and archiving
- zlib — Compression compatible with gzip
- gzip — Support for gzip files
- bz2 — Support for bzip2 compression
- lzma — Compression using the LZMA algorithm
- zipfile — Work with ZIP archives
- tarfile — Read and write tar archive files
### file formats
- csv — CSV File Reading and Writing
- configparser — Configuration file parser
- netrc — netrc file processing
- xdrlib — Encode and decode XDR data
- plistlib — Generate and parse Mac OS X .plist files
### cryptographic services
- hashlib — Secure hashes and message digests
- hmac — Keyed-Hashing for Message Authentication
- secrets — Generate secure random numbers for managing secrets
### generic operating system services
- os — Miscellaneous operating system interfaces
- io — Core tools for working with streams
- time — Time access and conversions
- argparse — Parser for command-line options, arguments and sub-commands
- getopt — C-style parser for command line options
- logging — Logging facility for Python
- logging.config — Logging configuration
- logging.handlers — Logging handlers
- getpass — Portable password input
- curses — Terminal handling for character-cell displays
- curses.textpad — Text input widget for curses programs
- curses.ascii — Utilities for ASCII characters
- curses.panel — A panel stack extension for curses
- platform — Access to underlying platform’s identifying data
- errno — Standard errno system symbols
- ctypes — A foreign function library for Python
### concurrent execution
- threading — Thread-based parallelism
- multiprocessing — Process-based parallelism
- The concurrent package
- concurrent.futures — Launching parallel tasks
- subprocess — Subprocess management
- sched — Event scheduler
- queue — A synchronized queue class
- dummy_threading — Drop-in replacement for the threading module
- _thread — Low-level threading API
- _dummy_thread — Drop-in replacement for the _thread module
### interprocess communication and networking
- socket — Low-level networking interface
- ssl — TLS/SSL wrapper for socket objects
- select — Waiting for I/O completion
- selectors — High-level I/O multiplexing
- asyncio — Asynchronous I/O, event loop, coroutines and tasks
- asyncore — Asynchronous socket handler
- asynchat — Asynchronous socket command/response handler
- signal — Set handlers for asynchronous events
- mmap — Memory-mapped file support
> stop reading word for word. 
> 
> find reading as needed. 
> 
> ———— moz 20181012
### internet data handling
### structured markup processing tools
### internet protocols and support
### multimedia services
### internationalization
### program frameworks
### graphical user interfaces with TK
### development tools
### debugging and profiling
### software packaging and distribution
### python runtime services
### custom python interpreters
### importing modules
### python language services
### miscellaneous services
### ms windows specific services
### unix specific services
### superseded modules
### undocumented modules

## The Python Language Reference

## Python Setup and Usage

## Python HOWTOs

## Installing Python Modules

## Distributing Python Modules

## extending and embedding

## python/c api

## FAQs

## NOTE
```
1. about decorator and special function like __init__
```

## WSGI ASGI HTTP SOCKET HOW TO USE
```
WSGI is the Web Server Gateway Interface(https://wsgi.readthedocs.io/en/latest)
ASGI (Asynchronous Server Gateway Interface) is a spiritual successor to WSGI, intended to provide a standard interface between async-capable Python web servers, frameworks, and applications.(https://asgi.readthedocs.io/en/latest/)
-  ★重构shadowsocks随时随地使用受保护的通道★study
1. 重构python版local，加入类似windows版的负载均衡(load balancing)、高可用(High availability)模式
2. 重构sock5代理端口1080，使之增加身份认证
3. 实现一个http、sock5代理服务器
4. 参考资料[免费ss账号](https://github.com/max2max/freess), [HTTP/HTTPs/Socks5 proxy](https://github.com/ring04h/wyproxy), 
5. [shadowsocks](https://github.com/shadowsocks/shadowsocks), [shadowsocks-windows](https://github.com/shadowsocks/shadowsocks-windows)
6. [gfwlist](https://github.com/gfwlist/gfwlist),[python proxy](https://github.com/qwj/python-proxy)
7. [ProxyBroker](https://github.com/constverum/ProxyBroker)
8. [mitmproxy](https://github.com/mitmproxy/mitmproxy)
```

# django/channels(https://channels.readthedocs.io/en/latest/introduction.html)
```
introduction: asynchronous through django synchronous core, not only deal with HTTP, but that long-running connections: websocket, MQTT, chatbots, and more.
turtles all the way down: 
scopes and events:
What is a Consumer?
Routing and Multiple Protocols
Cross-Process Communication
Django Integration

Tutorial.
Consumers. sync and async
Database Access.
Channel Layers. cross process communication
```