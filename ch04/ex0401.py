from flask import Flask, render_template

app = Flask(__name__)


@app.route("/ex0401")
def ex0401():
    x = 100
    z = "220"
    return render_template("ex0401.html", x=x, y=z)
