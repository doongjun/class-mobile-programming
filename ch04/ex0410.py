from flask import Flask, render_template
app = Flask(__name__)


@app.route("/ex0410")
def example10():
    return render_template("ex0410.html")
