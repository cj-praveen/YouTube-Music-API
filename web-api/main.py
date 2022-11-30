from flask import Flask, Response, request
from flask_cors import CORS, cross_origin
from json import dumps, loads
from urllib.request import Request, urlopen
from re import search
from warnings import filterwarnings
from urllib.parse import quote

app = Flask(__name__)
CORSA(app)
headers: dict = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
filterwarnings("ignore", category=DeprecationWarning)

def getVideoId(query: str):
	page_source: str = urlopen(Request(f"https://music.youtube.com/search?q={quote(query)}", headers=headers)).read().decode("unicode_escape")
	if videoId := search('"videoId":"(.*?)"', page_source):
		return loads(f"{{{videoId.group()}}}")["videoId"]
	return None

@app.route("/get_url", methods=["GET"])
@cross_origin()
def get_url():
	if not request.args.get("query"):
		return Response(response="No Search Query Passed", status=400, mimetype="text/plain")
	if videoId := getVideoId(request.args.get("query")):
		return Response(response=f"https://music.youtube.com/watch?v={videoId}", status=200, mimetype="text/plain")
	else:
		return Response(response="No URL Found", status=405, mimetype="text/plain")

@app.route("/get_track", methods=["GET"])
@cross_origin()
def get_track():
	if not request.args.get("query"):
		return Response(response="No Search Query Passed", status=400, mimetype="text/plain")
	if videoId := getVideoId(request.args.get("query")):
		meta: dict = loads(urlopen(Request(f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={videoId}", headers=headers)).read())

		return Response(dumps(dict(
			name = meta["title"],
			id = videoId,
			url = f"https://music.youtube.com/watch?v={videoId}",
			images = [
				f"https://i.ytimg.com/vi/{videoId}/hqdefault.jpg",
				f"https://i.ytimg.com/vi/{videoId}/default.jpg",
				f"https://i.ytimg.com/vi/{videoId}/mqdefault.jpg",
				f"https://i.ytimg.com/vi/{videoId}/sddefault.jpg",
				f"https://i.ytimg.com/vi/{videoId}/maxresdefault.jpg"
			],
			author_name = meta["author_name"],
			author_url = meta["author_url"]
		), indent=4), status=200, mimetype="application/json")

	else:
		return Response(response="No Result Found", status=405, mimetype="text/plain")

app.run("0.0.0.0", 5000)
