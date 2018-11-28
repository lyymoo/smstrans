import asyncio
import aiohttp
import time
import os
import shutil
import sys


class M3U8Downloader(object):
    def __init__(self, loop, save_name):
        self.session = aiohttp.ClientSession()
        self.videos = None
        self.proxies = (None, None)
        self.loop = loop

        # 暂时保存ts文件的路径, 视频下载完合并后删除.
        self.ts_path = os.getcwd() + '/ts_' + time.strftime('%H_%M_%S', time.localtime())
        # 视频合成后的保存路径,不会删除
        self.save_path = os.getcwd() + '/video/'
        self.check_path()
        # 默认视频名称 时_分_秒.mp4
        self.save_name = save_name + ".mp4" or time.strftime('%H_%M_%S', time.localtime()) + '.mp4'

    def check_path(self):
        # 检查路径是否存在,不存在则生成.
        if os.path.exists(self.ts_path) is False:
            os.mkdir(self.ts_path)
        if os.path.exists(self.save_path) is False:
            os.mkdir(self.save_path)

    def main(self, url_list):
        print("开始下载,一共{}个文件。".format(len(url_list)))
        videos = ((name, url) for name, url in enumerate(url_list))

        if videos:
            self.videos = videos
            self.prepare_download()
        else:
            print('url_list can not be null')

        self.session.close()
        self.ts_merge()
        self.ts_delete()

    def prepare_download(self):
        try:
            tasks = asyncio.gather(*[self.download() for _ in range(8)])
            self.loop.run_until_complete(tasks)
        except Exception as e:
            print(e)
            print('出错')

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
        os.system(command)
        time.sleep(2)

    def ts_delete(self):
        shutil.rmtree(self.ts_path)
