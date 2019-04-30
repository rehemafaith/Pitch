from app import db
from werkzeug.security import generate_password_hash,check_password_hash 
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'



    id = db.Column(db.Integer,primary_key = True)
    username =db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))
    pitches = db.relationship('Pitch', backref = 'user',lazy = "dynamic")
    comments = db.relationship("Comment", backref="user", lazy = "dynamic")

    def save_user(self):
        db.session.add(self)
        db.session.commit()


    @property

    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def get_user_pitches(self):
        user = User.query.filter_by(id = self.id).first()
        return user.pitches

    def get_user_comments(self):
        user = User.query.filter_by(id = self.id).first()
        return user.comments

        
    def __repr__(self):
        return f'User {self.username}'
        
class Pitch(db.Model):

    __tablename__ = 'pitches'

    id = db.Column(db.Integer,primary_key= True)
    content = db.Column(db.String)
    title = db.Column(db.String)
    date = db.Column(db.String)
    time = db.Column(db.String)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    comments = db.relationship("Comment", backref = "pitch", lazy = "dynamic")
    category = db.Column(db.String)

    
    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitch(cls,id):
        pitches = Pitch.query.filter_by(pitch_id=id).first()
        comments = Comment.query.filter_by(pitch_id = pitch.id).order_by(Comment.time.desc())
        return pitches 

class Comment(db.Model):
    
    __tablename__= "comments"

    id = db.Column(db.Integer,primary_key = True)
    content = db.Column(db.String)
    date = db.Column(db.String)
    time = db.Column(db.String)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    pitch_id = db.Column(db.Integer,db.ForeignKey("pitches.id"))

    def save_comment(self):
        db.session.ass(self)
        db.session.commmit()

def init_db():
    db.create_all()


    db.session.commit()

if __name__ == '__main__':
    init_db()
