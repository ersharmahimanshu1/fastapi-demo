from fastapi import FastAPI

app = FastAPI()


@app.get("/hello")
async def root():
    return {"message": "Hello World"}


@app.get("/bye")
async def root():
    return {"message": "bye"}


# http://127.0.0.1:8000 