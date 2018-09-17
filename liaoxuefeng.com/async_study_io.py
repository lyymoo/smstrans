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
    sync = False

    urls = ["https://lee.mo.cn/bing/2018091708100116.jpg",
            "https://lee.mo.cn/bing/2018091608100191.jpg",
            "https://lee.mo.cn/bing/2018091508100230.jpg",
            "https://lee.mo.cn/bing/2018091408100218.jpg",
            "https://lee.mo.cn/bing/2018091308100296.jpg",
            "https://lee.mo.cn/bing/2018091208100224.jpg",
            ]
    if sync:
        # a sync process
        for url in urls:
            filename = os.path.basename(url)
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