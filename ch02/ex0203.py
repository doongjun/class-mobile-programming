from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/example3a")
def ex0203a():
	return "<H3>Good Request</H3>"

@app.route("/example3b")
def ex0203b():
	return "<H3>Bad Request</H3>",400