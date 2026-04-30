from fastapi import FastAPI

import models
from api.admin_api import router as admin_router
from api.auth_api import router as auth_router
from api.categories_api import router as categories_router
from api.repair_requests_api import router as repair_requests_router
from database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Repair Request System")

app.include_router(auth_router)
app.include_router(categories_router)
app.include_router(repair_requests_router)
app.include_router(admin_router)


@app.get("/")
def home():
    return {"message": "Repair Request API is running"}


@app.get("/api/health")
def health_check():
    return {
        "status": "ok",
        "database": "connected"
    }