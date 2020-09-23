from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
	return "<h1>Hello World!</h1>"

@app.route("/kim")
def kim():
	return "<h1>Hello kim!</h1>"

@app.route("/lee")
def lee():
	return "<h1>Hello lee!</h1>"