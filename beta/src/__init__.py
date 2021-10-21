from requests import get
from warnings import filterwarnings
from flask import Flask, request
from flask_cors import cross_origin, CORS

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
    def suggestion():
        re = get("https://music.youtube.com/search?q={}".format(query.replace(" ", "+")), headers=user_agent).content.decode("unicode_escape").split('"')
        count = 0
        for i in re:
            count += 1
            if "videoId" == i : id = re[count + 1]
        return f"https://music.youtube.com/watch?v={id}"

    def url():
        count, results = 0, get(f"https://www.youtube.com/results?q={query}", headers=user_agent).text.split('"')
        for i in results:
            count += 1
            if i == "WEB_PAGE_TYPE_WATCH" : break
        if "watch" in results[count - 5] : id = results[count - 5]
        return f"https://music.youtube.com{id}"

    return dict(url = url(), suggested_music_video = suggestion())

app.run(host="0.0.0.0", debug=True)
