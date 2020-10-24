import os
import datetime

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask import request

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
db_url = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_DATABASE_URI'] = False

db = SQLAlchemy(app)


class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.Text)
    cdate = db.Column(db.Date)


@app.route("/")
def list():
    query = db.session.query(Post)
    posts = query.order_by(Post.cdate.desc()).all()
    num = len(posts)
    return render_template("list.html", num=num, posts=posts)


@app.route("/new_form", methods=['POST', 'GET'])
def new_form():
    if request.method == "POST":
        title = request.form['title']
        content = request.form['content']
        d = datetime.date.today()
        # 데이터베이스에 새로운 메세지를 추가한다.
        n_post = Post(title=title, comtent=content, cdate=d)
        db.session.add(n_post)
        db.session.commit()
        return render_template("new.html")
    else:
        return render_template("new_form.html")


@app.route("/view", methods=['POST', 'GET'])
def view():
    mid = request.args.get('mid', 1, type=int)
    # 데이터베이스에서 기존의 메세지를 읽는다.
    query = db.session.query(Post)
    query = query.filter(Post.id == mid)
    v_post = query.one()
    return render_template("view.html", post=v_post)


@app.route("/update", methods=['POST', 'GET'])
def update():
    mid = request.args.get('mid', 1, type=int)
    # 데이터베이스에서 기존의 메세지를 읽을 준비한다.
    query = db.session.query(Post)
    query = query.filter(Post.id == mid)
    if request.method == "POST":
        query.update(
            {Post.title: request.form['title'],
                Post.content: request.form['content']}
        )
        db.session.commit()
        return render_template("update.html")
    else:  # 기존의 메세지 내용을 읽어서 보여주다
        u_post = query.one()
        return render_template("update_form.html", post=u_post)


@app.route("/delete", methods=['POST', 'GET'])
def delete():
    mid = request.args.get('mid', 1, type=int)
    # 데이터베이스에서 기존의 메세지를 삭제한다.
    query = db.session.query(Post)
    query = query.filter(Post.id == mid)
    query.delete()
    db.session.commit()
    return render_template("update.html")
