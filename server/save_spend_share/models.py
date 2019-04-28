import datetime

from flask_sqlalchemy import SQLAlchemy
#from save_spend_share import app, login_manager

db = SQLAlchemy(app)


class Kids(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.name


class Spend(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    amount = db.Column(db.Integer, unique=True, nullable=False)
    date = db.Column(DateTime, default=datetime.datetime.utcnow)
    kid_id = db.Column(db.Integer, db.ForeignKey('Kids.id'),
        nullable=False)

    def __repr__(self):
        return '<User %r>' % self.name
 

class Wishlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    wishlist_name = db.Column(db.String(128), unique=True, nullable=False)
    complete = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Integer, unique=True, nullable=False)
    goal_amount =db.Column(db.Integer, unique=True, nullable=False) 
    goal_date = db.Coulmn(db.DateTime, nullable=False)
    date = db.Column(DateTime, default=datetime.datetime.utcnow)
    kid_id = db.Column(db.Integer, db.ForeignKey('Kids.id'), nullable=Flase)

    def __repr__(self):
        return '<Wishlist %r>' % self.wishlist_name


db.create_all()
