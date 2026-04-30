# Repair Request Management System

ระบบแจ้งซ่อมอุปกรณ์ภายในองค์กร พัฒนาด้วย FastAPI โดยมีระบบ Authentication ด้วย JWT และมี Admin สำหรับจัดการข้อมูล

## Features

- Login ด้วย JWT
- แยกสิทธิ์ Admin / User
- Admin Dashboard
- จัดการหมวดหมู่อุปกรณ์
- สร้างรายการแจ้งซ่อม
- ดูรายการแจ้งซ่อม
- เปลี่ยนสถานะงานซ่อม
- Unit Testing ด้วย Pytest

## Tech Stack

- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- PyJWT
- Passlib
- Pytest

## Database Models

### User

- id
- username
- email
- hashed_password
- role
- created_at

### EquipmentCategory

- id
- name
- description

### RepairRequest

- id
- title
- description
- location
- priority
- status
- user_id
- category_id
- created_at
- updated_at
- completed_at

### RepairStatusLog

- id
- repair_request_id
- changed_by
- old_status
- new_status
- note
- created_at

## API Endpoints

### Auth

- POST /api/v1/auth/register
- POST /api/v1/auth/login
- GET /api/v1/auth/me

### Categories

- GET /api/v1/categories/
- POST /api/v1/categories/
- GET /api/v1/categories/{category_id}
- PUT /api/v1/categories/{category_id}
- DELETE /api/v1/categories/{category_id}

### Repair Requests

- GET /api/v1/repair-requests/
- POST /api/v1/repair-requests/
- GET /api/v1/repair-requests/{request_id}
- PUT /api/v1/repair-requests/{request_id}
- DELETE /api/v1/repair-requests/{request_id}
- PATCH /api/v1/repair-requests/{request_id}/status

### Admin

- GET /api/v1/admin/dashboard

## How to Run

```bash
python -m venv venv
venv\Scripts\activate
python -m pip install -r requirements.txt
python -m uvicorn main:app --reload

http://localhost:8000
http://localhost:8000/docs

## Run Unit Test
python -m pytest -v

POST /api/v1/auth/login
{
  "email": "admin@test.com",
  "password": "1234"
}



## Example Request
  ##Create Category
  {
    "name": "Network",
    "description": "ระบบอินเทอร์เน็ตและเครือข่าย"
  }

  ## Create Repair Request
  {
  "title": "อินเทอร์เน็ตใช้งานไม่ได้",
  "description": "คอมพิวเตอร์ในห้อง Lab ต่ออินเทอร์เน็ตไม่ได้",
  "location": "Lab 302",
  "priority": "high",
  "category_id": 1
}

## Update Repair Status
{
  "new_status": "repairing",
  "note": "เจ้าหน้าที่รับเรื่องและกำลังตรวจสอบ"
}

## Run Unit Test
python -m pytest -v 
-3 passed