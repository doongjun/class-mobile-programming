from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "hello world!"


@app.route('/name')
def question():
    return "What your name?"


@app.route('/name/<name>')
def answer(name):
    return "My name is "+name


if __name__ == '__main__':
    app.run()
