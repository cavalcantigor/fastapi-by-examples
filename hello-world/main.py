from fastapi import FastAPI
import uvicorn


app = FastAPI()


@app.get("/")
def hello_world():
    return {"Hello": "World"}


@app.get("/hello")
def hello_guest(q: str = "Guest"):
    return {"Hello": q}


@app.get("/hello/{name}")
async def read_item(name):
    return {"Hello": name}

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
