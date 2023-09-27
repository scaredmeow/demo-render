from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/poc/merchant/generation")
async def poc_merchant_generation(name: str = "Name"):
    return {"poc_merchant_generation": name}


@app.get("/poc/merchant/{merchant_id}")
async def poc_merchant(merchant_id: int):
    return {"poc_merchant_generation": merchant_id}
