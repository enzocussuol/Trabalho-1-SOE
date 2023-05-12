from kafka import KafkaProducer, KafkaConsumer, TopicPartition
import json
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

TOPIC="clima"

# To consume latest messages and auto-commit offsets
consumer = KafkaConsumer(bootstrap_servers=['localhost:9092'],
                        value_deserializer=lambda m: json.loads(m.decode('utf-8')),
                        auto_offset_reset='earliest')

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

    #a k a leen beef patty 
    for m in consumer:
        item = m
        break

    return item.value

# COMPLEX PRODUCER ------------------------------
def on_send_success(record_metadata):
    print(f"Evento enviado com sucesso no topico {record_metadata.topic} na partição {record_metadata.partition} com offset {record_metadata.offset}")

def on_send_error(excp):
    print(excp)
    print("ERROR SENDING TO KAFKA")

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],value_serializer=lambda m: json.dumps(m).encode('utf-8'))

def save_last_offsets():
    offsets = []
    
    partition = TopicPartition(TOPIC, 0)
    end_offset = consumer.end_offsets([partition])
    consumer.seek(partition,list(end_offset.values())[0]-5)

    for i, m in enumerate(consumer):
        offsets.append(m.value)
        if i == 4:
            break
    
    data = []
    info = offsets[-1]["data"]
    info2 = offsets[-2]["data"]
    
    for i in range(len(info)):
        city = info[i]
        city2 = info2[i]

        avisos = {"heat":False, "rain":False, "change":0}
        
        if(city["data"]["temperature"] >= 30 or city["data"]["uv_index_max"] >= 6):
            avisos["heat"] = True
        if(city["data"]["precipitation"] >= 50 and city["data"]["windspeed"] >= 8):
            avisos["rain"] = True
        if(city["data"]["temperature"] - city2["data"]["temperature"] >= 5):
            avisos["change"] = 1
        elif( city["data"]["temperature"] - city2["data"]["temperature"] < -5):
            avisos["change"] = -1
        
        data.append({"code":city["code"], "avisos":avisos}) 

    producer.send('avisos', data).add_callback(on_send_success).add_errback(on_send_error)