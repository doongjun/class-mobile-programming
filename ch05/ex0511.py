from flask import Flask, render_template

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    name = StringField('이름', validators=[DataRequired()])
    password = PasswordField('암호', validators=[DataRequired()])
    submit = SubmitField('Submit')


app = Flask(__name__)
app.config['SECRET_KEY'] = "hard to guess string"


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/ex0511", methods=['GET', 'POST'])
def ex0511():
    name = None
    form = LoginForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ""
        form.password.data = ""
    return render_template("ex0511.html", form=form, name=name)
