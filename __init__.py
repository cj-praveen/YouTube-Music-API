"""
MIT License

Copyright (c) 2021 Sijey

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import os
import pafy
import socket
import webbrowser
from youtube_search import YoutubeSearch

def Search(song_name):
    query = YoutubeSearch(song_name, max_results=1).to_dict()
    Data = query[0]
    Music_ID = Data['url_suffix']
    URL = f"https://music.youtube.com{Music_ID}"
    return URL

Host = socket.gethostname()
IP = socket.gethostbyname(Host)

if "127.0.0.1" in IP:
    print("You're Offline, Please Connect to Internet!")
    exit()
else:
    pass

def download(song_name, path):
    if "Topic" in song_name.lower():
        pass
    else:
        song_name = song_name + " Album Topic"
    print("Connecting To Youtube Music...")
    dl_config = pafy.new(Search(song_name))
    print("\nCollecting Data From Youtube Music...")
    dl = dl_config.getbestaudio()
    dl.download(path)
    print("Download Completed!")

def play(song_name):
    if "Topic" in song_name.lower():
        pass
    else:
        song_name = song_name + " Album Topic"
    print("Connecting To Youtube Music...")
    Music_URL = Search(song_name)
    webbrowser.open(Music_URL)
    return Music_URL

def playonvlc(song_name):
    if "Topic" in song_name.lower():
        pass
    else:
        song_name = song_name + " Album Topic"
    print("Connecting To Youtube Music...")
    Music_URL = Search(song_name)
    os.system("start vlc " + Music_URL)
