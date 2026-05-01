import os
import shutil
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

BASE_DIR = Path(__file__).resolve().parent
LOCAL_DB_PATH = BASE_DIR / "repair_system.sqlite3"

if os.environ.get("VERCEL"):
    VERCEL_DB_PATH = Path("/tmp/repair_system.sqlite3")
    if LOCAL_DB_PATH.exists() and not VERCEL_DB_PATH.exists():
        shutil.copyfile(LOCAL_DB_PATH, VERCEL_DB_PATH)
    DATABASE_URL = f"sqlite:///{VERCEL_DB_PATH}"
else:
    DATABASE_URL = f"sqlite:///{LOCAL_DB_PATH}"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    expire_on_commit=False
)

Base = declarative_base()
