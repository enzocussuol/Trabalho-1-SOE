from kafka import KafkaProducer, KafkaConsumer, TopicPartition
import json
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

TOPIC="avisos"

# To consume latest messages and auto-commit offsets
consumer = KafkaConsumer(bootstrap_servers=['localhost:9092'],
                        value_deserializer=lambda m: json.loads(m.decode('utf-8')),
                        auto_offset_reset='earliest')


def get_last_offset_secundary():
    
    consumer.subscribe(TOPIC)
    partition = TopicPartition(TOPIC, 0)
    end_offset = consumer.end_offsets([partition])
    consumer.seek(partition,list(end_offset.values())[0]-1)

    for m in consumer:
        item = m
        break

    return item.value

