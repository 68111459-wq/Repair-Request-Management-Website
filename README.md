# Repair Request Management System

ระบบแจ้งซ่อมอุปกรณ์ภายในองค์กร พัฒนาด้วย FastAPI มีระบบ Login ด้วย JWT แยกสิทธิ์ Admin / User และมีหน้าเว็บสำหรับใช้งานระบบ

---

## Features

- Login / Logout ด้วย JWT
- แยกสิทธิ์ Admin และ User
- หน้า Web Application สำหรับใช้งานระบบ
- Swagger API Docs สำหรับทดสอบ API
- Admin Dashboard
- จัดการหมวดหมู่อุปกรณ์
- สร้างรายการแจ้งซ่อม
- ดูรายการแจ้งซ่อม
- เปลี่ยนสถานะงานซ่อม
- ลบรายการแจ้งซ่อม
- Unit Testing ด้วย Pytest
- มี `start.bat` สำหรับรันระบบอัตโนมัติ
- มี `run_tests.bat` สำหรับรัน Unit Test อัตโนมัติ

---

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- PyJWT
- Passlib
- Pytest
- HTML / CSS / JavaScript

---

## URL

### Local Web Application

```txt
http://localhost:8000/web
```

### Swagger API Docs

```txt
http://localhost:8000/docs
```

### Local API

```txt
http://localhost:8000
```

### Production

หลังจาก Deploy แล้ว ให้ใช้ URL ที่ได้จาก Render เช่น:

```txt
https://your-render-url.onrender.com/web
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

## Quick Start for Instructor

สำหรับการตรวจงาน สามารถรันระบบได้โดยไม่ต้องพิมพ์คำสั่งเอง

### Run Application

ดับเบิลคลิกไฟล์:

```txt
start.bat
```

ระบบจะทำงานให้อัตโนมัติ ดังนี้:

```txt
1. สร้าง virtual environment ถ้ายังไม่มี
2. Activate virtual environment
3. ติดตั้ง dependencies จาก requirements.txt
4. สร้างข้อมูลตัวอย่างด้วย seed.py
5. เปิดหน้า Web Application อัตโนมัติ
6. รัน FastAPI server
```

หลังจากรันสำเร็จ ระบบจะเปิดที่:

```txt
http://localhost:8000/web
```

ถ้าต้องการทดสอบ API โดยตรง สามารถเปิด Swagger ได้ที่:

```txt
http://localhost:8000/docs
```

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

จากนั้นเปิดหน้าเว็บ:

```txt
http://localhost:8000/web
```

หรือเปิด Swagger API Docs:

```txt
http://localhost:8000/docs
```

---

## How to Deploy on Render

ตั้งค่า Render Web Service ดังนี้:

### Build Command

```bash
pip install -r requirements.txt
```

### Start Command

```bash
python seed.py && python -m uvicorn main:app --host 0.0.0.0 --port $PORT
```

หลัง Deploy เสร็จ ให้เข้า:

```txt
https://your-render-url.onrender.com/web
```

---

## Web Frontend

ระบบมีหน้าเว็บสำหรับใช้งานที่ `/web`

### ความสามารถของหน้าเว็บ

- Login / Logout
- แสดงข้อมูล Current User
- Admin ดู Dashboard ได้
- Admin จัดการ Category ได้
- Admin ดูรายการแจ้งซ่อมทั้งหมดได้
- Admin เปลี่ยนสถานะงานซ่อมได้
- Admin ลบรายการแจ้งซ่อมได้
- User สร้างรายการแจ้งซ่อมได้
- User ดูรายการแจ้งซ่อมของตัวเองได้
- เมื่อ Logout แล้ว ระบบจะซ่อนข้อมูลที่ต้อง Login

---

## Role Permission

### Guest

ผู้ใช้ที่ยังไม่ได้ Login

```txt
- เห็นหน้า Login
- ไม่เห็น Dashboard
- ไม่เห็น Categories
- ไม่เห็น Repair Requests
- ไม่สามารถสร้างรายการแจ้งซ่อมได้
```

### User

ผู้ใช้ทั่วไป

```txt
- Login ได้
- ดูข้อมูลตัวเองได้
- สร้างรายการแจ้งซ่อมได้
- ดูรายการแจ้งซ่อมของตัวเองได้
- ไม่เห็น Admin Dashboard
- ไม่สามารถจัดการ Category ได้
- ไม่สามารถเปลี่ยนสถานะงานซ่อมได้
```

### Admin

ผู้ดูแลระบบ

```txt
- Login ได้
- ดูข้อมูลตัวเองได้
- ดู Admin Dashboard ได้
- จัดการ Category ได้
- ดูรายการแจ้งซ่อมทั้งหมดได้
- เปลี่ยนสถานะงานซ่อมได้
- ลบรายการแจ้งซ่อมได้
```

---

## How to Login and Use JWT Token in Swagger

1. เข้า Swagger API Docs

```txt
http://localhost:8000/docs
```

2. ไปที่ API

```txt
POST /api/v1/auth/login
```

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
8. วาง Token ในรูปแบบนี้:

```txt
Bearer your_access_token
```

9. กด `Authorize` แล้วกด `Close`

หลังจาก Authorize แล้ว จะสามารถเรียก API ที่ต้อง Login หรือ API ที่ต้องใช้สิทธิ์ Admin ได้

---

## Database Models

### User

```txt
id
username
email
hashed_password
role
created_at
```

### EquipmentCategory

```txt
id
name
description
```

### RepairRequest

```txt
id
title
description
location
priority
status
user_id
category_id
created_at
updated_at
completed_at
```

### RepairStatusLog

```txt
id
repair_request_id
changed_by
old_status
new_status
note
created_at
```

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

สถานะที่ใช้ได้:

```txt
pending
accepted
repairing
completed
cancelled
```

---

## Run Unit Test

### Run with file

ดับเบิลคลิกไฟล์:

```txt
run_tests.bat
```

### Run with command

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
├── static/
│   └── index.html
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



## Git Repository

Source code is managed using Git.

GitHub Repository:

```txt
https://github.com/wachirawichsuchaiyasit/repair-request-system
```

---

## Summary

Repair Request Management System เป็นระบบแจ้งซ่อมอุปกรณ์ภายในองค์กร มีระบบยืนยันตัวตนด้วย JWT แยกสิทธิ์ Admin และ User โดย Admin สามารถจัดการหมวดหมู่ ดู Dashboard เปลี่ยนสถานะงานซ่อม และลบรายการแจ้งซ่อมได้ ส่วน User สามารถสร้างรายการแจ้งซ่อมและดูรายการของตัวเองได้ ระบบมีหน้าเว็บสำหรับใช้งานจริง มี Swagger สำหรับทดสอบ API และมี Unit Test สำหรับตรวจสอบการทำงานของระบบ
