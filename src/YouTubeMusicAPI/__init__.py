"""
YouTubeMusicAPI Library
~~~~~~~~~~~~~~~~~~~~~

An unofficial YouTube Music API For Python Programming Language. Written in Python, for human beings.
"""

__all__ = ["get_track"]

__author__ = "Sijey (cjpraveen@hotmail.com)"
__version__ = ""
__copyright__ = "Copyright (c) 2021 Sijey"
__license__ = "MIT" # Use of this source code is governed by the MIT License license, See LICENSE for more details.

from os import *
from requests import *
import platform
from bs4 import *

class YouTubeMusicAPI():
    def __init__(self, song_name : str):
        self.song_name = song_name

        """
        Get's the MusicId or VideoId or TrackId from youtube using 'Request' library.
        """
        count = 0
        results = str(get(f"https://www.youtube.com/results?q={self.song_name} Album Topic").content).split('"')

        for i in results:
            count += 1
            if i == 'WEB_PAGE_TYPE_WATCH' : break
        if "watch" in results[count - 5] : self.music_id = results[count - 5]
        else: print("No Song found."), exit()

        """
        Gather's All Metadata about the music or song or track using web scraping libraries ('BeautifulSoup' & 'Requests' library used here for this process.).

        """

        __src__ = BeautifulSoup(get(f"https://www.youtube.com/{self.music_id}").text, 'html.parser')
        self.track_name = __src__.find("meta", attrs={"name" : "title"}).get("content")
        self.datePublished = __src__.find("meta", attrs={"itemprop" : "datePublished"}).get("content")
        self.interactionCount = __src__.find("meta", attrs={"itemprop" : "interactionCount"}).get("content")
        self.artist_id = __src__.find("meta", attrs={"itemprop" : "channelId"}).get("content")
        self.track_Id = __src__.find("meta", attrs={"itemprop" : "videoId"}).get("content")
        self.artist_image = BeautifulSoup(get(f"https://www.youtube.com/channel/{self.artist_id}").text, 'html.parser').find("link", attrs={"itemprop" : "thumbnailUrl"}).get("href")
        for i in __src__.find_all("span")[0]:
            if i.get("itemprop") == "name" : self.artist = str(i.get("content"))

    def get_track(self):
        """
        >>> .get_track()

        Return metadata about the song or music or track in json format based on your search query.
        """
        return dict(
        track_name = self.track_name, 
        datePublished = self.datePublished,
        track_Id = self.track_Id,
        track_url = f"https://music.youtube.com/watch?v={self.track_Id}",
        track_image = f"https://i.ytimg.com/vi/{self.track_Id}/hqdefault.jpg", 
        interactionCount = self.interactionCount, 
        artist = self.artist, 
        artist_url = f"https://music.youtube.com/channel/{self.artist_id}",
        artist_id = self.artist_id, 
        artist_image = self.artist_image
    )

if __name__ == "__main__":

    # Check for new version update

    if 200 == head("https://pypi.org/project/YouTubeMusicAPI/2.1/").status_code:
        if "windows" == platform.system().lower() : system("pip install YouTubeMusicAPI==2.1")
        else : system("pip3 install YouTubeMusicAPI==2.1")
