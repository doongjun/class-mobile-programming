from flask import Flask, render_template

app = Flask(__name__)


@app.route("/ex0406")
def ex0406():
    result = {}
    result["한국"] = "김밥"
    result["중국"] = "짜장면"
    result["미국"] = "햄버거"

    return render_template("ex0406.html", result=result)
