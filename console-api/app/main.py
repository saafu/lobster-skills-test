from datetime import datetime, timezone
from fastapi import FastAPI

app = FastAPI()


@app.get("/info")
def get_info():
    return {"service": "lobster-skills-test", "version": "v1.0.0", "env": "test"}


@app.get("/version")
def get_version():
    return {"version": "1.0.0", "env": "test"}


@app.get("/status")
def get_status():
    return {
        "status": "ok",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "agent": "lobster",
    }
