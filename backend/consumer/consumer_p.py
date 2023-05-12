from kafka import KafkaProducer, KafkaConsumer, TopicPartition
import json
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

TOPIC="clima"

# To consume latest messages and auto-commit offsets
consumer = KafkaConsumer(bootstrap_servers=['localhost:9092'],
                        value_deserializer=lambda m: json.loads(m.decode('utf-8')),
                        auto_offset_reset='earliest')

offsets = []
# SIMPLE CONSUMER -----------------------------------
def get_last_offset():

    # # print(consumer.assignment())
    
    # tp = TopicPartition(TOPIC, 0)
    # #consumer.assign([tp])

    # end_offsets = consumer.end_offsets([tp])

    # last_offset = end_offsets[tp]

    # print(last_offset)

    # # print(item)
    # # print(type(item))
    # # return item
    
    # # consumer.seek(tp, last_offset-1)
    
    # item = consumer.poll()
    # print(item)
    
    consumer.subscribe(TOPIC)
    partition = TopicPartition(TOPIC, 0)
    end_offset = consumer.end_offsets([partition])
    consumer.seek(partition,list(end_offset.values())[0]-1)

    for m in consumer:
        item = m
        offsets.append(item.value)
        break

    return item.value

# COMPLEX PRODUCER ------------------------------
def on_send_success(record_metadata):
    print(f"Evento enviado com sucesso no topico {record_metadata.topic} na partição {record_metadata.partition} com offset {record_metadata.offset}")

def on_send_error(excp):
    print(excp)
    print("ERROR SENDING TO KAFKA")

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],value_serializer=lambda m: json.dumps(m).encode('utf-8'))

# # def save_last_offsets():
# #     if(len(offsets) > 5):


# #     return item.value