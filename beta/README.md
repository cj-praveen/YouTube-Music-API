# Development Progess

- [ ] Accurate search result
- [ ] Search result suggestions

<hr>


## Basic GET usage:

```python
from YouTubeMusicAPI import YouTubeMusicAPI

artist = YouTubeMusicAPI().get_track("Marshmello Alone")

print(track)

# output of this program

{
    'track_name': 'Marshmello - Alone (Official Music Video)', 
    'datePublished': '2016-07-02', 
    'track_Id': 'ALZHF5UqnU4', 
    'track_url': 'https://music.youtube.com/watch?v=ALZHF5UqnU4', 
    'track_image': 'https://i.ytimg.com/vi/ALZHF5UqnU4/hqdefault.jpg'
}
```
