from kafka import KafkaConsumer
import sys
from flaskApi import db
from flaskApi.message import Message


def listMessages(topic):
    apiconsumer = KafkaConsumer(topic)
    list = []
    print("list messages running")

    for msg in apiconsumer:
        msgDict = {
            'body' : str(msg)
            }
        writeToDb(msgDict)

def writeToDb(data):
    print("Wrote {} to db".format(data))
    msg = Message()
    msg.from_dict(data)
    db.session.add(msg)
    db.session.commit()
