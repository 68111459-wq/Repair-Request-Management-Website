from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from auth_dependencies import get_current_user, require_admin
from database import SessionLocal
from models import EquipmentCategory, RepairRequest, RepairStatusLog, User
from schemas.repair_request import (
    RepairRequestCreate,
    RepairRequestResponse,
    RepairRequestUpdate,
    RepairStatusUpdate,
)

router = APIRouter(
    prefix="/api/v1/repair-requests",
    tags=["Repair Requests"]
)


VALID_STATUS = {"pending", "accepted", "repairing", "completed", "cancelled"}
VALID_PRIORITY = {"low", "medium", "high"}


@router.get("/", response_model=list[RepairRequestResponse])
def list_repair_requests(current_user: User = Depends(get_current_user)):
    db: Session = SessionLocal()
    try:
        if current_user.role == "admin":
            repair_requests = db.query(RepairRequest).all()
        else:
            repair_requests = db.query(RepairRequest).filter(
                RepairRequest.user_id == current_user.id
            ).all()

        return repair_requests
    finally:
        db.close()


@router.post("/", response_model=RepairRequestResponse)
def create_repair_request(
    data: RepairRequestCreate,
    current_user: User = Depends(get_current_user)
):
    db: Session = SessionLocal()
    try:
        priority = data.priority.lower()

        if priority not in VALID_PRIORITY:
            raise HTTPException(
                status_code=400,
                detail="Priority must be low, medium, or high"
            )

        if data.category_id:
            category = db.get(EquipmentCategory, data.category_id)
            if not category:
                raise HTTPException(status_code=404, detail="Category not found")

        new_request = RepairRequest(
            title=data.title,
            description=data.description,
            location=data.location,
            priority=priority,
            status="pending",
            category_id=data.category_id,
            user_id=current_user.id,
        )

        db.add(new_request)
        db.commit()
        db.refresh(new_request)

        log = RepairStatusLog(
            repair_request_id=new_request.id,
            changed_by=current_user.id,
            old_status=None,
            new_status="pending",
            note="Repair request created",
        )

        db.add(log)
        db.commit()

        return new_request

    finally:
        db.close()


@router.get("/{request_id}", response_model=RepairRequestResponse)
def get_repair_request(
    request_id: int,
    current_user: User = Depends(get_current_user)
):
    db: Session = SessionLocal()
    try:
        repair_request = db.get(RepairRequest, request_id)

        if not repair_request:
            raise HTTPException(status_code=404, detail="Repair request not found")

        if current_user.role != "admin" and repair_request.user_id != current_user.id:
            raise HTTPException(
                status_code=403,
                detail="No permission to view this request"
            )

        return repair_request
    finally:
        db.close()


@router.put("/{request_id}", response_model=RepairRequestResponse)
def update_repair_request(
    request_id: int,
    data: RepairRequestUpdate,
    current_user: User = Depends(get_current_user)
):
    db: Session = SessionLocal()
    try:
        repair_request = db.get(RepairRequest, request_id)

        if not repair_request:
            raise HTTPException(status_code=404, detail="Repair request not found")

        if current_user.role != "admin" and repair_request.user_id != current_user.id:
            raise HTTPException(
                status_code=403,
                detail="No permission to update this request"
            )

        priority = data.priority.lower()

        if priority not in VALID_PRIORITY:
            raise HTTPException(
                status_code=400,
                detail="Priority must be low, medium, or high"
            )

        if data.category_id:
            category = db.get(EquipmentCategory, data.category_id)
            if not category:
                raise HTTPException(status_code=404, detail="Category not found")

        repair_request.title = data.title
        repair_request.description = data.description
        repair_request.location = data.location
        repair_request.priority = priority
        repair_request.category_id = data.category_id
        repair_request.updated_at = datetime.now()

        db.commit()
        db.refresh(repair_request)

        return repair_request

    finally:
        db.close()


@router.delete("/{request_id}")
def delete_repair_request(
    request_id: int,
    admin: User = Depends(require_admin)
):
    db: Session = SessionLocal()
    try:
        repair_request = db.get(RepairRequest, request_id)

        if not repair_request:
            raise HTTPException(status_code=404, detail="Repair request not found")

        db.query(RepairStatusLog).filter(
            RepairStatusLog.repair_request_id == request_id
        ).delete()

        db.delete(repair_request)
        db.commit()

        return {"message": "Repair request deleted successfully"}

    finally:
        db.close()


@router.patch("/{request_id}/status", response_model=RepairRequestResponse)
def update_repair_status(
    request_id: int,
    data: RepairStatusUpdate,
    admin: User = Depends(require_admin)
):
    db: Session = SessionLocal()
    try:
        repair_request = db.get(RepairRequest, request_id)

        if not repair_request:
            raise HTTPException(status_code=404, detail="Repair request not found")

        new_status = data.new_status.lower()

        if new_status not in VALID_STATUS:
            raise HTTPException(
                status_code=400,
                detail="Status must be pending, accepted, repairing, completed, or cancelled"
            )

        old_status = repair_request.status

        repair_request.status = new_status
        repair_request.updated_at = datetime.now()

        if new_status == "completed":
            repair_request.completed_at = datetime.now()

        log = RepairStatusLog(
            repair_request_id=repair_request.id,
            changed_by=admin.id,
            old_status=old_status,
            new_status=new_status,
            note=data.note,
        )

        db.add(log)
        db.commit()
        db.refresh(repair_request)

        return repair_request

    finally:
        db.close()