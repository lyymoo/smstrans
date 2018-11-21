# -*- coding: utf-8 -*-


def use_urlopen():
    import socket
    from urllib import request
    print('socket timeout is:', socket.getdefaulttimeout())
    timeout = 2
    socket.setdefaulttimeout(timeout)
    print('socket timeout is:', socket.getdefaulttimeout())
    response = request.urlopen('https://www.twitter.com')
    print(response.read().decode('utf8')[0:100])


def use_request():
    from urllib import request
    req = request.Request('http://www.openbsd.org/images/')
    response = request.urlopen(req)
    print(response.read())


def post_data_by_get_method():
    from urllib import parse
    from urllib import request
    from urllib import error
    url = 'http://localhost/login.php'
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    values = {'act': 'login', 'login[email]': 'abc@abc.com', 'login[password]': '123456'}
    # generate a GET url parameter
    data = parse.urlencode(values)
    # add header 1
    # req = request.Request(url, data)
    # req.add_header('Referer', 'http://www.python.org/')
    # req.add_header('User-Agent', user_agent)
    # add header 2
    headers = {'User-Agent': user_agent, 'Referer': 'http://www.python.org/'}
    req = request.Request(url, data, headers)
    try:
        response = request.urlopen(req)  # error throw
    except error.HTTPError as e:
        print(e.code)
    except error.URLError as e:
        if hasattr(e, 'reason'):
            print('We failed to reach a server.')
            print('Reason: ', e.reason)
        elif hasattr(e, 'code'):
            print('The server couldn\'t fulfill the request.')
            print('Error code: ', e.code)
    else:
        pass
    the_page = response.read()
    print(the_page.decode("utf8"))


def post_data_by_post_method():
    from urllib import request
    data = '{"test": 1}'
    data = bytes(data, 'utf8')
    req = request.Request('http://www.baidu.com')
    response = request.urlopen(req, data)
    print(response.read())


def http_basic_auth():
    from urllib import request
    password_mgr = request.HTTPPasswordMgrWithDefaultRealm()
    top_level_url = "https://www.python.org/"
    password_mgr.add_password(None, top_level_url, 'rekfan', '1111')
    handler = request.HTTPBasicAuthHandler(password_mgr)
    opener = request.build_opener(handler)

    # way 1: use the opener to fetch a URL
    a_url = 'https://www.python.org/'
    x = opener.open(a_url)
    print(x.read())

    # way 2: install the opener.
    request.install_opener(opener)
    response = request.urlopen(a_url)
    print(response.read())


def use_proxy1():
    import re
    import os
    from urllib import request
    # case 1: un-authenticated proxy
    proxy_unauthenticated = request.ProxyHandler({'http': 'http://127.0.0.1:1080', 'https': 'http://127.0.0.1:1080'})
    opener1 = request.build_opener(proxy_unauthenticated)
    request.install_opener(opener1)
    image_rex = re.compile(r"<a href=\"(.+?)\.(png|jpg|gif)\">")

    if not os.path.exists('www.openbsd.org'):
        os.mkdir('www.openbsd.org')

    r1 = request.urlopen('http://www.openbsd.org/images/')
    for image in image_rex.findall(r1.read().decode('utf8')):
        r2 = request.urlopen('http://www.openbsd.org/images/%s.%s' % image)
        with open('www.openbsd.org/%s.%s' % image, 'wb') as f:
            f.write(r2.read())
        print('save: ', '%s.%s' % image)

    if not os.path.exists('www.openbsd.org/hackathons'):
        os.makedirs('www.openbsd.org/hackathons')

    r3 = request.urlopen('http://www.openbsd.org/images/hackathons/')
    for image in image_rex.findall(r3.read().decode('utf8')):
        r4 = request.urlopen('http://www.openbsd.org/images/hackathons/%s.%s' % image)
        with open('www.openbsd.org/hackathons/%s.%s' % image, 'wb') as f:
            f.write(r4.read())
        print('save: ', '%s.%s' % image)


def use_proxy2():
    from urllib import request
    # case 2: authenticated proxy 1 
    proxy_support = request.ProxyHandler(
        {"http": "http://username:password@127.0.0.1:1080", "https": "http://username:password@127.0.0.1:1080"})
    opener = request.build_opener(proxy_support)
    request.install_opener(opener)
    x = request.urlopen('https://www.twitter.com')
    print(x.read()[0:100])


