# YouTube Music API
The search API for [YouTube Music](https://music.youtube.com/).

## Installation:
- Python 3.6 or later is required.
- First, please make sure that the latest **pip** version is installed in your working environment.
```
python -m pip install -U pip
```
- Run the following command given below to install the package:
```
python -m pip install -U YouTubeMusicAPI
```

## Get Started
Here is an example program.
```python
import YouTubeMusicAPI

query: str = "alan walker faded"

result = YouTubeMusicAPI.Search(query)

if result:
    print(result)
else:
    print("No Result Found")
```
If a result for your search query is found, it will return an **dict object**; otherwise, it will return an **empty dict object**. 
```json
{
    "trackName": "...",
    "trackId": "...",
    "trackUrl": "...",
    "artworkUrl": "...",
    "artistName": "...",
    "artistUrl": "..."
}
```

## Implementing in FastAPI
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
