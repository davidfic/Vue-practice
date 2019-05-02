from save_spend_share import app
from flask import request, jsonify, render_template, redirect, flash, url_for, session

from save_spend_share import database as db
from save_spend_share import utils as utils

from save_spend_share.exceptions import WishlistNameCollision
import flask
import logging
import timber
from flask_cors import CORS

# users = {'admin': {'password': 'password'}}
users = {'dylan': {'password': 'password'}, 'ben': {'password': 'password'}}
app.config['RECAPTCHA_PUBLIC_KEY'] = 'TEST'
app.config['SECRET_KEY'] = 'USE-YOUR-OWN-SECRET-KEY-DAMNIT'



# todos =   {'userId': 1,'id': 1,'title': "delectus aut autem",'completed': False}
#     ,
#     {
#     'userId': 1,
#     'id': 2,
#     'title': "quis ut nam facilis et officia qui",
#     'completed': False
#     },
#     {
#     'userId': 1,
#     'id': 3,
#     'title': "fugiat veniam minus",
#     'completed': False
#     },
#     {
#     'userId': 1,
#     'id': 4,
#     'title': "et porro tempora",
#     'completed': True
#     },
#     {
#     'userId': 1,
#     'id': 5,
#     'title': "laboriosam mollitia et enim quasi adipisci quia provident illum",
#     'completed': False
#     }
# ]


@app.route('/kids')
def get_kids():
    kids = get_kids_from_db()
    return jsonify(get_kids_from_db())


@app.route('/chores', methods = ['POST', 'GET'])
def chores():
    chores = [
        {'id': 1, 'completed': False, 'title': 'laundry'},
        {'id': 2, 'completed': False, 'title': 'sweeping'},
        {'id': 3, 'completed': False, 'title': 'trash'},
        {'id': 4, 'completed': False, 'title': 'bathroom'},
    ]
    return jsonify(chores)


@app.route('/wishlists', methods=['POST', 'GET'])
def wishlists():
    if request.method == 'POST':
        print('hello there from post')
        # amount = request.data('amount')
        print(f"request data is {request.data}")
        
    wishlists = [
        {'id': 1, 'name': 'xbox', 'goal': 250, 'added': 50},
        {'id': 2, 'name': 'lego', 'goal': 80, 'added': 75},
        {'id': 3, 'name': 'ps4', 'goal': 250, 'added': 200}
    ]
    return jsonify(wishlists)

@app.route('/todos', methods=['POST', 'GET'])
def todos():
    todos = [
        {'id': 1, 'name': 'wish1', 'goal': 100, 'added': 22},
        {'id': 2, 'name': 'wish2', 'goal': 101, 'added': 3},
        {'id': 3, 'name': 'wish3', 'goal': 102, 'added': 75}
    ]
    return jsonify(todos)
    
@app.route('/')
@app.route('/home')#, methods=['POST', 'GET'])
def home():
    return jsonify('hello from home')



