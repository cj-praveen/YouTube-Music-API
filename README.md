<img src="https://is3-ssl.mzstatic.com/image/thumb/Purple115/v4/f6/ec/80/f6ec8014-2dcc-abd1-f3ac-d6fbebd2326c/AppIcon-0-0-1x_U007emarketing-0-0-0-7-0-0-sRGB-0-0-0-GLES2_U002c0-512MB-85-220-0-0.png/230x0w.webp" width="100px">

# YouTube-Music-API

**What's new  in version 1.7?**

- Stable release.
- **Get Song Information** feature added.

<hr>

## How To Use

- For Playing a song, Create the code like this:

```python
# import the module

import YouTubeMusicAPI

# Use .play for playing song

# Type The Song Name inside the brackets eg: ("Faded Alan Walker")

YouTubeMusicAPI.play("Song Name")
```
- For playing the song in VLC Media Player without downloading, Create the code like this:
```python
# import the module

import YouTubeMusicAPI

# Use .playonvlc for streaming song in VLC Media Player

# Type The Song Name inside the brackets eg: ("Faded Alan Walker")

YouTubeMusicAPI.playonvlc("Song Name")
```
- To get song information, Create the code like this:
```python
# import the module

import YouTubeMusicAPI

# Use .getsonginfo to get song information

# Type The Song Name inside the brackets eg: ("Faded")

YouTubeMusicAPI.getsonginfo("Song Name")

# Output
{'Name': 'Faded', 'ID': 'd0eUMnJ5kTA', 'Total Listeners': '29,808,990', 'Duration': '3:33', 'Artist': 'Alan Walker', 'URL': 'https://music.youtube.com/watch?v=d0eUMnJ5kTA'}
```

<hr>

**MIT License | Copyright (c) 2021 Sijey**
```
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software
```
