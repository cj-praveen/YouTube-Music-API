# YouTubeMusicAPI

<a href="https://raw.githubusercontent.com/sijey-praveen/YouTube-Music-API/Sijey/LICENSE"><img align="right" src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" width="130px"></a>

**What's new  in version 2.1?**

- Stable release.
- Updated Code Format.

## About
An unofficial YouTube Music API For Python Programming Language.<br>
A Python library which Quickly gather the metadata of a Song, Playlist, Artist existing on **YouTube** or **YouTube Music**.


## Basic GET usage:

```python
from YouTubeMusicAPI import YouTubeMusicAPI

# type == search type

# available search types >>> ['artist', 'playlist', 'track']

artist = YouTubeMusicAPI("marshmello", type="artist")
track = YouTubeMusicAPI("marshmello", type="track")
playlist = YouTubeMusicAPI("marshmello", type="playlist")

print(artist, track, playlist)
```

- output 

```
{
    'artist': 'Marshmello', 
    'artist_url': 'https://music.youtube.com/channel/UCEdvpU2pFRCVqU6yIPyTpMQ', 
    'artist_id': 'UCEdvpU2pFRCVqU6yIPyTpMQ', 
    'artist_image': 'https://yt3.ggpht.com/3kmvsf3NNYy4XLy3hKc2ZVF8O-XkSaahtwUr3KW-YzJKMJsy-g2HePIayrh-JnXWbilYQ6n_=s900-c-k-c0x00ffffff-no-rj'
} 

{
    'track_name': 'Marshmello Live at Lollapalooza 2021 [Full DJ Set]', 
    'datePublished': '2021-08-04', 
    'track_Id': '8eXFvzMEldk', 
    'track_url': 'https://music.youtube.com/watch?v=8eXFvzMEldk', 
    'track_image': 'https://i.ytimg.com/vi/8eXFvzMEldk/hqdefault.jpg'
}

{
    'playlist_name': 'Marshmallow Playlist', 
    'playlist_url': 'https://music.youtube.com/playlist?list=PL4FB1JvhTLrGNSL4odYt72EqjDPJfjSdp', 
    'playlist_id': 'PL4FB1JvhTLrGNSL4odYt72EqjDPJfjSdp'
}
```

## Contributing
- <a href="https://github.com/sijey-praveen/YouTube-Music-API/pulls">Pull requests</a> are welcome. For major changes or improvement, please open an <a href="https://github.com/sijey-praveen/YouTube-Music-API/issues">issue</a> first to discuss what you would like to change or add. 
