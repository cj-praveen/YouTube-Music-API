# YouTube Music API [unofficial]
The search API for [YouTube Music](https://music.youtube.com/)

## Installation:
- Python 3.6 or later is required.
- Run the following command given below to install the latest version of the package:
```
python -m pip install --disable-pip-version-check --no-cache -U YouTubeMusicAPI
```

## Get started with examples:
### Basic implementation
```python
import YouTubeMusicAPI

query: str = "alan walker faded"

result = YouTubeMusicAPI.Search(query)

if result:
    print(result)
else:
    print("No Result Found")
```

### Implementing with FastAPI
Run the following command given below to install the latest version of [fastapi](https://pypi.org/project/fastapi/) and [uvicorn](https://pypi.org/project/uvicorn/).

```
python -m pip install --disable-pip-version-check --no-cache -U fastapi uvicorn
```

```python
from fastapi import FastAPI
import uvicorn
import YouTubeMusicAPI

app = FastAPI()

@app.get("/")
def main(q: str) -> dict:
    return YouTubeMusicAPI.Search(q)

uvicorn.run(app)
```

### Downloading Tracks with YouTubeDL
Run the following command given below to install the latest version of [youtubedl](https://pypi.org/project/youtube-dl/).

```
python -m pip install --disable-pip-version-check --no-cache -U youtube-dl
```

```python
from youtube_dl import YoutubeDL
import YouTubeMusicAPI

query: str = "ncs fearless pt2"

result: dict = YouTubeMusicAPI.Search(query)

if result:
    YoutubeDL({ "format": "bestaudio/best" }).download([result["trackUrl"]])
else:
    print("no result found.")
```
