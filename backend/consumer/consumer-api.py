from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from consumer_p import get_last_offset
#from consumer.consumer_s import consumer_s

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*']
)

@app.get("/clima")
async def GET_clima():
    # item = {
    #     "list": [
    #         {"location": "Rio Branco", "code": "BR-AC", "data": {"temperature": 30.1, "precipitation": 39}}, 
    #         {"location": "Maceio", "code": "BR-AL", "data": {"temperature": 28.5, "precipitation": 30}}, 
    #         {"location": "Manaus", "code": "BR-AM", "data": {"temperature": 29.4, "precipitation": 77}}
    #     ]
    # }
    item = get_last_offset()
    print("ITEM RECEBIDO", item)
    json_compatible_item_data = jsonable_encoder(item)
    return JSONResponse(content=json_compatible_item_data)

if __name__ == "__main__":
    uvicorn.run(app, port=30000)