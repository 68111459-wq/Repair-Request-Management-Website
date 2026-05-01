# วิธีเข้าใช้งานระบบ Repair Request Management System

Repair Request Management System เป็นระบบแจ้งซ่อมอุปกรณ์ภายในองค์กร พัฒนาด้วย FastAPI มีระบบ Login ด้วย JWT แยกสิทธิ์การใช้งานระหว่าง Admin และ User และมีหน้าเว็บสำหรับใช้งานระบบ

---

## URL สำหรับเข้าใช้งาน

### Web Application

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

## บัญชีสำหรับเข้าใช้งาน

### Admin Account

Email: admin@test.com  
Password: 1234

### User Account

Email: user@test.com  
Password: 1234

---

## วิธีรันระบบแบบง่าย

สามารถดับเบิลคลิกไฟล์นี้ได้เลย:

```txt
start.bat
```

เมื่อเปิด `start.bat` ระบบจะทำงานให้อัตโนมัติ ดังนี้:

```txt
1. สร้าง virtual environment ถ้ายังไม่มี
2. Activate virtual environment
3. ติดตั้ง dependencies จาก requirements.txt
4. สร้างข้อมูลตัวอย่างด้วย seed.py
5. เปิดหน้า Web Application อัตโนมัติ
6. รัน FastAPI server
```

หลังจากรันสำเร็จ ระบบจะเปิดหน้าเว็บที่:

```txt
http://localhost:8000/web
```

และยังสามารถเปิด Swagger API Docs ได้ที่:

```txt
http://localhost:8000/docs
```

---

## วิธีรันระบบด้วยคำสั่ง Manual

ถ้าต้องการรันเอง ให้เปิด Terminal ที่โฟลเดอร์ `repair-request-system` แล้วพิมพ์:

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

หรือเปิด Swagger:

```txt
http://localhost:8000/docs
```

---

## วิธีใช้งานผ่านหน้าเว็บ

1. เปิดหน้าเว็บ:

```txt
http://localhost:8000/web
```

2. Login ด้วยบัญชี Admin หรือ User

3. ถ้า Login เป็น Admin จะสามารถใช้งานได้ดังนี้:

```txt
- ดู Admin Dashboard
- ดูจำนวน Users, Categories และ Repair Requests
- สร้าง Category
- ดู Category ทั้งหมด
- สร้าง Repair Request
- ดู Repair Requests ทั้งหมด
- เปลี่ยนสถานะงานซ่อม
- ลบรายการแจ้งซ่อม
```

4. ถ้า Login เป็น User จะสามารถใช้งานได้ดังนี้:

```txt
- ดูข้อมูล Current User
- สร้าง Repair Request
- ดู Repair Requests ของตัวเอง
- ไม่เห็น Admin Dashboard
- ไม่เห็น Create Category
- ไม่สามารถเปลี่ยนสถานะหรือลบรายการแจ้งซ่อมได้
```

5. ถ้า Logout แล้ว ระบบจะซ่อนข้อมูลที่ต้อง Login เช่น Dashboard, Categories, Create Repair Request และ Repair Requests

---

## วิธีใช้งานผ่าน Swagger

1. เข้า Swagger API Docs:

```txt
http://localhost:8000/docs
```

2. ไปที่ API:

```txt
POST /api/v1/auth/login
```

3. กด `Try it out`

4. ใส่ข้อมูล Login:

```json
{
  "email": "admin@test.com",
  "password": "1234"
}
```

5. กด `Execute`
6. Copy ค่า `access_token` จาก Response
7. กดปุ่ม `Authorize` ด้านบนของ Swagger
8. วาง token ในรูปแบบนี้:

```txt
Bearer your_access_token
```

9. กด `Authorize` แล้วกด `Close`

หลังจาก Authorize แล้ว จะสามารถเรียก API ที่ต้อง Login หรือ API สำหรับ Admin ได้

---

## API หลักของระบบ

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

หมายเหตุ: การเพิ่ม แก้ไข และลบ Category ต้องใช้สิทธิ์ Admin

### Repair Requests

