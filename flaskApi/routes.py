from flaskApi import app, db, consumer

@app.route('/')
def index():
    consumer.listAll("test")
    return 'Debug'
