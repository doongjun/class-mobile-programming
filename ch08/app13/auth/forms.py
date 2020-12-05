from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField #2 FlaskForm
from wtforms import BooleanField, SubmitField #3 FlaskForm
from wtforms.validators import DataRequired, Length, Email
from wtforms.validators import Regexp, EqualTo
from wtforms import ValidationError
from ..models import User

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log in')