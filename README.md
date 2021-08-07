# YouTubeMusicAPI

<a href="https://raw.githubusercontent.com/sijey-praveen/YouTube-Music-API/Sijey/LICENSE"><img align="right" src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" width="130px"></a>

**What's new  in version 2.0?**

- Stable release.
- Updated **get_track()** function.
- Updated Code Format.

<hr>

## About
An unofficial YouTube Music API For Python Programming Language.
A Python library which Quickly gather the metadata of a Song existing on **YouTube** or **YouTube Music**.

<hr>

## Basic GET usage:

### get_track()
- This function can be used to get meta data of a song existing on **YouTube** or **YouTube Music**.

- Use the function with Song or track or music name.

```python
from YouTubeMusicAPI import YouTubeMusicAPI

var = YouTubeMusicAPI("marshmello happier").get_track()

print(var)
```

**Output of this program:**

```

{
    'track_name': 'Marshmello ft. Bastille - Happier (Official Music Video)', 
    'datePublished': '2018-09-24', 
    'track_Id': 'm7Bc3pLyij0', 
    'track_url': 'https://music.youtube.com/watch?v=m7Bc3pLyij0', 
    'track_image': 'https://i.ytimg.com/vi/m7Bc3pLyij0/hqdefault.jpg', 
    'interactionCount': '851450849', 
    'artist': 'Marshmello', 
    'artist_url': 'https://music.youtube.com/channel/UCEdvpU2pFRCVqU6yIPyTpMQ', 
    'artist_id': 'UCEdvpU2pFRCVqU6yIPyTpMQ', 
    'artist_image': 'https://yt3.ggpht.com/3kmvsf3NNYy4XLy3hKc2ZVF8O-XkSaahtwUr3KW-YzJKMJsy-g2HePIayrh-JnXWbilYQ6n_=s900-c-k-c0x00ffffff-no-rj'
}
```

<hr>

## Contributing
- <a href="https://github.com/sijey-praveen/PaperPro/pulls">Pull requests</a> are welcome. For major changes or improvement, please open an <a href="https://github.com/sijey-praveen/PaperPro/issues">issue</a> first to discuss what you would like to change or add. 
