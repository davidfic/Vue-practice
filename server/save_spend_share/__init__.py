from flask import Flask

import os
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS



sql_password = ''
try:
    sql_password = os.environ['SQL_PASSWORD']
except:
    print('sql password env variable not set11')



app = Flask(__name__)


# connection_string = f'postgresql://xtlkdgnm:{sql_password}@isilo.db.elephantsql.com/xtlkdgnm'
heroku_connection_string = f'postgresql://hrodkyqwtxxszx:{sql_password}@ec2-23-23-92-204.compute-1.amazonaws.com/de6ngqr9gj5g90'
app.config['SQLALCHEMY_DATABASE_URI'] = heroku_connection_string
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# enable CORS
CORS(app)



db = SQLAlchemy(app)
# Base = declarative_base()
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(128), nullable=False)

class Kids(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


class Save(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # kid_id = db.Column(db.String(80), unique=True, nullable=False)
    amount = db.Column(db.Integer, unique=True, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    kid_id = db.Column(db.Integer, db.ForeignKey('kids.id'),nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username
        
class Share(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # kid_id = db.Column(db.String(80), unique=True, nullable=False)
    amount = db.Column(db.Integer, unique=True, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    kid_id = db.Column(db.Integer, db.ForeignKey('kids.id'), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


class Spend(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # kid_id = db.Column(db.String(80), unique=True, nullable=False)
    amount = db.Column(db.Integer, unique=True, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    kid_id = db.Column(db.Integer, db.ForeignKey('kids.id'), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username
 
class Wishlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # kid_id = db.Column(db.String(80), unique=True, nullable=False)
    wishlist_name = db.Column(db.String(80), unique=True, nullable=False)
    complete = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    goal_amount = db.Column(db.Integer, nullable=False)
    goal_date = db.Column(db.DateTime)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    kid_id = db.Column(db.Integer, db.ForeignKey('kids.id'), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

class Chores(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # kid_id = db.Column(db.String(80), unique=True, nullable=False)
    chore_name = db.Column(db.String(80), unique=True, nullable=False)
    complete = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    kid_id = db.Column(db.Integer, db.ForeignKey('kids.id'),nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


# db.create_all()

from save_spend_share import routes
