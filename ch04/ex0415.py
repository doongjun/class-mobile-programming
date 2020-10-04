from flask import Flask, render_template
from flask import request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route("/ex0415a")
def example14a():
    return render_template("ex0415a.html")


@app.route("/ex0415b")
def example14b():
    return render_template("ex0415b.html")


@app.route("/ex0415c")
def example14c():
    return render_template("ex0415c.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template
