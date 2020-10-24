from flask import Flask
from askname import name

app = Flask(__name__)
# 등록될 프린트의 개체, 사용될 url (url_prefix)
app.register_blueprint(name, url_prefix="/name")


@app.route('/')
def hello_world():
    return 'hello world'


if __name__ == '__main__':
    app.run()
