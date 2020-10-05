from flask import Flask, render_template

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class NameForm(FlaskForm):
    name = StringField('Your Name?', validators=[DataRequired()])
    submit = SubmitField('Submit')


app = Flask(__name__)
app.config['SECRET_KEY'] = "hard to guess string"


@app.route("/", methods=['GET', 'POST'])
def hello():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.date = ""
    return render_template("hello.html", form=form, name=name)
