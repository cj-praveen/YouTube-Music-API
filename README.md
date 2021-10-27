# YouTubeMusicAPI

**What's new  in version 2.3?**

- Stable release.
- Improved Library Speed (**10x Faster than version [2.2](https://pypi.org/project/YouTubeMusicAPI/2.2/).**)
- Updated Code Format.
- Removed **artist()** for temporarily.

## 📜 About
- An unofficial YouTube Music API For Python Programming Language.<br>
- A Python library which Quickly gather the metadata of a Song, Playlist, Artist existing on **YouTube** or **YouTube Music**.

## 👤 Author
- [Sijey Praveen](https://github.com/sijey-praveen/)

## 🔑 ❌ No Access token or Credentials required.

## 📦 Package Installation
- Windows

`pip install --upgrade YouTubeMusicAPI`

- Linux & Mac OS

`pip3 install --upgrade YouTubeMusicAPI`

## 📚 GET Basic 

## track()
- This function can be used to get metadata of a track or song.

```python
from YouTubeMusicAPI import YouTubeMusicAPI

track = YouTubeMusicAPI("immortals").track()

print(track)
```

[![Track](https://i.imgur.com/2C9VdKO.png)](https://i.imgur.com/2C9VdKO.png)

### 👉 Output of this program

```
{
    'name': 'Fall Out Boy - Immortals (Official Music Video) (From "Big Hero 6")', 
    'datePublished': '2014-10-13', 
    'Id': 'l9PxOanFjxQ', 
    'url': 'https://music.youtube.com/watch?v=l9PxOanFjxQ', 
    'image': 'https://i.ytimg.com/vi/l9PxOanFjxQ/hqdefault.jpg'
}
```

<hr>

## playlist()
- This function can be used to get metadata of a playlist.

```python
from YouTubeMusicAPI import YouTubeMusicAPI

playlist = YouTubeMusicAPI("Alan Walker").playlist()

print(playlist)
```

[![Playlist](https://i.imgur.com/9rqpVKR.png)](https://i.imgur.com/9rqpVKR.png)

### 👉 Output of this program

```
{
    'name': 'Alan Walker - Teledyski', 
    'url': 'https://music.youtube.com/playlist?list=PLwcXu6NozQZjVjazNF0fqbdQ8e15mnMJ4', 
    'Id': 'PLwcXu6NozQZjVjazNF0fqbdQ8e15mnMJ4'
}
```

## 🧾 License
- [MIT License](https://mit-license.org/)

## 🤝 Contributing
- For major changes or improvement, Open an <a href="https://github.com/sijey-praveen/YouTube-Music-API/issues">issue</a> and mention what you would like to change or add. 

