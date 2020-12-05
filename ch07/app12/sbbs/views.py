import datetime

from flask import render_template
from flask import session, redirect, url_for
from flask import request
from ..models import db                  #2. SQLAlchemy instance
from ..models import User
from ..models import Post
from . import sbbs     #추가해 주어야 함. instance이름

#from .forms import NameForm

@sbbs.route("/")
def list():
   query = db.session.query(Post)
   posts = query.order_by(Post.cdate.desc()).all()   #게시물 날짜 최신이 젤 앞으로
   num = len(posts)
   return render_template("list.html", num=num, posts=posts)
@sbbs.route("/new_form", methods=['POST','GET'])
def new_form():
    if request.method == "POST":
        title = request.form['title']
        content = request.form['content']
        d = datetime.date.today()
        # Database에 새로운 메시지를 추가한다.
        n_post = Post(title=title, content=content, cdate=d)
        db.session.add(n_post)
        db.session.commit()
        return render_template("new.html")
    else:
        return render_template("new_form.html")

@sbbs.route("/view", methods=['POST','GET'])
def view():
    mid = request.args.get('mid',1,type=int)
    #데이터 베이스에서 기존의 메시지를 읽는다.
    #query = db.session.query(Post)
    #query = query.filter(Post.id==mid)
    query = Post.query.filter_by(id=mid)
    v_post = query.one()
    return render_template("view.html", post=v_post)

@sbbs.route("/update", methods=['POST','GET'])
def update():
    mid = request.args.get('mid', 1, type=int)
    # 데이터베이스에서 기존의 메시지를 읽을 준비한다.
    query = db.session.query(Post)
    #query = db.query.filter(Post.id==mid)
    #query = Post.query.filter_by(Post)
    query = Post.query.filter(Post.id==mid)
    if request.method == "POST":  #수정하기
        query.update(
            {Post.title : request.form['title'],
            Post.content : request.form['content']} )
        db.session.commit()
        return render_template("update.html")
    else:  #기존의 메시지 내용을 읽어서 
        u_post = query.one()
        return render_template("update_form.html", post=u_post)

@sbbs.route("/delete", methods=['POST','GET'])
def delete():
    mid = request.args.get('mid', 1, type=int)
    query = db.session.query(Post)
    query = query.filter(Post.id == mid)
    query.delete()
    db.session.commit()
    return render_template("update.html")
