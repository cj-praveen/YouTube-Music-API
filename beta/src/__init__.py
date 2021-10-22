from requests import get
from warnings import filterwarnings
from flask import Flask, request
from flask_cors import cross_origin, CORS
from bs4 import BeautifulSoup

app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"
user_agent = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0"}
filterwarnings("ignore", category=DeprecationWarning)

@app.route("/", methods = ["GET"])
@cross_origin()
def main():
    if request.args.get("q") == None : return "Query is None!"
    else : query = request.args.get("q")

    count ,ytm = 0, get("https://music.youtube.com/search?q={}".format(query.replace(" ", "+")), headers=user_agent).content.decode("unicode_escape").split('"')
    for i in ytm:
        count += 1
        if "videoId" == i : break
    ytm_id = ytm[count + 1]

    count ,yt = 0, get(f"https://www.youtube.com/results?q={query}", headers=user_agent).text.split('"')
    for i in yt:
        count += 1
        if i == "videoId" : break
    yt_id = yt[count + 1]

    ytwp = BeautifulSoup(get(f"https://www.youtube.com/watch?v={yt_id}").text, "html.parser")
    ytmwp = BeautifulSoup(get(f"https://www.youtube.com/watch?v={ytm_id}").text, "html.parser")

    return {
        "result" : {
            "name" : ytwp.find("meta", attrs={"name" : "title"}).get("content"),
            "Id" : yt_id,
            "url" : f"https://music.youtube.com/watch?v={yt_id}",
            "image" : f"https://i.ytimg.com/vi/{yt_id}/hqdefault.jpg",
            "datePublished" : ytwp.find("meta", attrs={"itemprop" : "datePublished"}).get("content")
            },

        "suggested_music_video" : {
            "name" : ytmwp.find("meta", attrs={"name" : "title"}).get("content"),
            "Id" : ytm_id,
            "url" : f"https://music.youtube.com/watch?v={ytm_id}",
            "image" : f"https://i.ytimg.com/vi/{ytm_id}/hqdefault.jpg",
            "datePublished" : ytwp.find("meta", attrs={"itemprop" : "datePublished"}).get("content")
            }
    }

app.run(host="0.0.0.0", debug=True)
