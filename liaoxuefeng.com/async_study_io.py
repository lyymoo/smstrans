import asyncio
import os
import requests

import aiohttp
import async_timeout

async def download_coroutine(url):
    """
    a coroutine to download the specified url
    """
    request = requests.get(url)
    filename = os.path.basename(url)

    with open(filename, 'wb') as file_handle:
        chunk = request.content
        file_handle.write(chunk)
    msg = 'Finished downloading {filename}'.format(filename=filename)
    return msg

async def download_coroutine_better(session, url):
    """
    a better coroutine process
    """
    timeout = False
    if timeout:
        with async_timeout.timeout(100):
            async with session.get(url) as response:
                filename = os.path.basename(url)
                with open(filename, "wb") as f_handle:
                    while True:
                        chunk = await response.content.read(1024)
                        if not chunk:
                            break
                        f_handle.write(chunk)
                return await response.release()
    else:
        async with session.get(url) as response:
            filename = os.path.basename(url)
            with open(filename, "wb") as f_handle:
                while True:
                    chunk = await response.content.read(1024)
                    if not chunk:
                        break
                    f_handle.write(chunk)
            return await response.release()

async def main(urls):
    """
    Creates a group of coroutines and waits for them to finish
    """
    coroutines = [download_coroutine(url) for url in urls]

    completed, pending = await asyncio.wait(coroutines)
    for item in completed:
        print(item.result())

async def main_better(urls, loop):
    async with aiohttp.ClientSession(loop=loop) as session:
        tasks = [download_coroutine_better(session, url) for url in urls]
        await asyncio.gather(*tasks)

if __name__ == '__main__':
    # https://www.blog.pythonlibrary.org/2016/07/26/python-3-an-intro-to-asyncio/
    import time
    start = time.time()
    sync = True

    # urls = ["https://desk-fd.zol-img.com.cn/t_s960x600c5/g3/M04/0F/0C/Cg-4WFQk_u-IPdc-AAWOIOqKJKkAAPcawKSJFoABY44004.jpg",
    #         "http://pic1.sc.chinaz.com/files/pic/pic9/201809/hpic15.jpg",
    #         "http://www.cncd8.com/uploads/allimg/120308/1-12030R10P4.jpg",
    #         "http://www.tuxiwa.com/bbs/data/attachment/forum/201804/01/231046iww1njf3eereeere.jpg",
    #         "https://img.pc841.com/2018/0319/20180319090858589.jpg",
    #         "http://img1.mydrivers.com/img/20150505/898c7353bc8049a780c0ca11eca17e3e_1000.jpg",
    #         "http://www.wyx.cc/uploads/allimg/140728/1-140HP01616419.jpg",
    #         ]
    urls = [
        "http://meizitu.com",
        "http://www.meizitu.com/a/pure.html",
        "http://www.meizitu.com/a/cute.html",
        "http://www.meizitu.com/a/sexy.html",
        "http://www.meizitu.com/a/fuli.html",
        "http://www.meizitu.com/a/legs.html",
        "http://www.meizitu.com/a/rixi.html",
        "http://www.meizitu.com/a/qingchun.html",
        "http://www.meizitu.com/a/yundong.html",
        "http://www.meizitu.com/a/qingchun.html",
        "http://www.meizitu.com/a/sifang.html",
        "http://www.meizitu.com/tag/mote_6_1.html",
        "http://www.meizitu.com/tag/keai_64_1.html",
        "http://www.meizitu.com/a/bijini.html",
        "http://www.meizitu.com/tag/qizhi_53_1.html",
        "http://www.meizitu.com/tag/banluo_5_1.html",
        "http://www.meizitu.com/tag/nvshen_460_1.html",
        "http://www.meizitu.com/tag/quanluo_4_1.html",
        "http://www.meizitu.com/tag/meitun_42_1.html",
        "http://www.meizitu.com/tag/chengshu_487_1.html",
        "http://www.meizitu.com/a/xinggan.html",
        "http://www.meizitu.com/a/xinggan.html",
        "http://www.meizitu.com/a/sifang.html",
        "http://www.meizitu.com/a/sifang.html",
        "http://www.meizitu.com/a/qingchun.html",
        "http://www.meizitu.com/a/qingchun.html",
        "http://www.meizitu.com/a/qingchun.html",
        "http://www.meizitu.com/a/meizi.html",
        "http://www.meizitu.com/a/xiaoqingxin.htm",
        "http://www.meizitu.com/a/nvshen.html",
        "http://www.meizitu.com/a/qizhi.html",
        "http://www.meizitu.com/a/mote.html",
        "http://www.meizitu.com/a/mote.html",
        "http://www.meizitu.com/a/bijini.html",
        "http://www.meizitu.com/a/baobei.html",
        "http://www.meizitu.com/a/luoli.html",
        "http://www.meizitu.com/a/wangluo.html",
        "http://www.meizitu.com/a/rihan.html",
        "http://www.meizitu.com/a/oumei.html",
    ]
    if sync:
        # a sync process
        for url in urls:
            filename = os.path.join('meizitu', os.path.basename(url))
            with open(filename, 'wb') as file_handle:
                chunk = requests.get(url).content
                file_handle.write(chunk)
            msg = 'Finished downloading {filename}'.format(filename=filename)
            print(msg)
    else:
        flag = False
        if flag:
            # a bad process
            event_loop = asyncio.get_event_loop()
            try:
                event_loop.run_until_complete(main(urls))
            finally:
                event_loop.close()
        else:
            # a better process
            loop = asyncio.get_event_loop()
            try:
                loop.run_until_complete(main_better(urls, loop))
            finally:
                loop.close()


    elapsed = (time.time() - start)
    print("Time used:",elapsed)