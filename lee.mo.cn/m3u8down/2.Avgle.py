import time
from wxpy import *
from selenium import webdriver


class M3U8Spider(object):
    def __init__(self):
        self.driver = None
        self.busy = False
        self.count = 0

    def log_in(self):
        bot = Bot(cache_path=True, console_qr=2)

        @bot.register()
        def process_msg(msg):
            # 打印消息

            if "avgle.com" in msg.text:
                if self.busy:
                    return "服务器正忙，请等待几秒后再使用"

                else:
                    self.busy = True
                    sender = msg.sender
                    url = msg.text
                    m3u8 = self.get_m3u8(url)
                    sender.send_msg(m3u8)
                    self.busy = False

    def get_m3u8(self, url):

        self.count += 1
        if self.count == 10:
            return "你的网址好像不正确，请检查"

        if self.driver is None:
            options = webdriver.ChromeOptions()
            options.add_argument('--proxy-server=socks5://127.0.0.1:1080')
            options.add_argument("--headless")
            options.add_argument("window-size=1024,768", )
            options.add_argument("--no-sandbox")
            print("正在打开该死的chrome")
            self.driver = webdriver.Chrome(executable_path="./chromedriver", chrome_options=options)
            print("打开成功")

        try:
            self.driver.get(url)
            time.sleep(5)
        except Exception as e:
            self.driver = None
            self.get_m3u8(url)
            print(e)

        script_to_execute = "var performance = window.performance || window.mozPerformance || window.msPerformance || window.webkitPerformance || {}; var network = performance.getEntries() || {}; return network;"
        network = self.driver.execute_script(script_to_execute)

        for item in network:
            m3u8 = item["name"]
            if ".m3u8" in m3u8:
                self.driver.get("about:blank")
                self.count = 0
                # print(m3u8)
                return m3u8

        self.get_m3u8(url)


if __name__ == '__main__':
    s = M3U8Spider()
    s.log_in()
    embed()
