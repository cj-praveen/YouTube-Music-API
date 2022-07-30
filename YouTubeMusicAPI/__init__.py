from requests import get
from re import search
from warnings import filterwarnings

filterwarnings("ignore", category=DeprecationWarning)

def Search(query : str):

    user_agent = {
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36"
    }

    id = search('"videoId":"(.*?)"', get(f"https://music.youtube.com/search?q={query}", headers=user_agent).content.decode("unicode_escape"))

    if id:
        id = id.group().split(":")[1].replace('"', "")
        
        meta = get(f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={id}", headers=user_agent).json()

        return dict(
            name = meta["title"],
            Id = id,
            url = f"https://music.youtube.com/watch?v={id}",
            image = f"https://i.ytimg.com/vi/{id}/hqdefault.jpg",
            author_name = meta["author_name"],
            author_url = meta["author_url"]
        )

    else:
        return dict(message = "No Track Found!")
