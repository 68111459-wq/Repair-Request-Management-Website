from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    role = Column(String(20), default="user")
    created_at = Column(DateTime, default=datetime.now)

    repair_requests = relationship("RepairRequest", back_populates="user")


class EquipmentCategory(Base):
    __tablename__ = "equipment_categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)

    repair_requests = relationship("RepairRequest", back_populates="category")


class RepairRequest(Base):
    __tablename__ = "repair_requests"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=False)
    location = Column(String(200), nullable=False)
    priority = Column(String(20), default="medium")
    status = Column(String(30), default="pending")

    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    category_id = Column(Integer, ForeignKey("equipment_categories.id"), nullable=True)

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)
    completed_at = Column(DateTime, nullable=True)

    user = relationship("User", back_populates="repair_requests")
    category = relationship("EquipmentCategory", back_populates="repair_requests")
    status_logs = relationship("RepairStatusLog", back_populates="repair_request")


class RepairStatusLog(Base):
    __tablename__ = "repair_status_logs"

    id = Column(Integer, primary_key=True, index=True)

    repair_request_id = Column(Integer, ForeignKey("repair_requests.id"))
    changed_by = Column(Integer, ForeignKey("users.id"), nullable=True)

    old_status = Column(String(30), nullable=True)
    new_status = Column(String(30), nullable=False)
    note = Column(Text, nullable=True)

    created_at = Column(DateTime, default=datetime.now)

    repair_request = relationship("RepairRequest", back_populates="status_logs")