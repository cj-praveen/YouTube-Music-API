# [YouTubeMusicAPI](https://pypi.org/project/YouTubeMusicAPI/)

**What's new  in version 2.5?**

- Stable release.

## About
- An unofficial YouTube Music API For Python Programming Language.<br>
- A Python library which Quickly gather the metadata of a Song, Playlist existing on **YouTube** or **YouTube Music**.
- No Access token or Credentials required.

## Package Installation
- Windows

`pip install --upgrade YouTubeMusicAPI==2.5`

- Linux & Mac OS

`pip3 install --upgrade YouTubeMusicAPI==2.5`

## GET Basic 

- track()

This function can be used to get metadata of a track or song.

```python
from YouTubeMusicAPI import YouTubeMusicAPI

track = YouTubeMusicAPI().track("faded")

print(track)

# output
{
    'name': 'Alan Walker - Faded',
    'Id': '60ItHLz5WEA',
    'url': 'https://music.youtube.com/watch?v=60ItHLz5WEA',
    'image': 'https://i.ytimg.com/vi/60ItHLz5WEA/hqdefault.jpg',
    'author_name': 'Alan Walker',
    'author_url': 'https://www.youtube.com/c/Alanwalkermusic'
}
```

<hr>

- playlist()

This function can be used to get metadata of a playlist.

```python
from YouTubeMusicAPI import YouTubeMusicAPI

playlist = YouTubeMusicAPI().playlist("Alan Walker")

print(playlist)

# output
{
    'name': 'Alan Walker - Topic',
    'url': 'https://music.youtube.com/playlist?list=PLnXZKEb05pjONeO2hRSnd077lc76f_6Rf',
    'Id': 'PLnXZKEb05pjONeO2hRSnd077lc76f_6Rf',
    'author_name': 'RadioActiva',
    'author_url': 'https://www.youtube.com/channel/UC_48oWtBy2_qqe_QJUxROlA'
}
```

- searchUrls()

This function can be used to get all result urls based on query.

```python
from YouTubeMusicAPI import YouTubeMusicAPI

urls = YouTubeMusicAPI().searchUrls("alone")

print(urls)

#output
[
    'https://music.youtube.com/watch?v=bPs0xFd4skY',
    'https://music.youtube.com/watch?v=TCFuCCY-pxc',
    'https://music.youtube.com/watch?v=ciwx8yJPX54',
    'https://music.youtube.com/watch?v=aZwklvDdaVw',
    'https://music.youtube.com/watch?v=ALZHF5UqnU4',
    'https://music.youtube.com/watch?v=KDzL80906Xo',
    'https://music.youtube.com/watch?v=HhjHYkPQ8F0'
]
```

## Author
- [Sijey Praveen](https://github.com/sijey-praveen/)

## License
- [MIT License](https://mit-license.org/)

## Contributing
- For major changes or improvement, Open an <a href="https://github.com/sijey-praveen/YouTube-Music-API/issues">issue</a> and mention what you would like to change or add. 

