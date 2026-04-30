from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from auth_dependencies import require_admin
from database import SessionLocal
from models import EquipmentCategory, RepairRequest, User

router = APIRouter(
    prefix="/api/v1/admin",
    tags=["Admin"]
)


@router.get("/dashboard")
def admin_dashboard(admin: User = Depends(require_admin)):
    db: Session = SessionLocal()
    try:
        total_users = db.query(User).count()
        total_categories = db.query(EquipmentCategory).count()
        total_requests = db.query(RepairRequest).count()

        pending_requests = db.query(RepairRequest).filter(
            RepairRequest.status == "pending"
        ).count()

        repairing_requests = db.query(RepairRequest).filter(
            RepairRequest.status == "repairing"
        ).count()

        completed_requests = db.query(RepairRequest).filter(
            RepairRequest.status == "completed"
        ).count()

        cancelled_requests = db.query(RepairRequest).filter(
            RepairRequest.status == "cancelled"
        ).count()

        return {
            "total_users": total_users,
            "total_categories": total_categories,
            "total_requests": total_requests,
            "pending_requests": pending_requests,
            "repairing_requests": repairing_requests,
            "completed_requests": completed_requests,
            "cancelled_requests": cancelled_requests
        }

    finally:
        db.close()