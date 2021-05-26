<img src="https://is3-ssl.mzstatic.com/image/thumb/Purple115/v4/f6/ec/80/f6ec8014-2dcc-abd1-f3ac-d6fbebd2326c/AppIcon-0-0-1x_U007emarketing-0-0-0-7-0-0-sRGB-0-0-0-GLES2_U002c0-512MB-85-220-0-0.png/230x0w.webp" width="100px">

# YouTube-Music-API

<a href="https://pypi.org/project/requests/"><img src="https://img.shields.io/badge/requests-2.25.1-blue" width="120px"></a>
<a href="https://pypi.org/project/pafy/"><img src="https://img.shields.io/badge/pafy-0.5.5-yellow" width="85px"></a>
<a href="https://pypi.org/project/youtube_dl/"><img src="https://img.shields.io/badge/youtube_dl-2021.4.26-red" width="155px"></a>
<a href="https://pypi.org/project/sockets/"><img src="https://img.shields.io/badge/sockets-1.0.0-green" width="110px"></a>

<hr>

**Features**
- Get Song Name For User and stream directly in <a href="https://music.youtube.com/">Youtube Music</a> Official website.
- Get Song Name For User and Download using pafy | youtube_dl

**How To Use**

- For Playing a song, Create the code like this:

```python
# import the module

import YouTubeMusicAPI as ytm

# Use .play for playing song

# Type The Song Name inside the brackets eg: ("Faded Alan Walker")

ytm.play("Song Name")
```
- For downloading the song, Create the code like this:

```python
# import the module

import YouTubeMusicAPI as ytm

# Use .download for downloading song

# Type The Song Name & download path inside the brackets eg: ("Faded Alan Walker, "C:\Downloads\")

ytm.download("Song Name", "Path")
```
- For playing the song in vlc without downloading, Create the code like this:
```python
# import the module

import YouTubeMusicAPI as ytm

# Use .playonvlc for streaming song in VLC Media Player

# Type The Song Name inside the brackets eg: ("Faded Alan Walker")

ytm.playonvlc("Song Name")
```

**MIT License, Copyright (c) 2021 Sijey**
