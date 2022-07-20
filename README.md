# [YouTubeMusicAPI](https://pypi.org/project/YouTubeMusicAPI/)

**What's new  in version 2.5?**

- Stable release.

## About
An open-source Python library which Quickly gather the metadata of a Song, Playlist existing on **YouTube** or **YouTube Music**. No Access token or Credentials required.

[![Downloads](https://static.pepy.tech/personalized-badge/youtubemusicapi?period=total&units=none&left_color=black&right_color=blue&left_text=Downloads)](https://pepy.tech/project/youtubemusicapi)

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
```

<hr>

- playlist()

This function can be used to get metadata of a playlist.

```python
from YouTubeMusicAPI import YouTubeMusicAPI

playlist = YouTubeMusicAPI().playlist("Alan Walker")

print(playlist)
```

- searchUrls()

This function can be used to get all result urls based on query.

```python
from YouTubeMusicAPI import YouTubeMusicAPI

urls = YouTubeMusicAPI().searchUrls("alone")

print(urls)
```

## License

(c) 2020 - 2022 Sijey All rights reserved.

The source is free to copy, modify, publish, use, compile, sell, or distribute.., licensed under the [MIT License](https://mit-license.org/).
