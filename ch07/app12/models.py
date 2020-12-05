from . import db                                  ##2. SQLAlchemy instance

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    loginname = db.Column(db.String(64), unique=True, index = True)
    #relationship
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"))

    def __repr__(self):
        return "<User {}>".format(self.loginname)

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key = True)
    rolename = db.Column(db.String(64), unique=True)
    #relationship
    users = db.relationship('User', backref='role')
    
    def __repr__(self):
        return "<Role {}>".format(self.rolename)

### 추가
class Post(db.Model):
   __tablename__ = 'post'
   id = db.Column(db.Integer, primary_key=True)
   title = db.Column(db.String, nullable=False)
   content = db.Column(db.Text)
   cdate = db.Column(db.Date)
