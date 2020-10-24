from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import config

boostrap = Bootstrap()
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    boostrap.init_app(app)
    db.init_app(app)

    @app.route("/")
    def hello():
        return "<h2>hello world</h2>"

    return app
