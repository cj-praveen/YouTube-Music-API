__all__ = ["YouTubeMusicAPI"]
__author__ = "Sijey (cjpraveen@hotmail.com)"
__version__ = "2.4"
__copyright__ = "Copyright (c) 2021 Sijey"
__license__ = "MIT" # >>> https://mit-license.org/

from requests import get
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
        if id == None : return dict(message = "No Track Found!")
        else : id = id.group().split(":")[1].replace('"', "")
        meta = get(f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={id}", headers=self.user_agent).json()
        return dict(
            name = meta["title"],
            Id = id,
            url = f"https://music.youtube.com/watch?v={id}",
            image = f"https://i.ytimg.com/vi/{id}/hqdefault.jpg",
            author_name = meta["author_name"],
            author_url = meta["author_url"]
        )

    def playlist(self, query : str):
        id = search('"playlistId":".{34}"', get(f"https://www.youtube.com/results?search_query={query}&sp=EgIQAw%253D%253D", headers=self.user_agent).content.decode("utf-8"))
        if id == None : return dict(message = "No Playlist Found!")
        else : id = id.group().split(":")[1].replace('"', "")
        meta = get(f"https://www.youtube.com/oembed?url=https://www.youtube.com/playlist?list={id}", headers=self.user_agent).json()
        return dict(
            name = meta["title"],
            url = f"https://music.youtube.com/playlist?list={id}",
            Id = id,
            author_name = meta["author_name"],
            author_url = f"https://www.youtube.com{meta['author_url']}"
        )

    def searchUrls(self, query : str):
        ids, result = [], findall('"videoId":".{11}"', get(f"https://music.youtube.com/search?q={query}", headers=self.user_agent).content.decode("unicode_escape"))
        if result == None : return dict(message = "No URLs Found!")
        for i in result : ids.append("https://music.youtube.com/watch?v={}".format(i.split(":")[1].replace('"', "")))
        return list(set(ids))

print(YouTubeMusicAPI().playlist("Alan Walker"))