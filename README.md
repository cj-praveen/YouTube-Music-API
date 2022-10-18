# YouTubeMusicAPI 2.7

The search API for [YouTube Music](https://music.youtube.com/).

```
pip install YouTubeMusicAPI
```

## Example

```python
import YouTubeMusicAPI

result = YouTubeMusicAPI.Search("Alan walker faded")

print(result)

# output
# {
#     "name": "Alan Walker - Faded",
#     "Id": "60ItHLz5WEA",
#     "url": "https://music.youtube.com/watch?v=60ItHLz5WEA",
#     "image": "https://i.ytimg.com/vi/60ItHLz5WEA/hqdefault.jpg",
#     "author_name": "Alan Walker",
#     "author_url": "https://www.youtube.com/c/Alanwalkermusic"
# }
```

## License
This Python package is distributed under the [MIT License](https://mit-license.org/).
