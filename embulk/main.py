import os
import subprocess

from fastapi import FastAPI, Body, status
from fastapi.responses import JSONResponse



app = FastAPI()


@app.get("/")
async def root():
    return {"status": "ok"}


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/run")
async def run(keyword: str = Body()):
    result = subprocess.run(["bash", "run.sh", keyword], capture_output=True)
    content= {
        "args": result.args,
        "stdout": str(result.stdout),
        "stderr": str(result.stderr),
    }

    try:
        result.check_returncode()
    except subprocess.CalledProcessError:
        return JSONResponse(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            content=content,
        )
    return content
