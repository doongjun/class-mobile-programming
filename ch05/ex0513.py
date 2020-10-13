from flask import Flask, render_template

from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import SelectField, SelectMultipleField, SubmitField
from wtforms.validators import DataRequired


class TestForm(FlaskForm):
    where = SelectField(
        "시험장소", choices=[('1', '서울'), ('2', '경기도')], validators=[DataRequired()])
    subjects = SelectMultipleField("시험과목", choices=[(
        'korean', '국어'), ('English', '영어')], validators=[DataRequired()])
    submit = SubmitField('Submit')


app = Flask(__name__)
app.config['SECRET_KEY'] = "hard to guess string"
bootstrap = Bootstrap(app)


@app.route("/ex0513", methods=['GET', 'POST'])
def ex0513():
    form = TestForm()
    if form.validate_on_submit():
        fdata = form.data
        return render_template("ex0512.html", fdata=fdata)
    return render_template("ex0513_form.html", form=form)


@app.route("/ex0512a", methods=['GET', 'POST'])
def ex0512a():
    form = TestForm()
    if form.validate_on_submit():
        fdata = form.data
        return render_template("ex0512.html", fdata=fdata)
    return render_template("ex0512a_form.html", form=form)
