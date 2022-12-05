from src import YouTubeMusicAPI

query: str = "alan walker faded remix"

if result := YouTubeMusicAPI.Search(query):
    print(result)
else:
    print("No Result Found")
