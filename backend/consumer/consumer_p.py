from kafka import KafkaConsumer
import json

# To consume latest messages and auto-commit offsets
consumer = KafkaConsumer('clima',
                         bootstrap_servers=['localhost:9092'],
                         value_deserializer=lambda m: json.loads(m.decode('utf-8')))

while True:
    for msg in consumer:
        print (msg)