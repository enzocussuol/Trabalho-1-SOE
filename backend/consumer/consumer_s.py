from kafka import KafkaConsumer
import json

# To consume latest messages and auto-commit offsets
consumer = KafkaConsumer('avisos',
                         bootstrap_servers=['localhost:9092'],
                         value_deserializer=lambda m: json.loads(m.decode('utf-8')))