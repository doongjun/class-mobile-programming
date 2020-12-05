from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///friends.db'
#Initialize the database
db = SQLAlchemy(app)

#Create database model
class Friends(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200),nullable=False)
    content = db.Column(db.Text,nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    #Create a function to return a string when we add something
    def __repr__(self):
        return f"<Friends ('{self.id}','{self.name}')>"

subscribers = []

@app.route('/lists')
def lists():
    title = "Lists"
    query = db.session.query(Friends)
    friends = Friends.query.order_by(Friends.date_created)
    return render_template('lists.html', title=title, friends=friends)

@app.route('/read/<int:id>')
def read(id):
    friend_to_read = Friends.query.get_or_404(id)
    query = db.session.query(Friends)
    friends = Friends.query.order_by(Friends.date_created)
    return render_template('read.html', friend_to_read = friend_to_read)

@app.route('/delete/<int:id>')
def delete(id):
    friend_to_delete = Friends.query.get_or_404(id)

    try:
        db.session.delete(friend_to_delete)
        db.session.commit()
        return redirect('/lists')
    except:
        return "There was problem deleting that friend..."


@app.route('/update/<int:id>', methods=['POST', 'GET'])
def update(id):
    friend_to_update = Friends.query.get_or_404(id)
    if request.method == "POST":
        friend_to_update.name = request.form['name']
        friend_to_update.content = request.form['content']
        try:
            db.session.commit()
            return redirect('/lists')
        except:
            return "There was a problem updating that friend..."
    else:
        return render_template('update.html', friend_to_update = friend_to_update)

@app.route('/friends', methods=['POST', 'GET'])
def friends():
    title = "게시글 작성"
    
    if request.method == "POST":
        friend_name = request.form['name']
        friend_content = request.form['content']
        n_post = Friends(name=friend_name, content=friend_content)

        #push to database
        try:
            db.session.add(n_post)
            db.session.commit()
            return redirect('/lists')
        except:
            return "There was an error adding your friend... "
    else:
        return render_template("friends.html",title=title)


@app.route('/')
def index():
    title = "Dongjun's Blog"
    return render_template("index.html", title=title)

@app.route('/about')
def about():
    title = "About Eulji University"
    names = ["의료IT학과","간호학과","의료홍보디자인학과","치위생학과","등등"]
    return render_template("about.html",names=names, title=title)

@app.route('/subscribe')
def subscribe():
    title = "Subscribe"
    return render_template("subscribe.html", title=title)

@app.route('/form', methods=["POST"])
def form():
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    email = request.form.get("email")

    if not first_name or not last_name or not email:
        error_statement = "All Form Fields Required.."
        return render_template("subscribe.html", error_statement=error_statement, 
        first_name = first_name, last_name=last_name, email=email)

    subscribers.append(f"{first_name} {last_name} | {email}")
    title = "Thank you!"
    return render_template("form.html", title=title, subscribers=subscribers)