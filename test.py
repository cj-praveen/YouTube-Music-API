from src import YouTubeMusicAPI

query: str = "alan walker faded remix"

result: dict = YouTubeMusicAPI.Search(query)

print(result) if result else print("No Result Found")
