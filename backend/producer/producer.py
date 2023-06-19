from kafka import KafkaProducer
from kafka.errors import KafkaError
import json
import time
import OpenMeteoClient as omc

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],value_serializer=lambda m: json.dumps(m).encode('utf-8'))
producerString = KafkaProducer(bootstrap_servers=['localhost:9092'])

def on_send_success(record_metadata):
    print(f"Evento enviado com sucesso no topico {record_metadata.topic} na partição {record_metadata.partition} com offset {record_metadata.offset}")

def on_send_error(excp):
    print(excp)
    print("ERROR SENDING TO KAFKA")


client = omc.OpenMeteo()

# Main loop
while True:
    # Get Info on OpenMeteo
    data = client.get_locations_weather()

    for location in data['data']:
        producerString.send('temperature',
                            value=bytes(str(location['data']['temperature']),encoding="utf-8"),
                            key=bytes(location['code'], encoding='utf-8')).add_callback(on_send_success).add_errback(on_send_error)

        producerString.send('wind',
                            value=bytes(str(location['data']['windspeed']),encoding="utf-8"),
                            key=bytes(location['code'], encoding='utf-8')).add_callback(on_send_success).add_errback(on_send_error)

        producerString.send('uv',
                            value=bytes(str(location['data']['uv_index_max']),encoding="utf-8"),
                            key=bytes(location['code'], encoding='utf-8')).add_callback(on_send_success).add_errback(on_send_error)

        producerString.send('precipitation',
                            value=bytes(str(location['data']['precipitation']),encoding="utf-8"),
                            key=bytes(location['code'], encoding='utf-8')).add_callback(on_send_success).add_errback(on_send_error)

    producer.send('clima', data).add_callback(on_send_success).add_errback(on_send_error)

    #Sleep
    time.sleep(10000)