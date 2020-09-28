from flask import Flask, render_template
from flask import request

app = Flask(__name__)


@app.route("/ex0501", methods=['POST', 'GET'])
def ex0501():
    if request.method == "POST":
        name = request.form['name']
        password = request.form['password']
        return render_template("ex0501.html", name=name, password=password)
    else:
        return render_template("ex0501_form.html")
