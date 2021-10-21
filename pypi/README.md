# YouTubeMusicAPI

<a href="https://raw.githubusercontent.com/sijey-praveen/YouTube-Music-API/Sijey/LICENSE"><img align="right" src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" width="130px"></a>

**What's new  in version 2.2?**

- Stable release.
- Updated Code Format.

## 📜 About
An unofficial YouTube Music API For Python Programming Language.<br>
A Python library which Quickly gather the metadata of a Song, Playlist, Artist existing on **YouTube** or **YouTube Music**.

## 📚 Basic GET usage:

```python
from YouTubeMusicAPI import YouTubeMusicAPI

artist = YouTubeMusicAPI("marshmello").artist()

print(artist)

# output of this program

{
    'artist': 'Marshmello', 
    'artist_url': 'https://music.youtube.com/channel/UCEdvpU2pFRCVqU6yIPyTpMQ', 
    'artist_id': 'UCEdvpU2pFRCVqU6yIPyTpMQ', 
    'artist_image': 'https://yt3.ggpht.com/3kmvsf3NNYy4XLy3hKc2ZVF8O-XkSaahtwUr3KW-YzJKMJsy...'
} 
```

```python
from YouTubeMusicAPI import YouTubeMusicAPI

track = YouTubeMusicAPI("marshmello").track()

print(track)

# output of this program

{
    'track_name': 'Marshmello Live at Lollapalooza 2021 [Full DJ Set]', 
    'datePublished': '2021-08-04', 
    'track_Id': '8eXFvzMEldk', 
    'track_url': 'https://music.youtube.com/watch?v=8eXFvzMEldk', 
    'track_image': 'https://i.ytimg.com/vi/8eXFvzMEldk/hqdefault.jpg'
}
```

```python
from YouTubeMusicAPI import YouTubeMusicAPI

playlist = YouTubeMusicAPI("marshmello").artist()

print(playlist)

# output of this program

{
    'playlist_name': 'Marshmallow Playlist', 
    'playlist_url': 'https://music.youtube.com/playlist?list=PL4FB1JvhTLrGNSL4odYt72EqjDPJfjSdp', 
    'playlist_id': 'PL4FB1JvhTLrGNSL4odYt72EqjDPJfjSdp'
}
```


## 🔗 Links
[![blog](https://img.shields.io/badge/DEV_Community-000?style=for-the-badge&logo=devdotto&logoColor=white)](https://dev.to/sijeypraveen/youtube-music-api-ecj)
[![linkedin](https://img.shields.io/badge/PyPI-000?style=for-the-badge&logo=pypi&logoColor=white)](https://pypi.org/project/YouTubeMusicAPI/)

## 🤝 Contributing
- For major changes or improvement, Open an <a href="https://github.com/sijey-praveen/YouTube-Music-API/issues">issue</a> and mention what you would like to change or add. 

