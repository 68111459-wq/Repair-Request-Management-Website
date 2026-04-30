from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from auth_utils import create_access_token, decode_access_token, hash_password, verify_password
from database import SessionLocal
from models import User
from schemas.user import TokenResponse, UserCreate, UserLogin, UserResponse

router = APIRouter(
    prefix="/api/v1/auth",
    tags=["Auth"]
)

security = HTTPBearer()


@router.post("/register", response_model=UserResponse)
def register(data: UserCreate):
    db: Session = SessionLocal()
    try:
        existing_user = db.query(User).filter(User.email == data.email).first()

        if existing_user:
            raise HTTPException(status_code=400, detail="Email already exists")

        if data.role not in ["user", "admin"]:
            raise HTTPException(status_code=400, detail="Role must be user or admin")

        new_user = User(
            username=data.username,
            email=data.email,
            hashed_password=hash_password(data.password),
            role=data.role
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return new_user

    finally:
        db.close()


@router.post("/login", response_model=TokenResponse)
def login(data: UserLogin):
    db: Session = SessionLocal()
    try:
        user = db.query(User).filter(User.email == data.email).first()

        if not user:
            raise HTTPException(status_code=401, detail="Invalid email or password")

        if not verify_password(data.password, user.hashed_password):
            raise HTTPException(status_code=401, detail="Invalid email or password")

        token = create_access_token({
            "user_id": user.id,
            "sub": user.email,
            "role": user.role
        })

        return {
            "access_token": token,
            "token_type": "bearer"
        }

    finally:
        db.close()


@router.get("/me", response_model=UserResponse)
def get_me(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    payload = decode_access_token(token)

    user_id = payload.get("user_id")

    db: Session = SessionLocal()
    try:
        user = db.get(User, user_id)

        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        return user

    finally:
        db.close()