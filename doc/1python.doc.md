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
### built-in constants
### built-in types
### built-in exceptions
### text processing services
### binary data services
### data types
### numeric and mathematical modules
### functional programming modules
### file and directory access
### data persistence
### data compression and archiving
### file formats
### cryptographic services
### generic operating system services
### concurrent execution
### interprocess communication and networking
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

## WSGI ASGI
```
WSGI is the Web Server Gateway Interface(https://wsgi.readthedocs.io/en/latest)
ASGI (Asynchronous Server Gateway Interface) is a spiritual successor to WSGI, intended to provide a standard interface between async-capable Python web servers, frameworks, and applications.(https://asgi.readthedocs.io/en/latest/)
```