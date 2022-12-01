from src import YouTubeMusicAPI

query: str = "alan walker faded remix"

result = YouTubeMusicAPI.Search(query)

if result:
    print(result)
else:
    print("No Result Found")
