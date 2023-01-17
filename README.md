# YouTube Music API
The YouTube Music search scraper for the Python programming language.

## Installation:
- Python 3.7 or later is required.
- First, please make sure that the latest pip version is installed in your working environment.
```
pip install -U pip
```
- Run the following command given below to install the package:
```
pip install -U YouTubeMusicAPI
```

## Get Started
Here is an example program.

```py
import YouTubeMusicAPI

query: str = "alan walker faded"

result = YouTubeMusicAPI.search(query)

if result:
    print(result)
else:
    print("No Result Found")
```
If a result for your search query is found while running the above program, it will return an **dict object** `{"title":"...", "id": "...", "url": "...", "artwork": "...", "author": {"name": "...", "url": "..."}}` ; otherwise, it will return **None**.

## License
This Python package is licenced under the MIT License.
