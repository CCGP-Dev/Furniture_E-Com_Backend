from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from app.db import  init_model

from fastapi.concurrency import run_in_threadpool
from app.db.postgresDB import db_connection
from app.services.cloudinaryService import  upload_product_image

@asynccontextmanager
async def lifespan(app: FastAPI): #start app fast api
    init_model() #call database creation
    yield #shutdown app after the database creation


app = FastAPI(
        title="Furnova E-Commerce  ",
        lifespan=lifespan, #call init model and createtabase models

)


@app.get("/")
def home():
    return {"message": "API Running"}
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)