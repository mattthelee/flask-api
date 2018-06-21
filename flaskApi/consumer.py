from kafka import KafkaConsumer
import sys


def listMessages(topic):
    apiconsumer = KafkaConsumer(topic)
    
    list = []
    print("list messages running")

    for msg in apiconsumer:
        yield msg
