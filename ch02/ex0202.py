from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/example2a")
def ex0202a():
	arguments = request.args.get("Search")
	return "<p>데이터 : <BR> {}</p>".format(arguments)

@app.route("/example2b")
def ex0202b():
	arguments = request.args
	return "<p>데이터 : <BR> {}</p>".format(arguments)