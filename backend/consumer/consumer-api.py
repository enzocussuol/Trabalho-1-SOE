from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from consumer_p import *
from consumer_s import return_avisos

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*']
)

@app.get("/clima")
async def GET_clima():
    item = get_last_offset()
    json_compatible_item_data = jsonable_encoder(item)
    return JSONResponse(content=json_compatible_item_data)

def ler_jsons_do_arquivo(nome_arquivo):
    lista_jsons = []
    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            json_objeto = json.loads(linha)
            lista_jsons.append(json_objeto)
    return lista_jsons

@app.get("/avisos")
async def GET_avisos():
    item = ler_jsons_do_arquivo('retorno_api.json')
    
    json_compatible_item_data = jsonable_encoder(item)
    print(item)
    return JSONResponse(content=json_compatible_item_data)

if __name__ == "__main__":
    uvicorn.run(app, port=30000)