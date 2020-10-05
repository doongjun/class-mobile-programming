from flask import Flask, render_template

from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired


class SimpleForm(FlaskForm):
    x = IntegerField('몇 단?', validators=[DataRequired()])
    submit = SubmitField('Submit')


app = Flask(__name__)
app.config['SECRET_KEY'] = "hard to guess string"


@app.route("/ex0510", methods=['GET', 'POST'])
def ex0510():
    x = None
    form = SimpleForm()
    if form.validate_on_submit():
        x = form.x.data
    return render_template("ex0510.html", form=form, x=x)
