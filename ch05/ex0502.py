from flask import Flask, render_template
from flask import request

app = Flask(__name__)


@app.route("/ex0502", methods=['POST', 'GET'])
def ex0502():
    if request.method == "POST":
        gender = request.form['gender']
        test = request.form['test']
        return render_template("ex0502.html", gender=gender, test=test)
    else:
        return render_template("ex0502_form.html")
