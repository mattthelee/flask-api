from flaskApi import app, db, consumer

@app.route('/')
def index():
    i = 0
    msgList = []
    for msg in consumer.listAll("test"):
        i +=1
        msgList.append(msg)
        if i >= 5:
            break
    msgString = ' '.join(str(x) for x in msgList)
    return msgString
