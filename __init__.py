import os
import socket
import webbrowser
from youtube_search import YoutubeSearch

def __main__(song_name):
    query = YoutubeSearch(song_name, max_results=1).to_dict()
    Data = query[0]
    Music_ID = Data['id']
    URL = f"https://music.youtube.com/watch?v={Music_ID}"
    return URL

def NoInternetConnectionError():
    Host = socket.gethostname()
    IP = socket.gethostbyname(Host)
    if "127.0.0.1" in IP:
        print("You're Offline, Please Connect to Internet!")
        exit()
    else:
        pass

def play(song_name):
    song_name = f"{song_name} Album Topic"
    Music_URL = __main__(song_name)
    webbrowser.open(Music_URL)

def playonvlc(song_name):
    song_name = f"{song_name} Album Topic"
    Music_URL = __main__(song_name)
    os.system("start vlc " + Music_URL)

NoInternetConnectionError()
