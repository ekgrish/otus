from fastapi import FastAPI

app = FastAPI()


@app.get("/health/")
async def health():
    return {"status": "OK"}

@app.get("/readiness/")
async def ready():
    return {"status": "OK"}