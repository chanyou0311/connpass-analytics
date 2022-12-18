import datetime
import os

from fastapi import FastAPI, Body
import httpx


app = FastAPI()


@app.get("/")
async def root():
    return {"status": "ok"}


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/run")
async def run(keyword: str = Body()):
    now = datetime.datetime.now()
    url = "https://connpass.com/api/v1/event/"
    transport = httpx.HTTPTransport(retries=5)
    client = httpx.Client(transport=transport)
    response = client.get(url, params={"keyword": keyword})

    date = now.date().isoformat()
    time = now.strftime("%H%M")
    path = f"/datalake/connpass/events/{keyword}/events_{date}_{time}.json"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, mode="wb") as f:
        f.write(response.content)

    return {"status": "success"}
