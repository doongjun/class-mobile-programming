from flask import Flask, render_template
from flask import request

app = Flask(__name__)


@app.route("/ex0504", methods=['POST', 'GET'])
def ex0504():
    if request.method == "POST":
        x = request.form['x']
        return render_template("ex0504.html", x=int(x))
    else:
        return render_template("ex0504_form.html")
