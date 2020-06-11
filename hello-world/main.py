from typing import List
from fastapi import (FastAPI, Query, status)
from pydantic import BaseModel
import uvicorn


app = FastAPI()


class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None


@app.get("/", status_code=200)
async def hello_world():
    return {"Hello": "World"}


@app.get("/hello", status_code=status.HTTP_200_OK)
async def hello_multiple_guest(q: List[str] = Query(None)):
    return {"Hello": ' '.join(q)}


@app.get("/hello/validate", status_code=status.HTTP_200_OK)
async def hello_validated_guest(q: str = Query("Guest", max_length=10)):
    return {"Hello": ' '.join(q)}


@app.get("/hello/{name}", status_code=status.HTTP_200_OK)
async def read_item(name):
    return {"Hello": name}


@app.post("/item/")
async def create_item(item: Item):
    return item

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
