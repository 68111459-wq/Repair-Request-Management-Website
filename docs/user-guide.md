\# วิธีเข้าใช้งานระบบ Repair Request Management System



ระบบแจ้งซ่อมอุปกรณ์ภายในองค์กร พัฒนาด้วย FastAPI มีระบบ Login ด้วย JWT และแยกสิทธิ์การใช้งานระหว่าง Admin กับ User



\---



\## URL



Local API: http://localhost:8000  

Swagger API Docs: http://localhost:8000/docs



\---



\## Account สำหรับเข้าใช้งาน



\### Admin Account



Email: admin@test.com  

Password: 1234



\### User Account



Email: user@test.com  

Password: 1234



\---



\## วิธีรันระบบแบบง่าย



สามารถดับเบิลคลิกไฟล์นี้ได้เลย:



```txt

start.bat

```



เมื่อเปิด `start.bat` ระบบจะติดตั้ง dependencies, สร้างข้อมูลตัวอย่าง และเปิด Swagger ให้อัตโนมัติ



\---



\## วิธีรันระบบแบบ Manual



เปิด Terminal ที่โฟลเดอร์ `repair-request-system` แล้วรันคำสั่ง:



```bash

python -m venv venv

venv\\Scripts\\activate

python -m pip install -r requirements.txt

python seed.py

python -m uvicorn main:app --reload

```



จากนั้นเปิด:



```txt

http://localhost:8000/docs

```



\---



\## วิธีใช้งานผ่าน Swagger



1\. เข้า http://localhost:8000/docs

2\. ไปที่ `POST /api/v1/auth/login`

3\. กด `Try it out`

4\. Login ด้วยข้อมูลนี้:



```json

{

&#x20; "email": "admin@test.com",

&#x20; "password": "1234"

}

```



5\. กด `Execute`

6\. Copy ค่า `access\_token`

7\. กดปุ่ม `Authorize`

8\. วาง token ลงไป

9\. กด `Authorize` แล้วกด `Close`

10\. ทดสอบ API เช่น Categories, Repair Requests และ Admin Dashboard



\---



\## API หลักของระบบ



\### Auth



```txt

POST /api/v1/auth/register

POST /api/v1/auth/login

GET  /api/v1/auth/me

```



\### Categories



```txt

GET    /api/v1/categories/

POST   /api/v1/categories/

GET    /api/v1/categories/{category\_id}

PUT    /api/v1/categories/{category\_id}

DELETE /api/v1/categories/{category\_id}

```



หมายเหตุ: การเพิ่ม แก้ไข และลบ Category ต้องใช้สิทธิ์ Admin



\### Repair Requests



```txt

GET    /api/v1/repair-requests/

POST   /api/v1/repair-requests/

GET    /api/v1/repair-requests/{request\_id}

PUT    /api/v1/repair-requests/{request\_id}

DELETE /api/v1/repair-requests/{request\_id}

PATCH  /api/v1/repair-requests/{request\_id}/status

```



หมายเหตุ: User สามารถสร้างและดูรายการของตัวเองได้ ส่วน Admin สามารถดูทั้งหมดและเปลี่ยนสถานะงานซ่อมได้



\### Admin



```txt

GET /api/v1/admin/dashboard

```



หมายเหตุ: API นี้ต้องใช้สิทธิ์ Admin



\---



\## ตัวอย่างการใช้งาน



\### สร้าง Category



```json

{

&#x20; "name": "Network",

&#x20; "description": "ระบบอินเทอร์เน็ตและเครือข่าย"

}

```



\### สร้าง Repair Request



```json

{

&#x20; "title": "อินเทอร์เน็ตใช้งานไม่ได้",

&#x20; "description": "คอมพิวเตอร์ในห้อง Lab ต่ออินเทอร์เน็ตไม่ได้",

&#x20; "location": "Lab 302",

&#x20; "priority": "high",

&#x20; "category\_id": 1

}

```



\### เปลี่ยนสถานะงานซ่อม



```json

{

&#x20; "new\_status": "repairing",

&#x20; "note": "เจ้าหน้าที่รับเรื่องและกำลังตรวจสอบ"

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



\---



\## วิธีทดสอบ Unit Test



สามารถดับเบิลคลิกไฟล์นี้ได้เลย:



```txt

run\_tests.bat

```



หรือรันเองด้วยคำสั่ง:



```bash

python -m pytest -v

```



ผลลัพธ์ที่ควรได้:



```txt

3 passed

```



\---



\## ไฟล์ที่ไม่ควรใส่ใน ZIP ส่งงาน



```txt

venv/

\_\_pycache\_\_/

.pytest\_cache/

token.txt

.env

\*.log

```



\---



\## ไฟล์ที่ควรมีใน ZIP ส่งงาน



```txt

repair-request-system/

├── api/

├── schemas/

├── tests/

├── docs/

│   ├── user-guide.md

│   ├── usecase-diagram.png

│   └── system-architecture.png

├── auth\_dependencies.py

├── auth\_utils.py

├── database.py

├── main.py

├── models.py

├── requirements.txt

├── README.md

├── seed.py

├── start.bat

├── run\_tests.bat

└── repair\_system.sqlite3

```



\---



\## สรุป



###### ระบบนี้มีการ Login ด้วย JWT แยกสิทธิ์ Admin และ User โดย Admin สามารถจัดการหมวดหมู่อุปกรณ์ เปลี่ยนสถานะงานซ่อม และดู Dashboard สรุปข้อมูลระบบได้ ส่วน User สามารถสร้างรายการแจ้งซ่อมและดูรายการของตัวเองได้

