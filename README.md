# YouTube Music API
An unofficial YouTube Music search API

## Installation
1) Python 3.9 or later is required.
2) make sure that the latest pip version is installed in your working environment.
```
pip install -U pip
```
3) Run the following command given below to install the package:
```
pip install -U YouTubeMusicAPI
```

## Usage
To use this package, you need to import it in your Python program and call the `search` function with a query string as an argument. The function will return a dictionary object with the following keys:
- `title`: The title of the song.
- `id`: The id of the song on YouTube Music.
- `url`: The url of the song on YouTube Music.
- `artwork`: The url of the artwork image of the song.
- `author`: A dictionary object with two keys: name and url, which represent the name and url of the author of the song.

If no result is found for your query, the function will return None.

## Example
Here is an example of how to use this package to search by song name.
```py
import YouTubeMusicAPI

query: str = "alan walker faded"

result = YouTubeMusicAPI.search(query)

if result:
    print(result)
else:
    print("No Result Found")
```

#### Output:
```json
{
    "title": "Alan Walker - Faded",
    "id": "60ItHLz5WEA",
    "url": "https://music.youtube.com/watch?v=60ItHLz5WEA",
    "artwork": "https://img.youtube.com/vi/60ItHLz5WEA/0.jpg",
    "author": {
        "name": "Alan Walker",
        "url": "https://www.youtube.com/@Alanwalkermusic"
    }
}
```
