from save_spend_share import app
# gunicorn seems to need the object to be called application. 
application = app
if __name__ == "__main__":
    application.run()