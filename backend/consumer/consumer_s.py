from kafka import KafkaProducer, KafkaConsumer, TopicPartition
import json
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from avisos_db_fake import JSON_AVISOS

TOPIC="avisos"

# To consume latest messages and auto-commit offsets
consumer = KafkaConsumer(bootstrap_servers=['localhost:9092'],
                        value_deserializer=lambda m: m.decode('utf-8'),
                        auto_offset_reset='earliest')


global RETORNO_PARA_API
RETORNO_PARA_API = JSON_AVISOS


import json

def escrever_jsons_em_arquivo(lista_jsons, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo:
        for json_objeto in lista_jsons:
            json.dump(json_objeto, arquivo)
            arquivo.write('\n')

def return_avisos():
    return RETORNO_PARA_API

def change_retorno_para_api(message, type):
    for message in messages:
        state = message.key.decode('utf-8')
        value = message.value
        for i,codes in enumerate(RETORNO_PARA_API):
            if(codes["code"] == state):
                if type != "change":
                    RETORNO_PARA_API[i]["avisos"][type] = value == "true"
                else:
                    RETORNO_PARA_API[i]["avisos"][type] = int(value)
                escrever_jsons_em_arquivo(RETORNO_PARA_API,'retorno_api.json')

consumer.subscribe(['heat','rain','change'])

if __name__ == "__main__":
    while True:
        # poll messages each certain ms
        raw_messages = consumer.poll(
            timeout_ms=5000, max_records=81
        )
        # for each messages batch
        for topic_partition, messages in raw_messages.items():
            change_retorno_para_api(messages,topic_partition.topic)