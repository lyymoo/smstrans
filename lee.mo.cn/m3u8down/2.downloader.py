import asyncio
import aiohttp
import requests
import time
import os
import shutil
import sys
import re
from lxml import etree


class Spider(object):
    def __init__(self):
        self.session = aiohttp.ClientSession()
        self.videos = None
        self.proxies = (None, None)
        self.ts_path = os.getcwd() + '/ts_' + time.strftime('%H_%M_%S', time.localtime())  # 暂时保存ts文件的路径, 视频下载完合并后删除.
        self.save_path = os.getcwd() + '/video'  # 视频合成后的保存路径,不会删除
        self.check_path()
        self.save_name = time.strftime('/%H_%M_%S', time.localtime()) + '.mp4'  # 视频保存名 时_分_秒.mp4

    def check_path(self):
        # 检查路径是否存在,不存在则生成.
        if os.path.exists(self.ts_path) is False:
            os.mkdir(self.ts_path)
        if os.path.exists(self.save_path) is False:
            os.mkdir(self.save_path)

    async def download(self, video=None):
        while True:
            try:
                v = video or next(self.videos)
            except StopIteration:
                return

            name = v[0]
            url = v[1]
            proxy = self.proxies[name % 2]
            try:
                async with self.session.get(url, proxy=proxy, timeout=20) as r:
                    if r.status != 200:
                        print('下载失败')
                        sys.exit()

                    content = await r.read()
                    with open('{}/{}.ts'.format(self.ts_path, name), 'wb') as f:
                        f.write(content)
                print('download done {}'.format(name))
                video = None

            except Exception as e:
                print('出现异常{},重新下载'.format(e))
                await asyncio.sleep(5)
                await self.download(video)

    def prepare_download(self):
        try:
            tasks = asyncio.gather(*[self.download() for _ in range(8)])
            loop.run_until_complete(tasks)
        except Exception as e:
            print(e)
            print('出错')

    def main(self, m3u8):
        r = requests.get(m3u8)
        text = r.text.split('\n')
        url_list = (url.strip('\r') for url in text if 'http' in url)
        videos = ((name, url) for name, url in enumerate(url_list))

        if videos:
            self.videos = videos
            self.prepare_download()
        else:
            print('m3u8网址过期.....')

        self.session.close()
        self.ts_merge()
        self.ts_delete()

    def download_by_list(self, url_list):
        videos = ((name, url) for name, url in enumerate(url_list))

        if videos:
            self.videos = videos
            self.prepare_download()
        else:
            print('m3u8网址过期.....')

        self.session.close()
        self.ts_merge()
        self.ts_delete()

    def ts_merge(self):
        ts_names = os.listdir(self.ts_path)
        print(ts_names)
        if ts_names == '[]':
            return

        ts_names.sort(key=lambda x: int(x.split('.')[0]))
        merge_files = ""
        for name in ts_names:
            merge_files += name + '|'
        merge_files = merge_files.strip('|')  # 除去最后多出来的|

        command = 'cd {} && ffmpeg -i concat:"{}" -c copy {}'
        command = command.format(self.ts_path, merge_files, self.save_path + self.save_name)
        print(command)
        os.system(command)
        time.sleep(2)

    def ts_delete(self):
        shutil.rmtree(self.ts_path)

    def get_video_url(self, web_site_url):
        resp = requests.get(web_site_url)
        html = etree.HTML(resp.content.decode("utf-8"))
        url = html.xpath("//meta[@property='og:image']/@content")[0]
        base_url = url.split(url.split("/")[-1])[0]

        m3u8_str = "hls/hls.m3u8"
        resp = requests.get(base_url + m3u8_str)
        content = resp.content.decode("utf8")
        resolution = re.findall("hls-.*?.m3u8", content)[0]

        m3u8_url = base_url + "hls/" + resolution

        resp = requests.get(m3u8_url)
        content = resp.content.decode("utf8")
        ts_list = re.findall("hls-.*?.ts", content)

        download_list = [base_url + "hls/" + ts for ts in ts_list]
        print(len(download_list))
        return download_list


if __name__ == '__main__':
    start = time.time()
    s = Spider()
    loop = asyncio.get_event_loop()
    # m3u8 = 'https://ip49636214.ahcdn.com/key=Z0dka1KoPnfkeoYvJIn62A,s=,end=1521422678,limit=2/data=1521422678/state=Q9jY/reftag=56109644/media=hlsA/ssd4/177/5/84815855.m3u8'
    # s.main(m3u8)
    download_list = s.get_video_url("http://1.yase555.com/video-989065")
    s.download_by_list(download_list)
    end = time.time()
    print('done {}'.format(end - start))