```txt
GET    /api/v1/repair-requests/
POST   /api/v1/repair-requests/
GET    /api/v1/repair-requests/{request_id}
PUT    /api/v1/repair-requests/{request_id}
DELETE /api/v1/repair-requests/{request_id}
PATCH  /api/v1/repair-requests/{request_id}/status
```

หมายเหตุ: User สามารถสร้างและดูรายการของตัวเองได้ ส่วน Admin สามารถดูทั้งหมดและเปลี่ยนสถานะงานซ่อมได้

### Admin

```txt
GET /api/v1/admin/dashboard
```

หมายเหตุ: API นี้ต้องใช้สิทธิ์ Admin

---

## ตัวอย่างการทดสอบระบบผ่าน Swagger

### 1. ตรวจสอบข้อมูลผู้ใช้ปัจจุบัน

ใช้ API:

```txt
GET /api/v1/auth/me
```

ตัวอย่าง Response:

```json
{
  "id": 1,
  "username": "Admin",
  "email": "admin@test.com",
  "role": "admin"
}
```

---

### 2. สร้างหมวดหมู่อุปกรณ์

ใช้ API:

```txt
POST /api/v1/categories/
```

Request Body:

```json
{
  "name": "Network",
  "description": "ระบบอินเทอร์เน็ตและเครือข่าย"
}
```

---

### 3. สร้างรายการแจ้งซ่อม

ใช้ API:

```txt
POST /api/v1/repair-requests/
```

Request Body:

```json
{
  "title": "อินเทอร์เน็ตใช้งานไม่ได้",
  "description": "คอมพิวเตอร์ในห้อง Lab ต่ออินเทอร์เน็ตไม่ได้",
  "location": "Lab 302",
  "priority": "high",
  "category_id": 1
}
```

เมื่อสร้างสำเร็จ ระบบจะกำหนดสถานะเริ่มต้นเป็น `pending`

---

### 4. เปลี่ยนสถานะงานซ่อม

ใช้ API:

```txt
PATCH /api/v1/repair-requests/{request_id}/status
```

ตัวอย่าง:

```txt
PATCH /api/v1/repair-requests/1/status
```

Request Body:

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

### 5. ดู Admin Dashboard

ใช้ API:

```txt
GET /api/v1/admin/dashboard
```

ตัวอย่าง Response:

```json
{
  "total_users": 2,
  "total_categories": 3,
  "total_requests": 2,
  "pending_requests": 1,
  "repairing_requests": 1,
  "completed_requests": 0,
  "cancelled_requests": 0
}
```

---

## วิธีรัน Unit Test

สามารถดับเบิลคลิกไฟล์นี้ได้เลย:

```txt
run_tests.bat
```

หรือรันเองด้วยคำสั่ง:

```bash
python -m pytest -v
```

ถ้าสำเร็จจะเห็นผลลัพธ์ประมาณนี้:

```txt
3 passed
```

---

## วิธี Deploy บน Render

ใช้ GitHub Repository ของโปรเจกต์นี้ แล้วสร้าง Web Service

### Build Command

```bash
pip install -r requirements.txt
```

### Start Command

```bash
python seed.py && python -m uvicorn main:app --host 0.0.0.0 --port $PORT
```

หลัง Deploy สำเร็จ ให้เปิด:

```txt
https://your-render-url.onrender.com/web
```

Swagger API Docs จะอยู่ที่:

```txt
https://your-render-url.onrender.com/docs

---

## ไฟล์ที่ควรมีใน ZIP ส่งงาน

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

## สรุป

ระบบนี้มีการ Login ด้วย JWT แยกสิทธิ์ Admin และ User โดย Admin สามารถจัดการหมวดหมู่อุปกรณ์ เปลี่ยนสถานะงานซ่อม และดู Dashboard สรุปข้อมูลระบบได้ ส่วน User สามารถสร้างรายการแจ้งซ่อมและดูรายการของตัวเองได้ ระบบมีหน้าเว็บสำหรับใช้งาน มี Swagger สำหรับทดสอบ API มี Database สำหรับจัดเก็บข้อมูล และมี Unit Test สำหรับตรวจสอบการทำงานของ API
