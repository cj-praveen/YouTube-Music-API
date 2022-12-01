from src import YouTubeMusicAPI

query: str = "alan walker faded"

result = YouTubeMusicAPI.Search(query)

if result:
    print(result)
else:
    print("No Result Found")
