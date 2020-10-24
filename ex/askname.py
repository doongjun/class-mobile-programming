from flask import Blueprint

name = Blueprint("name", __name__, template_folder="templates")


@name.route('/')
def question():
    return "What your name?"


@name.route('/<name>')
def answer(name):
    return "My name is "+name
