"""
MIT License

Copyright (c) 2021 Sijey

Read more : https://raw.githubusercontent.com/sijey-praveen/YouTube-Music-API/Sijey/LICENSE

"""

try:
    import os
    import socket
    import webbrowser
    import requests
    import platform
    from youtube_search import YoutubeSearch
except Exception as Error:
    if "No module named 'youtube_search'" in f"{Error}":
        if "windows" == platform.system().lower():
            os.system("pip install youtube-search")
        elif "darwin" == platform.system().lower():
            os.system("pip3 install youtube-search")
        elif "linux" == platform.system().lower():
            os.system("pip3 install youtube-search")

def NoInternetConnectionError():
    Host = socket.gethostname()
    IP = socket.gethostbyname(Host)
    if "127.0.0.1" in IP:
        print("You're Offline, Please Connect to Internet!")
        exit()

def AutoUpdate():
    if 200 == requests.head("https://pypi.org/project/YouTubeMusicAPI/1.8/").status_code:
        if "Windows" == platform.system():
            os.system("pip install YouTubeMusicAPI==1.8")
        elif "Darwin" == platform.system():
            os.system("pip install YouTubeMusicAPI==1.8")
        elif "Linux" == platform.system():
            os.system("pip install YouTubeMusicAPI==1.8")
        
def __main__(song_name):
    Domain = "https://www.youtube.com/"
    Sub_Domain = "https://music.youtube.com/"
    try:
        query = YoutubeSearch(song_name, max_results=1).to_dict()
        Data = query[0]
        Music_ID = Data['id']
        URL = f"{Sub_Domain}watch?v={Music_ID}"
        return URL
    except Exception:
        count = 0
        results = str(requests.get(f"https://www.youtube.com/results?q={song_name}").content).split('"')
        for i in results:
            count += 1
            if i == 'WEB_PAGE_TYPE_WATCH':
                break
        if results[count - 5] == "/results":
             raise Exception("No video found.")
        URL = f"{Sub_Domain}{results[count - 5]}"
        return URL

def play(song_name):
    song_name = f"{song_name} Album Topic"
    Music_URL = __main__(song_name)
    webbrowser.open(Music_URL)

def playonvlc(song_name):
    song_name = f"{song_name} Album Topic"
    Music_URL = __main__(song_name)
    os.system("start vlc " + Music_URL)

def getsonginfo(song_name):
    song_name = f"{song_name} Album Topic"
    query = YoutubeSearch(song_name, max_results=1).to_dict()[0]
    Data = {"Name" : f"{query['title']}", "ID" : f"{query['id']}", "Total Listeners" : f"{str(query['views'].replace(' views', ''))}", "Duration" : f"{query['duration']}", "Artist" : f"{query['channel']}", "URL" : f"https://music.youtube.com/watch?v={query['id']}"}
    return Data

NoInternetConnectionError()
AutoUpdate()
