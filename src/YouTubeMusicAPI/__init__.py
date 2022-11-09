from urllib.request import Request, urlopen
from urllib.parse import quote
from re import search
from warnings import filterwarnings
from json import loads, dumps

filterwarnings("ignore", category=DeprecationWarning)

def Search(query: str):

    headers: dict = {
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36"
    }

    page_source: str = urlopen(Request(f"https://music.youtube.com/search?q={quote(query)}", headers=headers)).read().decode("unicode_escape")

    id = search('"videoId":"(.*?)"', page_source)

    if id:
        id = loads(f"{{{id.group()}}}")["videoId"]
        
        meta = loads(urlopen(Request(f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={id}", headers=headers)).read())

        return dumps(dict(
            name = meta["title"],
            id = id,
            url = f"https://music.youtube.com/watch?v={id}",
            images = [
                f"https://i.ytimg.com/vi/{id}/hqdefault.jpg",
                f"https://i.ytimg.com/vi/{id}/default.jpg",
                f"https://i.ytimg.com/vi/{id}/mqdefault.jpg",
                f"https://i.ytimg.com/vi/{id}/sddefault.jpg",
                f"https://i.ytimg.com/vi/{id}/maxresdefault.jpg"
            ],
            author_name = meta["author_name"],
            author_url = meta["author_url"]
        ))

    else:
        return dict(message = "No Track Found!")