from flask import Flask, render_template
from flask import request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route("/ex0414a")
def example14a():
    return render_template("ex0303.html")


@app.route("/ex0414b")
def example14b():
    return render_template("ex0304.html")


@app.route("/ex0414c")
def example14c():
    return render_template("ex0305.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template
