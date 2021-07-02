"""
MIT License

Copyright (c) 2021 Sijey

Read more : https://raw.githubusercontent.com/sijey-praveen/YouTube-Music-API/Sijey/LICENSE

"""
try:
    from os import system
    from socket import gethostname, gethostbyname
    import webbrowser
    import requests
    import platform
    from youtube_dl import YoutubeDL
except Exception as Error:
    if "No module named 'youtube_dl'" in f"{Error}":
        if "windows" == platform.system().lower():
            system("pip install youtube-dl")
        elif "darwin" == platform.system().lower():
            system("pip3 install youtube-dl")
        elif "linux" == platform.system().lower():
            system("pip3 install youtube-dl")


def NoInternetConnectionError():
    if "127.0.0.1" == gethostbyname(gethostname()):
        print("You're Offline, Please Connect to Internet!")
        exit()

def check_for_update():
    if 200 == requests.head("https://pypi.org/project/YouTubeMusicAPI/2.0/").status_code:
        if "Windows" == platform.system():
            system("pip install YouTubeMusicAPI==2.0")
        elif "Darwin" == platform.system():
            system("pip install YouTubeMusicAPI==2.0")
        elif "Linux" == platform.system():
            system("pip install YouTubeMusicAPI==2.0")
        
def url(song_name):
    count = 0
    results = str(requests.get(f"https://www.youtube.com/results?q={song_name}").content).split('"')
    for i in results:
        count += 1
        if i == 'WEB_PAGE_TYPE_WATCH':
            break
    if results[count - 5] == "/results":
            raise Exception("No video found.")
    URL = f"{results[count - 5]}"
    return URL

def play(song_name):
    Music_URL = url(f"{song_name} Album Topic")
    webbrowser.open(f"https://music.youtube.com/{Music_URL}")

def playonvlc(song_name):
    Music_URL = url(f"{song_name} Album Topic")
    system(f"start vlc  https://www.youtube.com/{Music_URL}")

def getsonginfo(song_name):
    song_name = f"{song_name} Album Topic"
    data = YoutubeDL(
        {
            "restrictfilenames": True, 
            "noplaylist": True, 
            "nocheckcertificate": True,
            "ignoreerrors": True, 
            "logtostderr": False, 
            "quiet": True, 
            "no_warnings": True
        }
    ).extract_info(f"https://www.youtube.com/{url(song_name)}", download=False)
    return dict(song_name = data['title'], total_listeners = str(data['view_count']), duration = data['duration'], artist = data['uploader'], album_art = data['thumbnail'], artist_url = str(data['uploader_url']).replace("www.", "music."), track_url = f"https://music.youtube.com/watch?v={data['id']}", track_id = data['id'])

if __name__ == "__main__":
    NoInternetConnectionError()
    check_for_update()