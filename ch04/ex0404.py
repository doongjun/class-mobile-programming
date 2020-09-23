from flask import Flask, render_template

app = Flask(__name__)


@app.route("/ex0404a")
def ex0404a():
    x = 40
    y = 20
    result = [x+y, x-y, x*y, x/y]  # list
    return render_template("ex0404a.html", result=result)


@app.route("/ex0404b")
def ex0404b():
    x = 40
    y = 20
    result = {}
    result["sum"] = x+y
    result["subtract"] = x-y
    result["multiply"] = x*y
    result["divide"] = x/y

    return render_template("ex0404b.html", result=result)
