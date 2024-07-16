# YouTube Music API
An unofficial search API for YouTube Music.

[![Downloads](https://static.pepy.tech/badge/youtubemusicapi)](https://pepy.tech/project/youtubemusicapi)

**Installation:**
```
pip install -U YouTubeMusicAPI
```

##  Get Basic
```py
# Import the YouTubeMusicAPI module
import YouTubeMusicAPI

# Example query
query = "alan walker faded"

# Call the search function with the query
result = YouTubeMusicAPI.search(query)

# Check if a result was found
if result:
    # Print the retrieved result
    print(result)
else:
    # Print a message if no result was found
    print("No Result Found")
```

**Example Output:**
```json
{
    "title": "Alan Walker - Faded",
    "id": "60ItHLz5WEA",
    "url": "https://music.youtube.com/watch?v=60ItHLz5WEA",
    "artwork": "https://img.youtube.com/vi/60ItHLz5WEA/0.jpg",
    "author": {
        "name": "Alan Walker",
        "url": "https://www.youtube.com/@Alanwalkermusic"
    }
}
```
## License
Free and open-source under [MIT License](LICENSE).
