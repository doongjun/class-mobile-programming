from flask import Flask, render_template
from flask import request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route("/")
def example12a():
    return render_template("ex0412a.html")


@app.route("/ex0412")
def example12b():
    return render_template("notexist.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500
