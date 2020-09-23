from flask import Flask, render_template

app = Flask(__name__)


@app.route("/example7a")
def ex0407a():
    return render_template("ex0407a.html")


@app.route("/example7b")
def ex0407b():
    return render_template("ex0407b.html")
