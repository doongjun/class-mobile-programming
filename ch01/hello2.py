from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
	return "<h3>Hello World!</h1>"

@app.route("/user/<name>")
def user(name):
	return "<h3>Hello,{}!</h3>".format(name)