from flask import Flask, render_template

app = Flask(__name__)


@app.route("/ex0402a")
def ex0402a():
    x = 10
    y = 20
    result = [x+y, x-y, x*y, x/y]  # list
    return render_template("ex0402a.html", result=result)


@app.route("/ex0402b")
def ex0401b():
    x = 10
    y = 20
    result = {}
    result["sum"] = x+y  # dictionary
    result["subtract"] = x-y
    result["multiply"] = x*y
    result["divide"] = x/y

    return render_template("ex0402b.html", result=result)
