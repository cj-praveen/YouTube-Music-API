<img src="https://is3-ssl.mzstatic.com/image/thumb/Purple115/v4/f6/ec/80/f6ec8014-2dcc-abd1-f3ac-d6fbebd2326c/AppIcon-0-0-1x_U007emarketing-0-0-0-7-0-0-sRGB-0-0-0-GLES2_U002c0-512MB-85-220-0-0.png/230x0w.webp" width="100px">

# YouTube-Music-API

**How It Works**
- Get Song Name For User and Redirect to <a href="https://music.youtube.com/">Youtube Music</a> Official website.

## How To Use

- For Playing a song, Create the code like this:

```python
# import the module

import YouTubeMusicAPI as ytm

# Use .play for playing song

# Type The Song Name inside the brackets eg: ("Faded Alan Walker")

ytm.play("Song Name")
```
- For playing the song in VLC Media Player without downloading, Create the code like this:
```python
# import the module

import YouTubeMusicAPI as ytm

# Use .playonvlc for streaming song in VLC Media Player

# Type The Song Name inside the brackets eg: ("Faded Alan Walker")

ytm.playonvlc("Song Name")
```

**MIT License, Copyright (c) 2021 Sijey**
