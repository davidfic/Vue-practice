from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from save_spend_share.exceptions import WishlistNameCollision
import os
try:
    sql_password = os.environ['SQL_PASSWORD']
except:
    print('sql password env variable not set')
# db_string = f"postgres://xtlkdgnm:{sql_password}@isilo.db.elephantsql.com/xtlkdgnm"
heroku_connection_string = f'postgresql://hrodkyqwtxxszx:{sql_password}@ec2-23-23-92-204.compute-1.amazonaws.com/de6ngqr9gj5g90'
db = create_engine(heroku_connection_string)
Session = sessionmaker(bind=db)

    
def get_kids_from_db():
    result_set = db.execute('SELECT name from kids')
    kids = []
    
    for item in result_set:
        kids.append(item)

    return kids


def add_kid_to_db(name):

    sql = f"INSERT into kids (name)  VALUES ('{name}')"
    db.execute(sql)

def add_wishlist(kid,wishlist_name,amount,goal_date):
    """
    check if kid already has used this wishlist name as they have to be unique
    """
    session = Session()

    now = datetime.now()
    wishlists = db.execute("SELECT wishlist_name FROM wishlist")
    if wishlist_name in wishlists:
        print('wishlist name collision returning exception')
        return WishlistNameCollision

    sql = f"""INSERT INTO wishlist ( kid_id, wishlist_name, amount, goal_date, complete, goal_amount, date ) 
            VALUES ('{kid}', '{wishlist_name}', '{amount}', '{goal_date}', 0, 0,'{now}' ) """
    db.execute(sql)

    return 0

def get_wishlists(kid):
    if not kid:
        return []
    kid_id = get_kid_id(kid)

    wishlists = []
    sql = f"select wishlist_name,complete,amount,goal_date, goal_amount from wishlist where kid_id = '{kid}'"
    results = db.execute(sql)
    for result in results:
        wishlists.append(result)
    

    return wishlists

def add_money(kid,amount,bucket):
    # need to grab the previous total and add/sub this new amount

    now = datetime.now()
    sql = f"INSERT into {bucket}(kid_id, amount, date )  VALUES ( (select id from kids where name = '{kid}' ), {amount}, '{now}')"
    db.execute(sql) 


def withdraw_money(kid,amount,bucket):
    # need to grab the previous total and add/sub this new amount
    # TODO: check to see if withdrawal amount from bucket will 
    # # go below 0 
    now = datetime.now()
    sql = f"INSERT into {bucket}(kid_id, amount, date )  VALUES ( (select id from kids where name = '{kid}' ), {amount}, '{now}')"
    db.execute(sql) 

def get_kid_id(kid):
    if not kid:
        return 0
    else:
        print(f'kid is {kid}')
    result = ''
    sql = f"select id from kids where name = '{kid}'"
    results = db.execute(sql)
    for r in results:
        result = r
    return result


def get_totals(kid):
    # return dictionary of kid with amount in each bucket
    totals = {}
    if not kid:
        return 0
    totals[kid] = {'save':  get_total(kid,'save'), 
                    'share': get_total(kid,'share'), 'spend': get_total(kid,'spend')}
    return totals


def get_total(kid,bucket):
    total = 0 
    if not kid:
        return 0
    else:
        print(f'in get_total and kid is {kid}')
    kid_id = get_kid_id(kid)
    print(f'kid_id is {kid_id} in get_total')
    sql = f"select sum(amount) from {bucket} where kid_id = {kid_id[0]}"
    results = db.execute(sql)
    for result in results:
        total = result
    if total[0]:
        return total[0]
    
    return 0



