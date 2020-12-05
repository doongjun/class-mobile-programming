import datetime

from flask import render_template
from flask import session, redirect, url_for
from flask import request
from ..models import db  # 2. SQLAlchemy instance
from ..models import User
from ..models import Post
from . import auth  # 추가해 주어야 함. instance이름
from .forms import LoginForm

@auth.route("/login",methods=["GET", "POST"])
def login():
    form = LoginForm()
    return render_template("auth/login.html", form=form)

