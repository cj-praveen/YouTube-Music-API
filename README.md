# [YouTubeMusicAPI](https://pypi.org/project/YouTubeMusicAPI/)

**What's new  in version 2.4?**

- Stable release.
- New **searchUrls()** function added.

## About
- An unofficial YouTube Music API For Python Programming Language.<br>
- A Python library which Quickly gather the metadata of a Song, Playlist existing on **YouTube** or **YouTube Music**.
- No Access token or Credentials required.

## Package Installation
- Windows

`pip install --upgrade YouTubeMusicAPI==2.4`

- Linux & Mac OS

`pip3 install --upgrade YouTubeMusicAPI==2.4`

## GET Basic 

- track()

This function can be used to get metadata of a track or song.

```python
from YouTubeMusicAPI import YouTubeMusicAPI

track = YouTubeMusicAPI().track("immortals")

print(track)

# output

{
    'name': 'Fall Out Boy - Immortals (Official Music Video) (From "Big Hero 6")', 
    'datePublished': '2014-10-13', 
    'Id': 'l9PxOanFjxQ', 
    'url': 'https://music.youtube.com/watch?v=l9PxOanFjxQ', 
    'image': 'https://i.ytimg.com/vi/l9PxOanFjxQ/hqdefault.jpg'
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
    'name': 'Alan Walker - Teledyski', 
    'url': 'https://music.youtube.com/playlist?list=PLwcXu6NozQZjVjazNF0fqbdQ8e15mnMJ4', 
    'Id': 'PLwcXu6NozQZjVjazNF0fqbdQ8e15mnMJ4'
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

