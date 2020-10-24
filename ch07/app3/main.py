from flask import Blueprint
from flask import session, redirect, url_for
from . import db
from flask import render_template

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class NameForm(FlaskForm):
    name = StringField('Your Name?', validators=[DataRequired()])
    submit = SubmitField('Submit')


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    loginname = db.Column(db.String(64), unique=True, index=True)
    # relationship
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"))

    def __repr__(self):
        return "<User {}>".format(self.loginname)


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    rolename = db.Column(db.String(64), unique=True)
    # relationship
    users = db.relationship('User', backref='role')

    def __repr__(self):
        return "<Role {}>".format(self.rolename)


main = Blueprint('main', __name__)


@main.route("/", methods=['GET', 'POST'])
def hello():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(loginname=form.name.data).first()
        if user is None:
            user = User(loginname=form.name.data)
            db.session.add(user)
            db.session.commit()
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ""
        return redirect(url_for("hello"))
    return render_template("ex0612.html", form=form, name=session.get('name'), known=session.get("known", False))
