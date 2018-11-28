from lxml import etree
import requests
import re
from M3U8_Downloader import M3U8Downloader
import asyncio
import time
import sys


def get_video_url(web_site_url):
    resp = requests.get(web_site_url)
    html = etree.HTML(resp.content.decode("utf-8"))
    url = html.xpath("//meta[@property='og:image']/@content")[0]
    base_url = url.split(url.split("/")[-1])[0]
    print(base_url)

    m3u8_str = "hls/hls.m3u8"
    resp = requests.get(base_url + m3u8_str)
    content = resp.content.decode("utf8")
    resolution = re.findall("hls-.*?.m3u8", content)[0]
    print("分辨率" + resolution)

    m3u8_url = base_url + "hls/" + resolution
    resp = requests.get(m3u8_url)
    content = resp.content.decode("utf8")
    ts_list = re.findall("hls-.*?.ts", content)
    return [base_url + "hls/" + ts for ts in ts_list]


if __name__ == '__main__':
    web_site_url = sys.argv[1]
    file_name = sys.argv[2]

    loop = asyncio.get_event_loop()
    download_list = get_video_url(web_site_url)
    print("下载列表")
    print(download_list)

    downloader = M3U8Downloader(loop, file_name)
    downloader.main(download_list)

