from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class RepairRequestCreate(BaseModel):
    title: str
    description: str
    location: str
    priority: str = "medium"
    category_id: Optional[int] = None


class RepairRequestUpdate(BaseModel):
    title: str
    description: str
    location: str
    priority: str = "medium"
    category_id: Optional[int] = None


class RepairStatusUpdate(BaseModel):
    new_status: str
    note: Optional[str] = None


class RepairRequestResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    description: str
    location: str
    priority: str
    status: str
    user_id: Optional[int] = None
    category_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime
    completed_at: Optional[datetime] = None