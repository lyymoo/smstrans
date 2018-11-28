#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
from down import path
import os
import shutil

video = r'to\video.m3u8'
name = '人物名称'
seed = '作品名称'

with open(video, 'r') as f:
    urls = {url.strip() for url in f.readlines() if 'https' in url}
    names = {str(index) + '.ts' for index in range(1, len(urls) + 1)}
while names-set(os.listdir(path)):
    print('开始')
    p = subprocess.Popen(['python','down.py',video],shell=False)
    p.wait()
    print('结束')
if not os.path.exists(os.path.join(os.path.dirname(path),name)):
    os.mkdir(os.path.join(os.path.dirname(path),name))
if not os.path.exists(os.path.join(os.path.dirname(path),name,'{seed}.ts'.format(seed=seed))):
    with open(os.path.join(path,'mylist.txt'),'w') as f:
        f.writelines(map(lambda x :'file '+ str(x)+'.ts\n',range(1,len(names)+1)))
    cmd = r'ffmpeg -f concat -i mylist.txt -c copy ..\\{name}\\{seed}.ts'.format(name=name,seed=seed)
    p = subprocess.Popen(cmd,shell=True,cwd=path)
    p.wait()

shutil.rmtree(path)
# if not os.path.exists(os.path.join(os.path.dirname(path),'{name}.mp4'.format(name=re.search(r'\d+',video).group()))):
#     cmd = r'ffmpeg -i {name}.ts -vcodec h264 {name}.mp4'.format(name=re.search(r'\d+',video).group())
#     p = subprocess.Popen(cmd,shell=True,cwd=os.path.dirname(path))
#     p.wait()