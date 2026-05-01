# Repair Request Management System

ระบบแจ้งซ่อมอุปกรณ์ภายในองค์กร พัฒนาด้วย FastAPI, SQLite, JWT และหน้าเว็บ HTML/CSS/JavaScript สำหรับใช้งานจริงผ่านเบราว์เซอร์

ระบบรองรับการแยกสิทธิ์ผู้ใช้เป็น `Admin` และ `User` โดย Admin สามารถจัดการหมวดหมู่อุปกรณ์ ดู Dashboard ดูรายการแจ้งซ่อมทั้งหมด และเปลี่ยนสถานะงานซ่อมได้ ส่วน User สามารถสร้างและดูรายการแจ้งซ่อมของตัวเองได้

---

## ฟีเจอร์ปัจจุบัน

- Login / Logout ด้วย JWT
- แสดงข้อมูลผู้ใช้ที่ Login อยู่
- แยกหน้าจอและสิทธิ์การใช้งานระหว่าง Admin, User และ Guest
- Admin Dashboard แสดงจำนวน Users, Categories และ Repair Requests
- Admin จัดการ Category ได้ครบ: สร้าง, แก้ไข Name/Description, ลบ
- เมื่อลบ Category ระบบจะเคลียร์ `category_id` ของรายการแจ้งซ่อมที่เกี่ยวข้องก่อน เพื่อป้องกันปัญหา foreign key
- User และ Admin สร้าง Repair Request ได้
- User เห็นเฉพาะ Repair Request ของตัวเอง
- Admin เห็น Repair Request ทั้งหมด
- Admin เปลี่ยนสถานะงานซ่อมเป็น `accepted`, `repairing`, `completed` ได้
- Admin ลบ Repair Request ได้
- หน้าเว็บซ่อนเมนูที่ต้อง Login เมื่อยังไม่ได้ Login
- ถ้า token หมดอายุหรือไม่มีสิทธิ์ ระบบจะเคลียร์ session และให้ Login ใหม่
- Swagger Docs สำหรับทดสอบ API
- รองรับการ Deploy บน Vercel ผ่าน `vercel.json`

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
- Vercel Python Runtime

---

## URL สำคัญ

### Local

```txt
http://localhost:8000/web
```

หน้า API Docs:

```txt
http://localhost:8000/docs
```

Health check:

```txt
http://localhost:8000/api/health
```

### Production บน Vercel

หลัง Deploy แล้วให้ใช้ URL ที่ Vercel สร้างให้ เช่น:

```txt
https://your-project.vercel.app/web
```

Swagger Docs บน Production:

```txt
https://your-project.vercel.app/docs
```

---

## บัญชีเริ่มต้น

### Admin

```txt
Email: admin@test.com
Password: 1234
```

### User

```txt
Email: user@test.com
Password: 1234
```

---

## วิธีรันแบบง่าย

ดับเบิลคลิกไฟล์:

```txt
start.bat
```

ไฟล์นี้จะทำงานให้อัตโนมัติ:

1. สร้าง virtual environment ถ้ายังไม่มี
2. Activate virtual environment
3. ติดตั้ง dependencies จาก `requirements.txt`
4. สร้างข้อมูลตัวอย่างด้วย `seed.py`
5. เปิดหน้าเว็บ
6. รัน FastAPI server

เมื่อรันสำเร็จ ให้เข้า:

```txt
http://localhost:8000/web
```

---

## วิธีรันด้วยคำสั่ง

เปิด Terminal ที่โฟลเดอร์โปรเจกต์ แล้วรัน:

```bash
python -m venv venv
venv\Scripts\activate
python -m pip install -r requirements.txt
python seed.py
python -m uvicorn main:app --reload
```

จากนั้นเปิด:

```txt
http://localhost:8000/web
```

---

## วิธีใช้งานหน้าเว็บ

1. เปิด `/web`
2. Login ด้วยบัญชี Admin หรือ User
3. ถ้าเป็น Admin จะเห็น Dashboard, ฟอร์มจัดการ Category และปุ่มเปลี่ยนสถานะ/ลบรายการแจ้งซ่อม
4. ถ้าเป็น User จะเห็นฟอร์มสร้าง Repair Request และรายการของตัวเอง
5. เมื่อ Logout ระบบจะซ่อนข้อมูลที่ต้องใช้สิทธิ์ Login

### การจัดการ Category สำหรับ Admin

