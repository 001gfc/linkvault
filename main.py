from fastapi import FastAPI

app = FastAPI(title="linkvault")


@app.get("/health")
def health():
    return {"status": "ok"}