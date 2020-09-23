from flask import Flask, render_template
from flask import request

app = Flask(__name__)


@app.route("/ex0403")  # http://127.0.0.1:5000/ex0403?jumsu=90
def ex0403():
    # jumsu=83
    jumsu = request.args.get("jumsu")
    if jumsu:
        jumsu = int(jumsu)
    else:  # jumsu==none
        jumsu = 0
    return render_template("ex0403.html", jumsu=jumsu)
