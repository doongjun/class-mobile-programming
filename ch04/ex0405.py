from flask import Flask, render_template

app = Flask(__name__)


@app.route("/ex0405")
def ex0405():
    result = {}
    result["kbs"] = "http://www.kbs.co.kr"
    result["mbc"] = "http://www.mbc.co.kr"
    result["sbs"] = "http://www.sbs.co.kr"

    return render_template("ex0405.html", result=result)


@app.route("/ex0405a")
def ex0405a():
    result = {}
    result["korea"] = "불고기"
    result["england"] = "피쉬앤칩스"
    result["america"] = "햄버거"

    return render_template("ex0405a.html", result=result)
