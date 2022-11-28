# YouTubeMusicAPI 2.7.1

The search API for [YouTube Music](https://music.youtube.com/).

```
python -m pip install -U YouTubeMusicAPI
```

## Example

```python
import YouTubeMusicAPI

result = YouTubeMusicAPI.Search("shape of you")

print(result)

# output
# {
#     "name": "Ed Sheeran - Shape of You (Official Music Video)",
#     "id": "JGwWNGJdvx8",
#     "url": "https://music.youtube.com/watch?v=JGwWNGJdvx8",
#     "images": [
#         "https://i.ytimg.com/vi/JGwWNGJdvx8/hqdefault.jpg",
#         "https://i.ytimg.com/vi/JGwWNGJdvx8/default.jpg",
#         "https://i.ytimg.com/vi/JGwWNGJdvx8/mqdefault.jpg",
#         "https://i.ytimg.com/vi/JGwWNGJdvx8/sddefault.jpg",
#         "https://i.ytimg.com/vi/JGwWNGJdvx8/maxresdefault.jpg"
#     ],
#     "author_name": "Ed Sheeran",
#     "author_url": "https://www.youtube.com/c/EdSheeran"
# }
```

## License
This Python package is distributed under the [MIT License](https://mit-license.org/).
