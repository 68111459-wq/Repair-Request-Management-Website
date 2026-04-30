from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from auth_dependencies import require_admin
from database import SessionLocal
from models import EquipmentCategory
from schemas.category import CategoryCreate, CategoryResponse, CategoryUpdate

router = APIRouter(
    prefix="/api/v1/categories",
    tags=["Categories"]
)


@router.get("/", response_model=list[CategoryResponse])
def list_categories():
    db: Session = SessionLocal()
    try:
        categories = db.query(EquipmentCategory).all()
        return categories
    finally:
        db.close()


@router.post("/", response_model=CategoryResponse)
def create_category(
    category: CategoryCreate,
    admin=Depends(require_admin)
):
    db: Session = SessionLocal()
    try:
        new_category = EquipmentCategory(
            name=category.name,
            description=category.description
        )

        db.add(new_category)
        db.commit()
        db.refresh(new_category)

        return new_category
    finally:
        db.close()


@router.get("/{category_id}", response_model=CategoryResponse)
def get_category(category_id: int):
    db: Session = SessionLocal()
    try:
        category = db.get(EquipmentCategory, category_id)

        if not category:
            raise HTTPException(status_code=404, detail="Category not found")

        return category
    finally:
        db.close()


@router.put("/{category_id}", response_model=CategoryResponse)
def update_category(
    category_id: int,
    category_data: CategoryUpdate,
    admin=Depends(require_admin)
):
    db: Session = SessionLocal()
    try:
        category = db.get(EquipmentCategory, category_id)

        if not category:
            raise HTTPException(status_code=404, detail="Category not found")

        category.name = category_data.name
        category.description = category_data.description

        db.commit()
        db.refresh(category)

        return category
    finally:
        db.close()


@router.delete("/{category_id}")
def delete_category(
    category_id: int,
    admin=Depends(require_admin)
):
    db: Session = SessionLocal()
    try:
        category = db.get(EquipmentCategory, category_id)

        if not category:
            raise HTTPException(status_code=404, detail="Category not found")

        db.delete(category)
        db.commit()

        return {"message": "Category deleted successfully"}
    finally:
        db.close()