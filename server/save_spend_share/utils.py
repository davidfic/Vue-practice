
from save_spend_share import database as db
def deposit(name,amount,bucket):
    db.add_money(name,amount,bucket)

def withdraw(name,amount,bucket):
    
    result = db.withdraw_money(name,amount,bucket)
    if result:
        return 0
    return 1



