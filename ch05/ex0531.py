from flask import Flask, render_template
from flask import session, redirect, url_for

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    name = StringField('이름', validators=[DataRequired()])
    password = PasswordField('암호', validators=[DataRequired()])
    submit = SubmitField('Submit')


app = Flask(__name__)
app.config['SECRET_KEY'] = "hard to guess string"


@app.route("/ex0531", methods=['GET', 'POST'])
def ex0521():
    name = None
    form = LoginForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        password = form.password.data
        flash("당신의 암호는"+password+"로 ")
        form.name.data = ""
        form.password.data = ""
        return redirect(url_for("ex0521"))
    return render_template("ex0531.html", form=form,
                           name=session.get("name"))


@app.route("/")
def hello():
    return "hello world"


@app.route("/ex0531")
