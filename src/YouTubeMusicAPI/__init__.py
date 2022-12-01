from urllib.request import Request, urlopen
from urllib.parse import quote
import re
from warnings import filterwarnings
from json import loads

filterwarnings("ignore", category=DeprecationWarning)

def Search(query: str):

    headers: dict = {
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36"
    }

    page_source: str = urlopen(Request(f"https://music.youtube.com/search?q={quote(query)}", headers=headers)).read().decode("unicode_escape")

    if trackId := re.search('"videoId":"(.*?)"', page_source):
        trackId = loads(f"{{{trackId.group()}}}")["videoId"]

        meta = loads(urlopen(Request(f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={trackId}", headers=headers)).read())

        return dict(
            trackName = meta["title"],
            trackId = trackId,
            trackUrl = f"https://music.youtube.com/watch?v={trackId}",
            artworkUrl = f"https://img.youtube.com/vi/{trackId}/0.jpg",
            artistName = meta["author_name"],
            artistUrl = meta["author_url"]
        )

    else:
        return None