- สร้าง Category: ใส่ `Category Name` และ `Description` แล้วกด `Create Category`
- แก้ไข Category: กด `Edit` ในตาราง Category แก้ Name/Description แล้วกด `Save Changes`
- ยกเลิกการแก้ไข: กด `Cancel`
- ลบ Category: กด `Delete` และยืนยันการลบ

---

## สิทธิ์การใช้งาน

### Guest

- เห็นหน้า Login
- ไม่เห็น Dashboard
- ไม่เห็น Categories
- ไม่เห็น Repair Requests
- ไม่สามารถสร้าง Repair Request ได้

### User

- Login ได้
- ดูข้อมูลตัวเองได้
- สร้าง Repair Request ได้
- ดู Repair Request ของตัวเองได้
- ไม่เห็น Admin Dashboard
- ไม่สามารถสร้าง แก้ไข หรือลบ Category ได้
- ไม่สามารถเปลี่ยนสถานะหรือลบ Repair Request ได้

### Admin

- Login ได้
- ดูข้อมูลตัวเองได้
- ดู Admin Dashboard ได้
- สร้าง แก้ไข และลบ Category ได้
- สร้าง Repair Request ได้
- ดู Repair Request ทั้งหมดได้
- เปลี่ยนสถานะ Repair Request ได้
- ลบ Repair Request ได้

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

หมายเหตุ: `POST`, `PUT` และ `DELETE` ต้องใช้สิทธิ์ Admin

### Repair Requests

```txt
GET    /api/v1/repair-requests/
POST   /api/v1/repair-requests/
GET    /api/v1/repair-requests/{request_id}
PUT    /api/v1/repair-requests/{request_id}
DELETE /api/v1/repair-requests/{request_id}
PATCH  /api/v1/repair-requests/{request_id}/status
```

### Admin Dashboard

```txt
GET /api/v1/admin/dashboard
```

---

## ตัวอย่าง Request

### Login

```json
{
  "email": "admin@test.com",
  "password": "1234"
}
```

### Create Category

```json
{
  "name": "Network",
  "description": "ระบบอินเทอร์เน็ตและเครือข่าย"
}
```

### Update Category

```json
{
  "name": "Network Equipment",
  "description": "อุปกรณ์เครือข่ายและอินเทอร์เน็ต"
}
```

### Create Repair Request

```json
{
  "title": "อินเทอร์เน็ตใช้งานไม่ได้",
  "description": "คอมพิวเตอร์ในห้อง Lab 302 ต่ออินเทอร์เน็ตไม่ได้",
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

สถานะที่รองรับ:

```txt
pending
accepted
repairing
completed
cancelled
```

---

## Deploy บน Vercel

โปรเจกต์มีไฟล์ `vercel.json` สำหรับให้ Vercel route ทุก request เข้า `main.py`

ขั้นตอน:

1. Push code ขึ้น GitHub
2. Import repository ใน Vercel
3. Deploy ได้เลยโดยใช้ settings เริ่มต้น
4. เปิด URL ที่ Vercel สร้างให้ แล้วเข้า `/web`

หมายเหตุสำคัญ: SQLite บน Vercel ใช้ไฟล์ชั่วคราวใน `/tmp` เพื่อให้เขียนข้อมูลได้ใน serverless runtime ข้อมูลที่เพิ่มใน Production อาจหายเมื่อเกิด cold start หรือ redeploy ถ้าต้องการใช้งานจริงแบบข้อมูลไม่หาย ควรเปลี่ยนเป็นฐานข้อมูลถาวร เช่น Supabase, Neon หรือ PostgreSQL service อื่น

---

## Run Unit Test

รันด้วยคำสั่ง:

```bash
python -m pytest -v
```

หรือดับเบิลคลิก:

```txt
run_tests.bat
```

ผลลัพธ์ปัจจุบันควรผ่านทั้งหมด:

```txt
4 passed
```

---

## Project Structure

```txt
repair-request-system/
├── api/
├── docs/
├── schemas/
├── static/
│   └── index.html
├── tests/
├── auth_dependencies.py
├── auth_utils.py
├── database.py
├── main.py
├── models.py
├── requirements.txt
├── seed.py
├── start.bat
├── run_tests.bat
├── vercel.json
└── repair_system.sqlite3
```

---

## สรุป

Repair Request Management System เป็นระบบแจ้งซ่อมที่มีหน้าเว็บพร้อมใช้งาน มีระบบ Login ด้วย JWT แยกสิทธิ์ Admin/User จัดการ Category ได้ครบ สร้างและติดตามรายการแจ้งซ่อมได้ มี API Docs สำหรับทดสอบ และมี config สำหรับ Deploy บน Vercel
