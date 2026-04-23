from fastapi import FastAPI

app = FastAPI()


@app.get("/info")
def get_info():
    return {"service": "lobster-skills-test", "version": "v1.0.0", "env": "test"}
