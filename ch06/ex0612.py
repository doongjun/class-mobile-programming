from flask_sqlalchemy import SQLAlchemy
from flask import session, redirect, url_for
import os
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class NameForm(FlaskForm):
    name = StringField('Your Name?', validators=[DataRequired()])
    submit = SubmitField('Submit')


app = Flask(__name__)
app.config['SECRET_KEY'] = "hard to guess string"


basedir = os.path.abspath(os.path.dirname(__file__))  # 파일의 절대경로 저장
db_url = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)  # SQLAlchemy를 인스턴스화


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


@app.route("/ex0612", methods=['GET', 'POST'])
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
