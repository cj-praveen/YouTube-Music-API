import warnings, httpx, re

warnings.filterwarnings("ignore", category=DeprecationWarning)

def search(query: str) -> dict:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0.1) Gecko/20100101 Firefox/123.0.1"
    }

    try:
        page = httpx.get(f"https://music.youtube.com/search?q={query}", headers=headers).content.decode("unicode_escape")

        trackId = re.search(r'"videoId":"(.*?)"', page)

        if not trackId:
            return {}

        trackId = trackId.group(1)

        track_info = httpx.get(f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={trackId}",
                               headers=headers).json()

        return {
            "title": track_info["title"],
            "id": trackId,
            "url": f"https://music.youtube.com/watch?v={trackId}",
            "artwork": f"https://img.youtube.com/vi/{trackId}/0.jpg",
            "author": {
                "name": track_info["author_name"],
                "url": track_info["author_url"]
            }
        }

    except Exception as e:
        print(f"An error occurred: {e}")
        return {}


if __name__ == "__main__":
    result = search("alan walker faded")
    print(result)
