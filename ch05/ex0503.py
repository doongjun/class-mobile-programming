from flask import Flask, render_template
from flask import request

app = Flask(__name__)


@app.route("/ex0503", methods=['POST', 'GET'])
def ex0502():
    if request.method == "POST":
        form = request.form
        return render_template("ex0503.html", form=form)
    else:
        return render_template("ex0502_form.html")
