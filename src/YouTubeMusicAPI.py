import warnings
import httpx
import re
import typing

warnings.filterwarnings("ignore", category=DeprecationWarning)


def search(query: str) -> typing.Dict[str, str] | typing.Dict:

    headers: dict = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0"}

    page: str = httpx.get(f"https://music.youtube.com/search?q={query}", headers=headers,
                          timeout=None).content.decode("unicode_escape")

    trackId: typing.Optional[str,None] = re.search('"videoId":"(.*?)"', page)

    if not trackId:
        return {}

    trackId: str = eval(f"{{{trackId.group()}}}")["videoId"]

    track_info: dict = httpx.get(f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={trackId}",
                                 headers=headers, timeout=None).json()

    return dict(
        title=track_info["title"],
        id=trackId,
        url=f"https://music.youtube.com/watch?v={trackId}",
        artwork=f"https://img.youtube.com/vi/{trackId}/0.jpg",
        author=dict(name=track_info["author_name"], url=track_info["author_url"])
    )
