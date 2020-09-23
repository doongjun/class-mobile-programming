from flask import Flask
from flask import redirect, make_response

app = Flask(__name__)

@app.route("/example6")
def ex0206():
	return redirect("http://www.naver.com")

@app.route("/example6a")
def ex0206a():
	response = make_response("<h3>이 문서에서 쿠키를 설정했어요</h3>")
	response.status_code = 302
	response.headers["Location"]="https://www.kbs.co.kr"
	return response

@app.route("/example6b")
def ex0206b():
	dic = {"Location" : "http://www.sbs.co.kr"}
	return "Hello", 302, dic