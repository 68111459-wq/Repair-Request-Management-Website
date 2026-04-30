from auth_utils import hash_password
from database import Base, SessionLocal, engine
from models import EquipmentCategory, RepairRequest, RepairStatusLog, User

Base.metadata.create_all(bind=engine)


def seed_data():
    db = SessionLocal()

    try:
        # 1. Create Admin User
        admin = db.query(User).filter(User.email == "admin@test.com").first()

        if not admin:
            admin = User(
                username="Admin",
                email="admin@test.com",
                hashed_password=hash_password("1234"),
                role="admin"
            )
            db.add(admin)
            db.commit()
            db.refresh(admin)
            print("Created admin user")
        else:
            print("Admin user already exists")

        # 2. Create Normal User
        user = db.query(User).filter(User.email == "user@test.com").first()

        if not user:
            user = User(
                username="User",
                email="user@test.com",
                hashed_password=hash_password("1234"),
                role="user"
            )
            db.add(user)
            db.commit()
            db.refresh(user)
            print("Created normal user")
        else:
            print("Normal user already exists")

        # 3. Create Categories
        category_data = [
            {
                "name": "Computer",
                "description": "คอมพิวเตอร์และอุปกรณ์ที่เกี่ยวข้อง"
            },
            {
                "name": "Network",
                "description": "ระบบอินเทอร์เน็ตและเครือข่าย"
            },
            {
                "name": "Printer",
                "description": "เครื่องพิมพ์และอุปกรณ์สำนักงาน"
            }
        ]

        categories = {}

        for item in category_data:
            category = db.query(EquipmentCategory).filter(
                EquipmentCategory.name == item["name"]
            ).first()

            if not category:
                category = EquipmentCategory(
                    name=item["name"],
                    description=item["description"]
                )
                db.add(category)
                db.commit()
                db.refresh(category)
                print(f"Created category: {category.name}")
            else:
                print(f"Category already exists: {category.name}")

            categories[item["name"]] = category

        # 4. Create Sample Repair Request
        existing_request = db.query(RepairRequest).filter(
            RepairRequest.title == "อินเทอร์เน็ตใช้งานไม่ได้"
        ).first()

        if not existing_request:
            repair_request = RepairRequest(
                title="อินเทอร์เน็ตใช้งานไม่ได้",
                description="คอมพิวเตอร์ในห้อง Lab ต่ออินเทอร์เน็ตไม่ได้",
                location="Lab 302",
                priority="high",
                status="pending",
                user_id=admin.id,
                category_id=categories["Network"].id
            )

            db.add(repair_request)
            db.commit()
            db.refresh(repair_request)

            log = RepairStatusLog(
                repair_request_id=repair_request.id,
                changed_by=admin.id,
                old_status=None,
                new_status="pending",
                note="Sample repair request created by seed script"
            )

            db.add(log)
            db.commit()

            print("Created sample repair request")
        else:
            print("Sample repair request already exists")

        print("Seed data completed successfully")

    finally:
        db.close()


if __name__ == "__main__":
    seed_data()