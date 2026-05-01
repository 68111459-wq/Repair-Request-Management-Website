from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from api.admin_api import router as admin_router
from api.auth_api import router as auth_router
from api.categories_api import router as categories_router
from api.repair_requests_api import router as repair_requests_router
from database import Base, engine

BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"

app = FastAPI(title="Repair Request System")

Base.metadata.create_all(bind=engine)

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
app.include_router(auth_router)
app.include_router(categories_router)
app.include_router(repair_requests_router)
app.include_router(admin_router)


@app.get("/")
def home():
    return FileResponse(STATIC_DIR / "index.html")


@app.get("/web")
def web():
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
