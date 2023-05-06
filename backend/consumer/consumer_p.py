from kafka import KafkaProducer, KafkaConsumer
import json
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

# To consume latest messages and auto-commit offsets
consumer = KafkaConsumer('clima',
                        bootstrap_servers=['localhost:9092'],
                        value_deserializer=lambda m: json.loads(m.decode('utf-8')))

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],value_serializer=lambda m: json.dumps(m).encode('utf-8'))

@app.get("/clima")
async def root():
    print(item)

    json_compatible_item_data = jsonable_encoder(item)

    print(json_compatible_item_data)

    return JSONResponse(content=json_compatible_item_data)

item = {
    "list": [
        {"location": "Rio Branco", "code": "BR-AC", "data": {"temperature": 30.1, "precipitation": 39}}, 
        {"location": "Maceio", "code": "BR-AL", "data": {"temperature": 28.5, "precipitation": 30}}, 
        {"location": "Manaus", "code": "BR-AM", "data": {"temperature": 29.4, "precipitation": 77}}
    ]
}

    # while True:
    #     for msg in consumer:
    #          continue