from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import subprocess

app = FastAPI()

app.add_middleware(
   CORSMiddleware,
   allow_origins=['*']
)


if __name__ == "__main__":
   uvicorn.run(app, port=30000)