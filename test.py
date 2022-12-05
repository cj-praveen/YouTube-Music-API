from src import YouTubeMusicAPI

query: str = "alan walker faded remix"

result = YouTubeMusicAPI.Search(query)

# if result:
#     print(result)
# else:
#     print("No Result Found")
    

result_found = result if result else "No Result Found"
print(result_found)
