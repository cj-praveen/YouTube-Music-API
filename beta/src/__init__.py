__all__ = ["YouTubeMusicAPI"]
__author__ = "Sijey (cjpraveen@hotmail.com)"
__version__ = "beta"
__copyright__ = "Copyright (c) 2021 Sijey"
__license__ = "MIT" # >>> https://mit-license.org/

from requests import get
from bs4 import BeautifulSoup
from warnings import filterwarnings

class YouTubeMusicAPI():

    def __init__(self) -> None:
        """

        YouTubeMusicAPI Library
        ~~~~~~~~~~~~~~~~~~~~~

        An unofficial YouTube Music API For Python Programming Language. Written in Python, for human beings.
        
        >>> https://github.com/sijey-praveen/YouTube-Music-API 

        """

        self.user_agent = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0"}

        filterwarnings("ignore", category=DeprecationWarning)

    def get_track(self, query : str):
        query = query.replace(" ", "+")
        re = get(f"https://music.youtube.com/search?q={query}", headers=self.user_agent).content.decode("unicode_escape").split('"')
        count = 0

        for i in re:
            count += 1
            if "contentPosition" == i : break

        try: 
            count = count + 29
            id = re[count]
        except IndexError : print(f"No result found."), exit()

        data = BeautifulSoup(get(f"https://www.youtube.com/watch?v={id}").text, 'html.parser')

        return dict(
            track_name = data.find("meta", attrs={"name" : "title"}).get("content"), 
            datePublished = data.find("meta", attrs={"itemprop" : "datePublished"}).get("content"),
            track_Id = id,
            track_url = f"https://music.youtube.com/watch?v={id}",
            track_image = f"https://i.ytimg.com/vi/{id}/hqdefault.jpg", 
        )

# t = YouTubeMusicAPI().get_track("")
# print(t)
