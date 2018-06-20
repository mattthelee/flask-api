from kafka import KafkaConsumer
import sys


def listAll(topic):
    apiconsumer = KafkaConsumer(topic)
    list = []
    print("list all running", file=sys.stderr)

    for msg in apiconsumer
        yield msg
