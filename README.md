# [YouTubeMusicAPI](https://pypi.org/project/YouTubeMusicAPI/)

An open-source Python library which helps to find a song or track existing on **YouTube Music**

[![](https://img.shields.io/badge/Made_with-Golang-blue?logo=go&style=flat-square)](https://go.dev/)
[![](https://img.shields.io/badge/License-Creative_Commons-ed9321?logo=creativecommons&style=flat-square)](https://creativecommons.org/)
[![](https://img.shields.io/badge/GitHub-sijey--praveen/YouTube--Music--API-ebebeb?logo=github&style=flat-square)](https://github.com/sijey-praveen/YouTube-Music-API/)
[![](https://img.shields.io/badge/Discord-sijey%239115-5865f2?logo=discord&style=flat-square)](https://discordapp.com/users/856839376436985876)
[![Downloads](https://static.pepy.tech/personalized-badge/youtubemusicapi?period=total&units=none&left_color=black&right_color=blue&left_text=Downloads)](https://pepy.tech/project/youtubemusicapi)

## Package Installation
```
pip install YouTubeMusicAPI==2.6
```

## Example

```python
from YouTubeMusicAPI import Search

result = Search("Alan walker faded")

print(result)

# output

{
    "name": "Faded",
    "Id": "pIWaVJPl0-c",
    "url": "https://music.youtube.com/watch?v=pIWaVJPl0-c",
    "image": "https://i.ytimg.com/vi/pIWaVJPl0-c/hqdefault.jpg",
    "author_name": "Alan Walker - Topic",
    "author_url": "https://www.youtube.com/channel/UCaXJEi-wOOVe2eZZHzyz4mQ"
}
```

## License

Copyright (c) 2020 - present, Sijey. All rights reserved.

The source is free to copy, modify, publish, use, compile, sell, or distribute.., licensed under the [MIT License](https://mit-license.org/).
