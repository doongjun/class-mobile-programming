from flask import Flask

import os
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

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


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role)
