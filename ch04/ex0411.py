from flask import Flask, render_template
from flask import request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/ex0411a")
def example11a():
    return render_template("ex0411a.html")


@app.route("/ex0411b")
def example11b():
    return render_template("ex0411b.html")


@app.route("/ex0411c")
def example11c():
    return render_template("ex0411c.html")
