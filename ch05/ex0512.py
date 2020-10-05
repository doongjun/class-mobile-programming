from flask import Flask, render_template

from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import RadioField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class PersonForm(FlaskForm):
    name = StringField('이름', validators=[DataRequired()])
    password = PasswordField('암호', validators=[DataRequired()])
    submit = SubmitField('Submit')


app = Flask(__name__)
app.config['SECRET_KEY'] = "hard to guess string"


@app.route("/ex0512", methods=['GET', 'POST'])
def ex0512():
    form = PersonForm()
    if form.validate_on_submit():
        fdata = form.data
        return render_template("ex0512.html", fdata=fdata)
    return render_template("ex0512_form.html", form=form)
