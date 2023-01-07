# YouTube Music API [unofficial]
 The YouTube Music search scraper for the Python programming language. 

## Installation instruction
- Python 3.6 or later is required.
- make sure the latest pip version is installed in your working environment.

**If you meet the above requirements, run the following command given below to install the latest version of YouTubeMusicAPI:**
```
pip install --no-cache -U YouTubeMusicAPI
```

## Get started
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

Program output:

If results are available for your search query, it will return a dict with data; otherwise, it will return an empty dict.

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
