import os
import requests
from bs4 import BeautifulSoup
from tornado import ioloop, httpclient

directory = "Episodes/"
path = ""

#program settings
silent = True

#anime settings
ep_start = str(0)
ep_end = str(5001)
#anime_id = str(1502) #1502 watch this one
default_ep = str(1)
quality_preferred = str(360) #1080p,720p,480p,360p
quality_preferred_type = "lowest" #highest,lowest,average

start_anime_id = 0
end_anime_id = 10000

#async settings
i = 0
threads = 100
headers={"Origin": "https://vidstreaming.io", "Referer": "https://vidstreaming.io"}

def init():
    global directory
    try:
        os.stat(directory)
    except:
        os.mkdir(directory)

def anime_folder(title,episode_title):
    try:
        os.stat(title)
    except:
        os.mkdir(title)
    try:
        os.stat(title+"/"+episode_title)
    except:
        os.mkdir(title+"/"+episode_title)

def get_video_src(url):
    req = requests.get(url)
    page = req.text
    soup = BeautifulSoup(page, "lxml")
    anime_name = soup.find("div", attrs={"class": "title_name"}).find("h2").text.strip()
    anime_series_name = soup.find("div", attrs={"class": "anime-info"}).find("a").text.strip()
    print("Episode Name:",anime_name)
    if not silent:
        print("Anime Name:",anime_series_name)
    #video_src = "https://"+soup.find("div", attrs={"class": "play-video"}).find("iframe").get("src")[2:]
    video_src = soup.find("li", attrs={"class": "vidcdn"}).find("a").get("data-video")
    return video_src,anime_name,anime_series_name

def get_m3u8_initiator_src(video_src):
    req = requests.get(video_src)
    page = req.text
    soup = BeautifulSoup(page, "lxml")
    js = soup.findAll("script")[3].text #sometimes [4].text
    m3u8_src = "http://"+js.split("file: '")[1].split("'")[0][8:] #isolate the https link in the js and convert it to http
    return m3u8_src

def get_m3u8_playlist_src(m3u8_src,headers):
    global quality_preferred,quality_preferred_type
    req = requests.get(m3u8_src, headers=headers)
    m3u8_stream = req.text
    m3u8_stream_array = m3u8_stream.split("\n")
    m3u8_stream_options = []
    for line in m3u8_stream_array:
        try:
            if line[0] != "#":
                m3u8_stream_options.append(line)
        except:
            pass
    if not silent:
        print("Options:",m3u8_stream_options)
    try:
        flag = False
        for quality in m3u8_stream_options:
            #print(quality)
            if quality_preferred in quality:
                m3u8_quality_playlist = quality
                flag = True
        quality_ordered = []
        quality_list = ["360","480","720","1080"]
        for theorectical_quality in quality_list:
            for quality in m3u8_stream_options:
                if theorectical_quality in quality:
                    quality_ordered.append(quality)
        if flag == False:
            if quality_preferred_type == "highest":
                m3u8_quality_playlist = quality_ordered[-1:][0]
            elif quality_preferred_type == "average":
                index_num = round(len(quality_ordered)/2)-1
                if (index_num < 0) or (index_num > len(quality_ordered)-1):
                    index_num = 0
                m3u8_quality_playlist = quality_ordered[index_num]
            else: #lowest or something else
                m3u8_quality_playlist = quality_ordered[0]
        quality_chosen = m3u8_quality_playlist.split(".")[2]
        print("Selected Quality:",str(quality_chosen)+"p")
    except:
        m3u8_quality_playlist = m3u8_stream_options[0] #maybe need another [0]
    url_domain = "/".join(m3u8_src.split("/")[:-1])+"/"
    m3u8_stream_src = url_domain + m3u8_quality_playlist
    return m3u8_stream_src,url_domain,m3u8_quality_playlist,m3u8_stream

def get_m3u8_playlist_links(m3u8_stream_src,headers):
    req = requests.get(m3u8_stream_src, headers=headers)
    m3u8_playlist = req.text
    m3u8_playlist_doc = req.text.split("\n")
    m3u8_links = []
    for line in m3u8_playlist_doc:
        try:
            if line[0] != "#":
                m3u8_links.append(line)
        except:
            pass
    return m3u8_links,m3u8_playlist

