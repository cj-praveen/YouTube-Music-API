from src import YouTubeMusicAPI

query: str = "alan walker faded"

result = YouTubeMusicAPI.YouTubeMusicAPI(query)

if result:
    print(result)
else:
    print("No Result Found")
