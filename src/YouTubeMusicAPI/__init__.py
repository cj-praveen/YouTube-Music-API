__all__ = ["YouTubeMusicAPI"]
__author__ = "Sijey (cjpraveen@hotmail.com)"
__version__ = "2.2"
__copyright__ = "Copyright (c) 2021 Sijey"
__license__ = "MIT" # >>> https://mit-license.org/

from requests import *
from bs4 import *

class YouTubeMusicAPI():

    def __init__(self, query : str) -> None:
        """

        YouTubeMusicAPI Library
        ~~~~~~~~~~~~~~~~~~~~~

        An unofficial YouTube Music API For Python Programming Language. Written in Python, for human beings.
        
        >>> https://github.com/sijey-praveen/YouTube-Music-API 

        """

        self.base_url = f"https://www.youtube.com/results?q={query}"

    def track(self):
        count, results = 0, str(get(self.base_url).content).split('"')
        for i in results:
            count += 1
            if i == "WEB_PAGE_TYPE_WATCH" : break
        if "watch" in results[count - 5] : id = results[count - 5]
        else: print(f"No result found."), exit()

        __src__ = BeautifulSoup(get(f"https://www.youtube.com/{id}").text, 'html.parser')
        track_Id = __src__.find("meta", attrs={"itemprop" : "videoId"}).get("content")
        return dict(
        track_name = __src__.find("meta", attrs={"name" : "title"}).get("content"), 
        datePublished = __src__.find("meta", attrs={"itemprop" : "datePublished"}).get("content"),
        track_Id = track_Id,
        track_url = f"https://music.youtube.com/watch?v={track_Id}",
        track_image = f"https://i.ytimg.com/vi/{track_Id}/hqdefault.jpg", 
        )

    def artist(self):        
        count, results = 0, str(get(self.base_url).content).split('"')
        for i in results:
            count += 1
            if i == "WEB_PAGE_TYPE_CHANNEL" : break
        if "artist" in results[count - 5] or "/c/" in results[count - 5] : id = results[count - 5]
        else: print(f"No result found."), exit()


        return dict(
        artist = BeautifulSoup(get(f"https://www.youtube.com{id}").text, 'html.parser').find("meta", attrs={"property" : "og:title"}).get("content"),
        artist_url = f"https://music.youtube.com{id}",
        artist_id = id.split("/")[2],
        artist_image = BeautifulSoup(get(f"https://www.youtube.com{id}").text, 'html.parser').find("link", attrs={"itemprop" : "thumbnailUrl"}).get("href")
        )


    def playlist(self):
        count, results = 0, str(get(f"{self.base_url}&sp=EgIQAw%253D%253D").content).split('"')
        for i in results:
            count += 1
            if i == "WEB_PAGE_TYPE_WATCH" : break
        if "watch" in results[count - 5] : id = results[count - 5]
        else: print(f"No result found."), exit()

        return dict(
            playlist_name = BeautifulSoup(get("https://music.youtube.com/playlist?list={}".format(id.split("list=")[1])).text, 'html.parser').find("meta", attrs={"property" : "og:title"}).get("content"),
            playlist_url = "https://music.youtube.com/playlist?list={}".format(id.split("list=")[1]),
            playlist_id = id.split("list=")[1]
        )
