from fastapi import FastAPI
from uvicorn import run
from requests import get
from re import search
from warnings import filterwarnings
from json import loads, dumps

filterwarnings("ignore", category=DeprecationWarning)

app = FastAPI()

@app.get("/")
def main_(query: str):
    if query:
        page_source: str = get(f"https://music.youtube.com/search?q={query}", headers={"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36"}).content.decode("unicode_escape")

        id = search('"videoId":"(.*?)"', page_source)

        if id:
            id = loads(f"{{{id.group()}}}")["videoId"]
            
            meta = get(f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={id}", headers=user_agent).json()

            return dumps(dict(
                name = meta["title"],
                Id = id,
                url = f"https://music.youtube.com/watch?v={id}",
                image = f"https://i.ytimg.com/vi/{id}/hqdefault.jpg",
                author_name = meta["author_name"],
                author_url = meta["author_url"]
            ))
        else:
            return dict(message = "no track found!")

    return dict(message = "No search query passed.")

run(app=app, host="0.0.0.0", port=5000)
