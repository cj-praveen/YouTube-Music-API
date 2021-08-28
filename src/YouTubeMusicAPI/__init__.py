__all__ = ["YouTubeMusicAPI"]
__author__ = "Sijey (cjpraveen@hotmail.com)"
__version__ = "2.1"
__copyright__ = "Copyright (c) 2021 Sijey"
__license__ = "MIT" # Use of this source code is governed by the MIT License, See LICENSE for more details. >>> https://github.com/sijey-praveen/YouTube-Music-API/blob/Sijey/LICENSE

from os import *
from requests import *
import platform
from bs4 import *

def YouTubeMusicAPI(query : str, type : str):

    """

    YouTubeMusicAPI Library
    ~~~~~~~~~~~~~~~~~~~~~

    An unofficial YouTube Music API For Python Programming Language. Written in Python, for human beings.
    
    >>> https://github.com/sijey-praveen/YouTube-Music-API 

    """

    base_url = f"https://www.youtube.com/results?q={query}"

    if type == "track" : snippet, _type = "watch", "WEB_PAGE_TYPE_WATCH"
    elif type == "artist" : snippet, _type = "channel", "WEB_PAGE_TYPE_CHANNEL"
    elif type == "playlist" : snippet, _type, base_url = "watch", "WEB_PAGE_TYPE_WATCH", base_url + "&sp=EgIQAw%253D%253D"
    else : print("Invalid Search Type, ['artist', 'playlist', 'track'] are available."), exit()

    count, results = 0, str(get(base_url).content).split('"')
    for i in results:
        count += 1
        if i == _type : break
    if snippet in results[count - 5] : id = results[count - 5]
    else: print(f"No result found."), exit()

    if type == "track":

        __src__ = BeautifulSoup(get(f"https://www.youtube.com/{id}").text, 'html.parser')
        track_Id = __src__.find("meta", attrs={"itemprop" : "videoId"}).get("content")
        return dict(
        track_name = __src__.find("meta", attrs={"name" : "title"}).get("content"), 
        datePublished = __src__.find("meta", attrs={"itemprop" : "datePublished"}).get("content"),
        track_Id = track_Id,
        track_url = f"https://music.youtube.com/watch?v={track_Id}",
        track_image = f"https://i.ytimg.com/vi/{track_Id}/hqdefault.jpg", 
        )

    if type == "artist":

        return dict(
        artist = BeautifulSoup(get(f"https://www.youtube.com{id}").text, 'html.parser').find("meta", attrs={"property" : "og:title"}).get("content"),
        artist_url = f"https://music.youtube.com{id}",
        artist_id = id.split("/")[2],
        artist_image = BeautifulSoup(get(f"https://www.youtube.com{id}").text, 'html.parser').find("link", attrs={"itemprop" : "thumbnailUrl"}).get("href")
    )

    if type == "playlist":

        return dict(
            playlist_name = BeautifulSoup(get("https://music.youtube.com/playlist?list={}".format(id.split("list=")[1])).text, 'html.parser').find("meta", attrs={"property" : "og:title"}).get("content"),
            playlist_url = "https://music.youtube.com/playlist?list={}".format(id.split("list=")[1]),
            playlist_id = id.split("list=")[1]
        )

if __name__ == "__main__":
    if 200 == head("https://pypi.org/project/YouTubeMusicAPI/2.2/").status_code:
        if "windows" == platform.system().lower() : system("pip install YouTubeMusicAPI==2.2")
        else : system("pip3 install YouTubeMusicAPI==2.2")
