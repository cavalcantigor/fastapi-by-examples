from typing import List
from fastapi import (FastAPI, Query)
import uvicorn


app = FastAPI()


@app.get("/")
async def hello_world():
    return {"Hello": "World"}


@app.get("/hello")
async def hello_multiple_guest(q: List[str] = Query(None)):
    return {"Hello": ' '.join(q)}


@app.get("/hello/validate")
async def hello_validated_guest(q: str = Query("Guest", max_length=10)):
    return {"Hello": ' '.join(q)}


@app.get("/hello/{name}")
async def read_item(name):
    return {"Hello": name}

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
