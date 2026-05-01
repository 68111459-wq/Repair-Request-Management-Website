# คู่มือการใช้งาน Repair Request Management System

เอกสารนี้อธิบายวิธีใช้งานระบบแจ้งซ่อมอุปกรณ์ ตั้งแต่การ Login การสร้างรายการแจ้งซ่อม การจัดการ Category สำหรับ Admin ไปจนถึงการ Deploy บน Vercel

---

## 1. เข้าใช้งานระบบ

### Local

เปิดหน้าเว็บ:

```txt
http://localhost:8000/web
```

เปิด Swagger API Docs:

```txt
http://localhost:8000/docs
```

### Production บน Vercel

หลัง Deploy ให้เปิด URL ของ Vercel แล้วเติม `/web` เช่น:

```txt
https://your-project.vercel.app/web
```

---

## 2. บัญชีสำหรับทดสอบ

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

## 3. วิธีรันระบบ

### รันแบบง่าย

ดับเบิลคลิก:

```txt
start.bat
```

ระบบจะติดตั้ง dependencies, seed ข้อมูลตัวอย่าง และเปิด server ให้โดยอัตโนมัติ

### รันด้วยคำสั่ง

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

## 4. การ Login

1. เปิดหน้า `/web`
2. ใส่ Email และ Password
3. กด `Login`
4. ถ้า Login สำเร็จ ระบบจะแสดงข้อมูลในส่วน `Current User`
5. ถ้าต้องการออกจากระบบ ให้กด `Logout`

ถ้า token หมดอายุหรือไม่มีสิทธิ์ ระบบจะเคลียร์ session และให้ Login ใหม่

---

## 5. สิทธิ์ของผู้ใช้

### Guest

ผู้ใช้ที่ยังไม่ได้ Login จะเห็นเฉพาะหน้า Login และข้อความแจ้งให้ Login ก่อนใช้งาน

Guest จะไม่สามารถ:

- ดู Dashboard
- ดู Categories
- ดู Repair Requests
- สร้าง Repair Request

### User

User สามารถ:

- ดูข้อมูลผู้ใช้ของตัวเอง
- สร้าง Repair Request
- ดู Repair Request ของตัวเอง

User ไม่สามารถ:

- ดู Admin Dashboard
- สร้าง แก้ไข หรือลบ Category
- เปลี่ยนสถานะ Repair Request
- ลบ Repair Request

### Admin

Admin สามารถ:

- ดู Admin Dashboard
- ดูจำนวน Users, Categories และ Repair Requests
- สร้าง แก้ไข และลบ Category
- สร้าง Repair Request
- ดู Repair Request ทั้งหมด
- เปลี่ยนสถานะ Repair Request
- ลบ Repair Request

---

## 6. การจัดการ Category สำหรับ Admin

ส่วนนี้จะแสดงเฉพาะเมื่อ Login ด้วยบัญชี Admin

### สร้าง Category

1. ใส่ชื่อในช่อง `Category Name`
2. ใส่รายละเอียดในช่อง `Description`
3. กด `Create Category`
4. Category ใหม่จะแสดงในตาราง Categories

### แก้ไข Category

1. กดปุ่ม `Edit` ที่แถวของ Category ที่ต้องการแก้ไข
2. ระบบจะนำ Name และ Description มาแสดงในฟอร์ม
3. แก้ไขข้อมูล
4. กด `Save Changes`
5. ตาราง Categories จะ refresh อัตโนมัติ

### ยกเลิกการแก้ไข

กด `Cancel` เพื่อกลับไปโหมดสร้าง Category ใหม่

### ลบ Category

1. กดปุ่ม `Delete`
2. ยืนยันการลบ
3. ระบบจะลบ Category และ refresh ตาราง

หมายเหตุ: ถ้ามี Repair Request ที่ใช้ Category นั้นอยู่ ระบบจะเคลียร์ `category_id` ของรายการแจ้งซ่อมเหล่านั้นก่อนลบ Category

---

## 7. การสร้าง Repair Request

1. Login ด้วย Admin หรือ User
2. ไปที่ส่วน `Create Repair Request`
3. กรอกข้อมูล:
   - Title
   - Description
   - Location
   - Priority
   - Category
4. กด `Create Repair Request`
5. รายการใหม่จะมีสถานะเริ่มต้นเป็น `pending`

Priority ที่รองรับ:

```txt
low
medium
high
```

---

## 8. การดู Repair Requests

