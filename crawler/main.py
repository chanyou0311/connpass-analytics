import datetime
import json
import os

from fastapi import FastAPI, Body
import httpx

JST = datetime.timezone(datetime.timedelta(hours=+9), "JST")
app = FastAPI()


@app.get("/")
async def root():
    return {"status": "ok"}


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/run")
async def run(keyword: str = Body()):
    # Get current datetime
    now = datetime.datetime.now(JST)
    now_str = now.strftime("%FT%T%z")
    fetched_at = now_str[:-2] + ":" + now_str[-2:]

    # Fetch events
    url = "https://connpass.com/api/v1/event/"
    transport = httpx.HTTPTransport(retries=5)
    client = httpx.Client(transport=transport)
    response = client.get(url, params={"keyword": keyword})

    # Add fetched_at column
    data = response.json()
    for event in data["events"]:
        event["fetched_at"] = fetched_at

    # Write to file
    date = now.date().isoformat()
    time = now.strftime("%H%M")
    path = f"/datalake/connpass/events/{keyword}/events_{date}_{time}.json"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, mode="w") as f:
        json.dump(data, f, separators=(",", ":"))

    return {"status": "success"}