def use_proxy3():
    from urllib import request
    # case 3: authenticated proxy 2
    password = request.HTTPPasswordMgrWithDefaultRealm()
    proxy_auth = request.ProxyBasicAuthHandler(password)
    password.add_password(realm=None, uri="http://127.0.0.1:1080", user='username', passwd='password')

    proxy_support = request.ProxyHandler(
        {"http": "http://127.0.0.1:1080", "https": "http://127.0.0.1:1080"})

    opener = request.build_opener(proxy_support, proxy_auth)
    # request.install_opener(opener)
    # r2 = request.urlopen('http://www.twitter.com')
    # or this blow:
    r2 = opener.open('https://www.twitter.com')
    print(r2.read(100))


def use_proxy4():
    import urllib.request
    # set up authentication info
    auth_info = urllib.request.HTTPBasicAuthHandler()
    auth_info.add_password(realm='PDQ Application',
                           uri='http://127.0.0.1:1080',
                           user='username',
                           passwd='password')

    proxy_support = urllib.request.ProxyHandler(
        {"http": "http://127.0.0.1:1080", "https": "http://127.0.0.1:1080"})

    # build a new opener that adds authentication and caching FTP handlers
    opener = urllib.request.build_opener(proxy_support, auth_info,
                                         urllib.request.CacheFTPHandler)

    # install it
    urllib.request.install_opener(opener)

    f = urllib.request.urlopen('https://www.twitter.com')
    print(f.read(100))


if __name__ == "__main__":
    use_proxy1()

# addition https://zhuanlan.zhihu.com/p/30670193
"""
# http
import requests

proxy = '127.0.0.1:9743' # proxy = 'username:password@127.0.0.1:9743'
proxies = {
    'http': 'http://' + proxy,
    'https': 'https://' + proxy,
}
try:
    response = requests.get('http://httpbin.org/get', proxies=proxies)
    print(response.text)
except requests.exceptions.ConnectionError as e:
    print('Error', e.args)

# socks5 pip3 install "requests[socks]"
# case 1
import requests

proxy = '127.0.0.1:9742'
proxies = {
    'http': 'socks5://' + proxy,
    'https': 'socks5://' + proxy
}
try:
    response = requests.get('http://httpbin.org/get', proxies=proxies)
    print(response.text)
except requests.exceptions.ConnectionError as e:
    print('Error', e.args)

# case 2
import requests
import socks
import socket

socks.set_default_proxy(socks.SOCKS5, '127.0.0.1', 9742)
socket.socket = socks.socksocket
try:
    response = requests.get('http://httpbin.org/get')
    print(response.text)
except requests.exceptions.ConnectionError as e:
    print('Error', e.args)

# Selenium
from selenium import webdriver

proxy = '127.0.0.1:9743'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=http://' + proxy)
browser = webdriver.Chrome(chrome_options=chrome_options)
browser.get('http://httpbin.org/get')

#####auth######
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import zipfile

ip = '127.0.0.1'
port = 9743
username = 'foo'
password = 'bar'

manifest_json = \"\"\"
{
    "version": "1.0.0",
    "manifest_version": 2,
    "name": "Chrome Proxy",
    "permissions": [
        "proxy",
        "tabs",
        "unlimitedStorage",
        "storage",
        "<all_urls>",
        "webRequest",
        "webRequestBlocking"
    ],
    "background": {
        "scripts": ["background.js"]
    }
}
\"\"\"

background_js = \"\"\"
var config = {
        mode: "fixed_servers",
        rules: {
          singleProxy: {
            scheme: "http",
            host: "%(ip)s",
            port: %(port)s
          }
        }
      }

chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

function callbackFn(details) {
    return {
        authCredentials: {
            username: "%(username)s",
            password: "%(password)s"
        }
    }
}

chrome.webRequest.onAuthRequired.addListener(
            callbackFn,
            {urls: ["<all_urls>"]},
            ['blocking']
)
\"\"\" % {'ip': ip, 'port': port, 'username': username, 'password': password}

plugin_file = 'proxy_auth_plugin.zip'
with zipfile.ZipFile(plugin_file, 'w') as zp:
    zp.writestr("manifest.json", manifest_json)
    zp.writestr("background.js", background_js)
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_extension(plugin_file)
browser = webdriver.Chrome(chrome_options=chrome_options)
browser.get('http://httpbin.org/get')
#####auth######

#对于 PhantomJS，代理设置方法可以借助于 service_args 参数，也就是命令行参数，代理设置方法如下
from selenium import webdriver

service_args = [
    '--proxy=127.0.0.1:9743',
    '--proxy-type=http'
]
browser = webdriver.PhantomJS(service_args=service_args)
browser.get('http://httpbin.org/get')
print(browser.page_source)

#如果需要认证，那么只需要再加入 --proxy-auth 选项即可，这样参数就改为：
service_args = [
    '--proxy=127.0.0.1:9743',
    '--proxy-type=http',
    '--proxy-auth=username:password'
]
"""
