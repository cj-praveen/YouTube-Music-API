import requests
import os
import pafy
import socket
import webbrowser

Host = socket.gethostname()
IP = socket.gethostbyname(Host)

if "127.0.0.1" in IP:
    print("Your Are Offline, Please Connect to Internet!")
    exit()
else:
    pass

def download(song_name, path):
    if "Topic" in song_name.lower():
        pass
    else:
        song_name = song_name + "Album Topic"
    PyWhatKitAPI = "https://pywhatkit.herokuapp.com/playonyt?topic=" + song_name
    print("Connecting To Youtube Music...")
    GET_content = requests.get(PyWhatKitAPI)
    Music_URL = GET_content.text.replace("www.", "music.")
    dl_config = pafy.new(GET_content.text)
    print("\nCollecting Data From Youtube Music...")
    dl = dl_config.getbestaudio()
    dl.download(path)
    print("Download Completed!")

def play(song_name):
    if "Topic" in song_name.lower():
        pass
    else:
        song_name = song_name + "Album Topic"
    PyWhatKitAPI = "https://pywhatkit.herokuapp.com/playonyt?topic=" + song_name
    print("Connecting To Youtube Music...")
    GET_content = requests.get(PyWhatKitAPI)
    Music_URL = GET_content.text.replace("www.", "music.") + ("&list=RDAMVMd0eUMnJ5kTA")
    song = pafy.new(GET_content.text)
    print("\nNow Playing : " + song.title + " | Copyrights (c) " + song.author)
    webbrowser.open(Music_URL)

def getURL(song_name):
    if "Topic" in song_name.lower():
        pass
    else:
        song_name = song_name + "Album Topic"
    PyWhatKitAPI = "https://pywhatkit.herokuapp.com/playonyt?topic=" + song_name
    GET_content = requests.get(PyWhatKitAPI)
    Music_URL = GET_content.text.replace("www.", "music.")
    print(Music_URL)
    return Music_URL

def playonvlc(song_name):
    if "Topic" in song_name.lower():
        pass
    else:
        song_name = song_name + "Album Topic"
    print("Connecting To Youtube Music...")
    PyWhatKitAPI = "https://pywhatkit.herokuapp.com/playonyt?topic=" + song_name
    GET_content = requests.get(PyWhatKitAPI)
    Music_URL = GET_content.text
    song = pafy.new(GET_content.text)
    print("\nNow Playing : " + song.title + " | Copyrights (c) " + song.author)
    os.system("start vlc " + Music_URL)