def save_playlist_information(m3u8_src,directory,anime_name,m3u8_quality_playlist,m3u8_playlist,m3u8_stream,anime_series_name):
    global path
    m3u8_src_name = m3u8_src.split("/")[-1:][0]
    anime_folder(directory+anime_series_name,anime_name) #creates the anime folder
    path = directory+anime_series_name+"/"+anime_name+"/"
    if not silent:
        print("Path:",path)
    with open(path+"playlist.m3u8", "w", encoding="utf-8") as file:
        file.write(m3u8_playlist)
    return path

def download_ts_files(m3u8_links,url_domain,headers,path):
    global i,threads
    http_client = httpclient.AsyncHTTPClient(force_instance=True,defaults=dict(user_agent="Mozilla/5.0"),max_clients=threads)
    for sub_link in m3u8_links:
        url = url_domain+sub_link
        request = httpclient.HTTPRequest(url.strip(),headers=headers,method='GET',connect_timeout=10000,request_timeout=10000)
        http_client.fetch(request,handle_ts_file_response)
        i += 1
    ioloop.IOLoop.instance().start()

def handle_ts_file_response(response):
    global i,path,headers
    if response.code == 599:
        print(response.effective_url,"error")
        http_client.fetch(response.effective_url.strip(),headers=headers,method='GET',connect_timeout=10000,request_timeout=10000)
    else:
        global i,path
        try:
            file_name = str(response.effective_url.split("/")[-1:][0])
            m3u8_video_file_part = response.body #use binary
            with open(path+file_name, "wb") as file: #save the file as a binary
                file.write(m3u8_video_file_part)
            if not silent:
                print("Downloaded:",file_name)
            #print("alive",response.effective_url)
        except Exception as e:
            print("dead",response.effective_url,e)
            http_client.fetch(response.effective_url.strip(),headers=headers,method='GET',connect_timeout=10000,request_timeout=10000)
        i -= 1
        if i == 0: #all pages loaded
            ioloop.IOLoop.instance().stop()
            print("Download Complete")

def download_episode(url,directory="Episodes/",headers={"Origin": "https://vidstreaming.io", "Referer": "https://vidstreaming.io"}):
    try:
        video_src,anime_name,anime_series_name = get_video_src(url)
        if not silent:
            print("Embed Src",video_src)#,anime_name)

        m3u8_src = get_m3u8_initiator_src(video_src)
        if not silent:
            print("M3U8 Src",m3u8_src)

        m3u8_stream_src,url_domain,m3u8_quality_playlist,m3u8_stream = get_m3u8_playlist_src(m3u8_src,headers)
        if not silent:
            print("Playlist:",m3u8_stream_src)#,url_domain)

        m3u8_links,m3u8_playlist = get_m3u8_playlist_links(m3u8_stream_src,headers)
        if not silent:
            print("Parts:",len(m3u8_links))
        
        if not silent:
            print("Saving Playlist Files..")
        path = save_playlist_information(m3u8_src,directory,anime_name,m3u8_quality_playlist,m3u8_playlist,m3u8_stream,anime_series_name)

        print("Downloading Episode Files..")
        download_ts_files(m3u8_links,url_domain,headers,path)
        
        print("Finished Episode")
        
    except Exception as e:
        print(e)
        download_episode(url)

def download_anime(ep_start,ep_end,anime_id,default_ep):
    url = "https://www04.gogoanimes.tv/load-list-episode?ep_start="+ep_start+"&ep_end="+ep_end+"&id="+anime_id+"&default_ep="+default_ep

    req = requests.get(url)
    page = req.text
    soup = BeautifulSoup(page, "lxml")
    episodes = ["https://www04.gogoanimes.tv"+tag.get("href").strip() for tag in soup.findAll("a")][::-1] #reverses episode order
    if not silent:
        print("API Episodes:",url)
    if len(episodes) != 0:
        print("Anime ID:",anime_id)
        print("Episodes:",len(episodes))

        for episode in episodes:
            if not silent:
                print("Episode Link:",episode)
            download_episode(episode)
    else:
        print("No Anime with ID:",anime_id)

init()
for anime_id in range(start_anime_id,end_anime_id):
    try:
        download_anime(ep_start,ep_end,str(anime_id),default_ep)
    except Exception as e:
        print("No Anime(?)",e)
