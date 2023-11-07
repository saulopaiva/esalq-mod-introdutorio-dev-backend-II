from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/test")
async def test(param: str = ""):
    param = param + param
    param = param + param
    return {"message": "Hello World 2: " + param}