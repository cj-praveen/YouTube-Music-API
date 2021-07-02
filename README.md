<img src="https://is3-ssl.mzstatic.com/image/thumb/Purple115/v4/f6/ec/80/f6ec8014-2dcc-abd1-f3ac-d6fbebd2326c/AppIcon-0-0-1x_U007emarketing-0-0-0-7-0-0-sRGB-0-0-0-GLES2_U002c0-512MB-85-220-0-0.png/230x0w.webp" width="100px">

# YouTube-Music-API

**What's new  in version 1.9?**

- Stable release.
- Updated **getsonginfo()** function.
- Updated Code Format.

<hr>

## How To Use

- To play the song, Create the code like this:

```python
# import the module

import YouTubeMusicAPI

# Use .play for playing song

# Type The Song Name inside the brackets eg: ("Faded Alan Walker")

YouTubeMusicAPI.play("Song Name")
```
- To play the song in VLC Media Player without downloading, Create the code like this:
```python
# import the module

import YouTubeMusicAPI

# Use .playonvlc for streaming song in VLC Media Player

# Type The Song Name inside the brackets eg: ("Faded Alan Walker")

YouTubeMusicAPI.playonvlc("Song Name")
```
- To get song meta data, Create the code like this:
```python
# import the module

import YouTubeMusicAPI

# Use .getsonginfo to get song information

# Type The Song Name inside the brackets eg: ("Faded")

YouTubeMusicAPI.getsonginfo("Song Name")

# Output

{
    'song_name': 'Faded', 
    'total_listeners': '29947694', 
    'duration': 213, 
    'artist': 'Alan Walker - Topic', 
    'album_art': 'https://i.ytimg.com/vi_webp/d0eUMnJ5kTA/maxresdefault.webp', 
    'artist_url': 'http://music.youtube.com/channel/UCaXJEi-wOOVe2eZZHzyz4mQ', 
    'track_url': 'https://music.youtube.com/watch?v=d0eUMnJ5kTA', 
    'track_id': 'd0eUMnJ5kTA'
}
```

<hr>

**MIT License | Copyright (c) 2021 Sijey**
