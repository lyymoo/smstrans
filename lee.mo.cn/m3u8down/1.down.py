import requests
from tomorrow import threads
import gc
import os
import sys
import re
#将浏览器上的headers直接复制到HEADERS中
Headers = {header.split(':', 1)[0].strip(): header.split(':', 1)[1].strip() for header in """HEADERS""".split('\n') if header}

@threads(20)
def download(url,name, path):
    try:
        content = requests.get(url,headers=Headers, stream=True, timeout=3).content
        with open(os.path.join(path, name), 'wb') as f:
            f.write(content)
        del content
        gc.collect()
    except:
        print(name)
        pass
#存放视频片段的地址
path = r'to\video'
if not os.path.exists(path):
    os.mkdir(path)

if __name__ == '__main__':
    video = sys.argv[1]
    with open(video, 'r') as f:
        urls = [url.strip() for url in f.readlines() if 'https' in url]
        url = re.sub('-\d+?-','-{}-',urls[0])
        names = {str(index) + '.ts' for index in range(1, len(urls) + 1)}
    responses = [download(url.format(name.split('.')[0]),name, path) for name in names-set(os.listdir(path))]
