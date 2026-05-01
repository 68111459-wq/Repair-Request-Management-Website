from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"

app = FastAPI(title="Repair Request System")

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


@app.get("/")
def home():
    return FileResponse(STATIC_DIR / "index.html")


@app.get("/api/health")
def health_check():
    return {
        "status": "ok",
        "message": "FastAPI backend is running"
    }


@app.get("/api/repairs")
def get_repairs():
    return [
        {
            "id": 1,
            "title": "Air conditioner broken",
            "status": "pending"
        },
        {
            "id": 2,
            "title": "Computer cannot turn on",
            "status": "done"
        }
    ]