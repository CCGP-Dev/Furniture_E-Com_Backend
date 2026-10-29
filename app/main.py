from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from app.db import  init_model

from fastapi import FastAPI
from app.routers import categories, orders, products , auth
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

# API Prefix
API_PREFIX = "/api/v1"

# Register routers
app.include_router(
    auth.router,
    prefix=f"{API_PREFIX}/auth",
    tags=["Authentication"],
)

app.include_router(
    products.router,
    prefix=f"{API_PREFIX}/products"
)

app.include_router(
    categories.router,
    prefix="/api/v1/categories",
    tags=["Categories"],
)

app.include_router(
    orders.router,
    prefix="/api/v1/orders",
    tags=["Orders"],
)

@app.get("/")
def home():
    return {"message": "API Running"}
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)