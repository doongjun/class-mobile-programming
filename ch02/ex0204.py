from flask import Flask
from flask import request, make_response

app = Flask(__name__)

@app.route("/example4a")
def ex0204a():
	response = make_response("<h3>이 문서에서 쿠키를 설정했어요</h3>")
	response.set_cookie("news","good")
	return response

@app.route("/example4b")
def ex0204b():
	headers = request.headers
	return "<p>Headers 데이터 : <BR> {}</p>".format(headers)

@app.route("/example5a")
def ex0205a():
	response = make_response("<h3>이 문서에서 쿠키를 삭제했어요</h3>")
	response.delete_cookie("news")
	return response

@app.route("/example5b")
def ex0205b():
	headers = request.headers
	return "<p>Headers 데이터 : <BR> {}</p>".format(headers)