from flaskApi import app, db

@app.route('/')
def index():
    return "Hello, World!"
