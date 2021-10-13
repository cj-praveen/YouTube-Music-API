
## Basic GET usage:

```python
from YouTubeMusicAPI import YouTubeMusicAPI

artist = YouTubeMusicAPI().get_track("Marshmello")

print(track)

# output of this program

{
    'track_name': 'Alone', 
    'datePublished': '2018-06-21', 
    'track_Id': 'OBs1Fb8adGQ', 
    'track_url': 'https://music.youtube.com/watch?v=OBs1Fb8adGQ', 
    'track_image': 'https://i.ytimg.com/vi/OBs1Fb8adGQ/hqdefault.jpg'
}
```
