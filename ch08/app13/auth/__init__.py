from flask import Blueprint            #1.Blueprint

auth = Blueprint('/auth', __name__)   #전역 변수로 생성

from . import views, forms