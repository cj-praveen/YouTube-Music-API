from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, World!"

app.run("0.0.0.0", 5000)

#####################################

# from src import YouTubeMusicAPI

# query: str = "alan walker faded"

# result = YouTubeMusicAPI.Search(query)

# if result:
#     print(result)
# else:
#     print("No Result Found")