### User

User จะเห็นเฉพาะรายการแจ้งซ่อมที่ตัวเองสร้าง

### Admin

Admin จะเห็นรายการแจ้งซ่อมทั้งหมด และมีปุ่ม Action สำหรับจัดการสถานะหรือลบรายการ

---

## 9. การเปลี่ยนสถานะงานซ่อมสำหรับ Admin

Admin สามารถกดปุ่มในตาราง Repair Requests ได้:

- `Accept` เปลี่ยนสถานะเป็น `accepted`
- `Repairing` เปลี่ยนสถานะเป็น `repairing`
- `Complete` เปลี่ยนสถานะเป็น `completed`
- `Delete` ลบรายการแจ้งซ่อม

สถานะที่ระบบรองรับ:

```txt
pending
accepted
repairing
completed
cancelled
```

---

## 10. การใช้ Swagger API Docs

เปิด:

```txt
http://localhost:8000/docs
```

### Login ผ่าน Swagger

1. ไปที่ `POST /api/v1/auth/login`
2. กด `Try it out`
3. ใส่ข้อมูล:

```json
{
  "email": "admin@test.com",
  "password": "1234"
}
```

4. กด `Execute`
5. Copy ค่า `access_token`
6. กดปุ่ม `Authorize`
7. ใส่ token ในรูปแบบ:

```txt
Bearer your_access_token
```

8. กด `Authorize`

หลังจากนั้นจะเรียก API ที่ต้อง Login หรือ API สำหรับ Admin ได้

---

## 11. API หลัก

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

หมายเหตุ: การสร้าง แก้ไข และลบ Category ต้องใช้สิทธิ์ Admin

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

## 12. ตัวอย่าง API Request

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
  "name": "Printer",
  "description": "เครื่องพิมพ์และอุปกรณ์สำนักงาน"
}
```

### Create Repair Request

```json
{
  "title": "เครื่องพิมพ์ใช้งานไม่ได้",
  "description": "เครื่องพิมพ์ไม่ดึงกระดาษ",
  "location": "Office 201",
  "priority": "medium",
  "category_id": 3
}
```

### Update Repair Status

```json
{
  "new_status": "repairing",
  "note": "เจ้าหน้าที่กำลังตรวจสอบ"
}
```

### Admin Dashboard Response

```json
{
  "total_users": 2,
  "total_categories": 3,
  "total_requests": 1,
  "pending_requests": 1,
  "repairing_requests": 0,
  "completed_requests": 0,
  "cancelled_requests": 0
}
```

---

## 13. Deploy บน Vercel

โปรเจกต์นี้มี `vercel.json` แล้ว สามารถ Deploy บน Vercel ได้

ขั้นตอน:

1. Push code ขึ้น GitHub
2. Import repository เข้า Vercel
3. Deploy ด้วยค่าเริ่มต้น
4. เปิด URL ที่ Vercel ให้มา แล้วเข้า `/web`

ตัวอย่าง:

```txt
https://your-project.vercel.app/web
```

### หมายเหตุเรื่อง SQLite บน Vercel

Vercel เป็น serverless runtime และไม่เหมาะกับการเขียนไฟล์ SQLite ถาวรในโฟลเดอร์ deploy ดังนั้นระบบนี้จะ copy database ไปใช้ที่ `/tmp/repair_system.sqlite3` เมื่อรันบน Vercel เพื่อให้สร้าง แก้ไข และลบข้อมูลได้

ข้อจำกัดคือข้อมูลใน `/tmp` เป็นข้อมูลชั่วคราว อาจหายเมื่อ cold start หรือ redeploy ถ้าต้องการใช้งานจริงแบบข้อมูลไม่หาย ควรเปลี่ยนไปใช้ฐานข้อมูลถาวร เช่น Supabase, Neon หรือ PostgreSQL service อื่น

---

## 14. Run Unit Test

รัน:

```bash
python -m pytest -v
```

หรือดับเบิลคลิก:

```txt
run_tests.bat
```

ผลลัพธ์ปัจจุบัน:

```txt
4 passed
```

---

## 15. สรุป

ระบบนี้รองรับการใช้งานแจ้งซ่อมครบขั้นพื้นฐาน มี Login แยกสิทธิ์ Admin/User มีหน้าเว็บใช้งานง่าย มี Category CRUD สำหรับ Admin มี Repair Request workflow และมี API Docs สำหรับทดสอบระบบ
