# Repair Request Management System

ระบบแจ้งซ่อมอุปกรณ์ภายในองค์กร พัฒนาด้วย FastAPI โดยมีระบบ Authentication ด้วย JWT และมี Admin สำหรับจัดการข้อมูล

---

## Features

- Login ด้วย JWT
- แยกสิทธิ์ Admin / User
- Admin Dashboard
- จัดการหมวดหมู่อุปกรณ์
- สร้างรายการแจ้งซ่อม
- ดูรายการแจ้งซ่อม
- เปลี่ยนสถานะงานซ่อม
- Unit Testing ด้วย Pytest

---

## Tech Stack

- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- PyJWT
- Passlib
- Pytest

---

## Quick Start for Instructor

สำหรับการตรวจงาน สามารถรันระบบได้โดยไม่ต้องพิมพ์คำสั่งเอง

### Run Application

ดับเบิลคลิกไฟล์:

```txt
start.bat
```

ระบบจะติดตั้ง dependencies, สร้างข้อมูลตัวอย่าง และเปิด Swagger API Docs ให้อัตโนมัติ

### Run Unit Tests

ดับเบิลคลิกไฟล์:

```txt
run_tests.bat
```

---

## URL

Local API:

```txt
http://localhost:8000
```

Swagger API Docs:

```txt
http://localhost:8000/docs
```

---

## Default Accounts

### Admin Account

Email: admin@test.com  
Password: 1234

### User Account

Email: user@test.com  
Password: 1234

---

## How to Run Manually

เปิด Terminal ที่โฟลเดอร์ `repair-request-system` แล้วรันคำสั่ง:

```bash
python -m venv venv
venv\Scripts\activate
python -m pip install -r requirements.txt
python seed.py
python -m uvicorn main:app --reload
```

จากนั้นเปิด:

```txt
http://localhost:8000/docs
```

---

## How to Login and Use JWT Token

1. เข้า Swagger API Docs
2. ไปที่ `POST /api/v1/auth/login`
3. กด `Try it out`
4. ใส่ข้อมูล Login

```json
{
  "email": "admin@test.com",
  "password": "1234"
}
```

5. กด `Execute`
6. Copy ค่า `access_token`
7. กดปุ่ม `Authorize`
8. วาง token ลงในช่อง Authorization
9. กด `Authorize` แล้วกด `Close`

หลังจาก Authorize แล้ว สามารถเรียก API ที่ต้อง Login หรือ API ที่ต้องใช้สิทธิ์ Admin ได้

---

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

---

## API Endpoints

### Auth

```txt
POST /api/v1/auth/register
POST /api/v1/auth/login
GET  /api/v1/auth/me
```

### Categories

```txt
GET    /api/v1/categories/
POST   /api/v1/categories/
GET    /api/v1/categories/{category_id}
PUT    /api/v1/categories/{category_id}
DELETE /api/v1/categories/{category_id}
```

### Repair Requests

```txt
GET    /api/v1/repair-requests/
POST   /api/v1/repair-requests/
GET    /api/v1/repair-requests/{request_id}
PUT    /api/v1/repair-requests/{request_id}
DELETE /api/v1/repair-requests/{request_id}
PATCH  /api/v1/repair-requests/{request_id}/status
```

### Admin

```txt
GET /api/v1/admin/dashboard
```

---

## Example Request

### Create Category

```json
{
  "name": "Network",
  "description": "ระบบอินเทอร์เน็ตและเครือข่าย"
}
```

### Create Repair Request

```json
{
  "title": "อินเทอร์เน็ตใช้งานไม่ได้",
  "description": "คอมพิวเตอร์ในห้อง Lab ต่ออินเทอร์เน็ตไม่ได้",
  "location": "Lab 302",
  "priority": "high",
  "category_id": 1
}
```

### Update Repair Status

```json
{
  "new_status": "repairing",
  "note": "เจ้าหน้าที่รับเรื่องและกำลังตรวจสอบ"
}
```

---

## Run Unit Test

```bash
python -m pytest -v
```

Expected result:

```txt
3 passed
```

---

## Project Structure

```txt
repair-request-system/
├── api/
├── schemas/
├── tests/
├── docs/
│   ├── user-guide.md
│   ├── usecase-diagram.png
│   └── system-architecture.png
├── auth_dependencies.py
├── auth_utils.py
├── database.py
├── main.py
├── models.py
├── requirements.txt
├── README.md
├── seed.py
├── start.bat
├── run_tests.bat
├── .gitignore
└── repair_system.sqlite3
```
---

## Summary

ระบบ Repair Request Management System มีการยืนยันตัวตนด้วย JWT แยกสิทธิ์ Admin และ User โดย Admin สามารถจัดการหมวดหมู่อุปกรณ์ เปลี่ยนสถานะงานซ่อม และดู Dashboard สรุปข้อมูลระบบได้ ส่วน User สามารถสร้างรายการแจ้งซ่อมและดูรายการของตัวเองได้ ระบบใช้ SQLite เป็นฐานข้อมูล และมี Unit Test สำหรับตรวจสอบการทำงานของ API