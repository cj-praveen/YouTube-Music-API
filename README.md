[![Loading Image](https://img.shields.io/badge/GitHub-sijey--praveen/Shift-ebebeb?logo=github&style=social)](https://github.com/sijey-praveen/Shift/)
[![Loading Image](https://img.shields.io/badge/PyPI-pypi.org/project/YouTubeMusicAPI-ebebeb?logo=pypi&style=social)](https://pypi.org/project/YouTubeMusicAPI/)

# [YouTubeMusicAPI](https://pypi.org/project/YouTubeMusicAPI/)

An open-source Python library which helps to find a song or track existing on **YouTube Music**

## Package Installation
```
pip install YouTubeMusicAPI==2.6.0
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

This Python Package is licensed under the [MIT License](https://mit-license.org/).
