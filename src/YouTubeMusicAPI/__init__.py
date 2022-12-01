import urllib.request
import urllib.parse
import re
import warnings
import json

warnings.filterwarnings("ignore", category=DeprecationWarning)

def Search(query: str):
    """
    The search API for YouTube Music.
    """
    
    headers: dict = {
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36"
    }

    page_source: str = urllib.request.urlopen(urllib.request.Request(f"https://music.youtube.com/search?q={urllib.parse.quote(query)}", headers=headers)).read().decode("unicode_escape")

    if trackId := re.search('"videoId":"(.*?)"', page_source):
        trackId = json.loads(f"{{{trackId.group()}}}")["videoId"]

        meta = json.loads(urllib.request.urlopen(urllib.request.Request(f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={trackId}", headers=headers)).read())

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
