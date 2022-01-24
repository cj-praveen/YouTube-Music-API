__all__ = ["YouTubeMusicAPI"]
__author__ = "Sijey (cjpraveen@hotmail.com)"
__version__ = "2.4"
__copyright__ = "Copyright (c) 2021 Sijey"
__license__ = "MIT" # >>> https://mit-license.org/

from requests import get
from bs4 import BeautifulSoup
from re import search, findall
from warnings import filterwarnings

class YouTubeMusicAPI():
    def __init__(self) -> None:
        """
        YouTubeMusicAPI Library
        ~~~~~~~~~~~~~~~~~~~~~
        An unofficial YouTube Music API For Python Programming Language. Written in Python, for human beings.
        >>> https://github.com/sijey-praveen/YouTube-Music-API 
        """
        filterwarnings("ignore", category=DeprecationWarning)
        self.user_agent = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.69"}
        
    def track(self, query : str):
        id = search('"videoId":".{11}"', get(f"https://music.youtube.com/search?q={query}", headers=self.user_agent).content.decode("unicode_escape"))
        if id == None : return "No Result Found!"
        else : id = id.group().split(":")[1].replace('"', "")
        __src__ = BeautifulSoup(get(f"https://www.youtube.com/watch?v={id}").text, 'html.parser')
        return dict(
            name = __src__.find("meta", attrs={"name" : "title"}).get("content"), 
            datePublished = __src__.find("meta", attrs={"itemprop" : "datePublished"}).get("content"),
            Id = id,
            url = f"https://music.youtube.com/watch?v={id}",
            image = f"https://i.ytimg.com/vi/{id}/hqdefault.jpg", 
        )

    def playlist(self, query : str):
        id = search('"playlistId":".{34}"', get(f"https://www.youtube.com/results?search_query={query}&sp=EgIQAw%253D%253D", headers=self.user_agent).content.decode("utf-8"))
        if id == None : return "No Result Found!"
        else : id = id.group().split(":")[1].replace('"', "")
        return dict(
            name = BeautifulSoup(get(f"https://music.youtube.com/playlist?list={id}").text, 'html.parser').find("meta", attrs={"property" : "og:title"}).get("content"),
            url = f"https://music.youtube.com/playlist?list={id}",
            Id = id
        )

    def searchUrls(self, query : str):
        ids, result = [], findall('"videoId":".{11}"', get(f"https://music.youtube.com/search?q={query}", headers=self.user_agent).content.decode("unicode_escape"))
        if result == None : return "No Result Found!"
        for i in result : ids.append("https://music.youtube.com/watch?v={}".format(i.split(":")[1].replace('"', "")))
        return list(set(ids))

