<<<<<<< HEAD
from flaskApi import app, db, consumer
from flaskApi.task import Task
from flask import jsonify, request
from flaskApi.errors import bad_request

@app.route('/')
def index():
    i = 0
    msgList = []
    for msg in consumer.listMessages("test"):
        i +=1
        msgList.append(msg)
        if i >= 5:
            break
    msgString = ' '.join(str(x) for x in msgList)
    return msgString

@app.route('/v1.0/tasks/<int:id>')
def getTask(id):
    task = Task.query.get_or_404(id)
    return jsonify(task.to_dict())

@app.route('/v1.0/tasks')
def getAllTasks():
    tasks = Task.query.all()
    data = ""
    for task in tasks:
        data += "{}".format(task.to_dict())
    return data

@app.route('/v1.0/tasks', methods=['POST'])
def createTask():
    data = request.get_json()
    print("data",data)
    if not request.json or not 'longDescription' in request.json:
        return bad_request("No long description provided")
    task = Task()
    task.from_dict(data)
    db.session.add(task)
    db.session.commit()
    response = jsonify(data)
    response.status_code = 201
    return response
