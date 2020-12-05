from flask import Flask, render_template

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')


app = Flask(__name__)

app.config['SECRET_KEY'] = '어려운 암호 키'


@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():  # 폼이 제출될 때 true 다르면 false
        name = form.name.data
        form.name.data = ''
    return render_template('index.html', form=form, name=name)


if __name__ == '__main__':
    app.run(debug=True)
