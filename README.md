# 🎴 Mythix TCG Platform — User Flow, UI & Architecture Specification

ยินดีต้อนรับสู่ Repository สำหรับจัดเก็บและติดตามความคืบหน้าของ **User Flow, Figma UI/UX Design System, User Stories และ Architecture Requirements** ของโปรเจกต์ **Mythix TCG Platform (DevOps Project)**

---

## 📊 ตารางการทำงานและการแบ่งหน้าที่ (DACI Framework)

การบริหารจัดการบทบาทและความรับผิดชอบของทีม ใช้ **DACI Framework** ในการกำหนดสิทธิ์และหน้าที่:
- **D (Driver):** ผู้ขับเคลื่อนโครงการและงานแต่ละส่วน
- **A (Approver):** ผู้มีอำนาจตัดสินใจและอนุมัติผลงาน
- **C (Contributor):** ผู้สนับสนุน ให้ข้อมูล ปรึกษา และช่วยออกแบบ/พัฒนา
- **I (Informed):** ผู้ที่ต้องได้รับแจ้งสถานะและความคืบหน้า

👉 **เข้าดูตารางงานและบทบาท DACI ฉบับเต็มได้ที่นี่:**  
🔗 **[DACI Framework — ตารางงานและหน้าที่ของทีม (Canva)](https://canva.link/jze669c3fkham3h)**

---

## 📁 โครงสร้างไฟล์ใน Repository (Directory Structure)

```text
.
├── Architecture/                     # เอกสารสถาปัตยกรรมและข้อกำหนดของระบบ
│   ├── build_detailed_erd.js         # สคริปต์สำหรับสร้าง ER Diagram แบบละเอียด
│   ├── CORE_REQUIREMENTS_CROSSCHECK.md # ตรวจสอบและ Cross-check Core Requirements
│   ├── database_architecture_detailed.html # ไฟล์ HTML สำหรับแสดงผล ER Diagram
│   ├── DATABASE_DESIGN.md            # เอกสารการออกแบบฐานข้อมูล
│   └── database_er_diagram.png       # รูปภาพ ER Diagram ของระบบ
│
├── Docker_compose_DB/                # การตั้งค่า Docker และฐานข้อมูลจำลอง (Local DB)
│   ├── docker-compose.yml            # ไฟล์สำหรับรัน PostgreSQL ด้วย Docker
│   ├── LOCAL_DATABASE_GUIDE.md       # คู่มือการใช้งานและเชื่อมต่อฐานข้อมูล Local
│   └── init-db/                      # โฟลเดอร์เก็บสคริปต์สำหรับสร้างและจำลองข้อมูลเริ่มต้น
│       ├── 01-schema.sql             # สคริปต์สร้างตาราง (Tables schema)
│       └── 02-data.sql               # สคริปต์เพิ่มข้อมูลตัวอย่าง (Mock data)
│
├── FIgma/                            # การออกแบบ UI/UX, Assets และ Catalog หน้าจอ
│   ├── FIGMA_UI_TODO.md              # รายการสิ่งที่ต้องทำและสถานะความคืบหน้าของ UI
│   ├── TCG DevOp Project_ui.pdf      # ไฟล์ Export UI Mockup รวมจาก Figma
│   ├── TCG DevOp Project_ui_Parsed.md# ข้อมูลสรุปและโครงสร้างที่สกัดจากไฟล์ UI PDF
│   ├── UI_FRAMES_CATALOG.md          # แคตตาล็อกแจกแจงรายละเอียดและ Flow ของทุก Frame
│   └── SVG/                          # ภาพ SVG แยกหมวดหมู่ตามหน้าจอและ Flow การใช้งาน
│       ├── auth/                     # หน้าจอระบบ Authentication
│       ├── Buyer Account & Storefront/# หน้าจอฝั่ง Buyer และ Storefront
│       ├── Checkout Flow/            # หน้าจอกระบวนการสั่งซื้อ ชำระเงิน
│       ├── platform-admin/           # หน้าจอจัดการระบบระดับ Platform
│       ├── profile/                  # หน้าจอการจัดการโปรไฟล์
│       ├── seller/                   # หน้าจอ Seller Dashboard, จัดการสต็อก/สินค้า
│       └── Shop & Browse/            # หน้าจอค้นหา เลือกดูการ์ด และ Filter
│
├── User Story & Flow/                # ผังการทำงาน (User Flow) และ User Story
│   ├── USER_STORIES.md               # ข้อกำหนด User Stories ฉบับสมบูรณ์ (US-01 ถึง US-12 รวม 38 ข้อ)
│   └── User Flow/                    # โฟลเดอร์สำหรับจัดเก็บแผนผัง User Flow
│
└── README.md                         # คำอธิบายโครงสร้างโปรเจกต์และเอกสารอ้างอิง
```

---

## 📌 สรุปรายละเอียดแต่ละโฟลเดอร์

### 1. `Architecture/`
รวบรวมเอกสารทางด้านข้อกำหนดและการวิเคราะห์เชิงเทคนิค
- **`CORE_REQUIREMENTS_CROSSCHECK.md`**: เอกสารสำคัญที่ระบุการ Cross-check ระหว่าง Requirement บังคับ 8 ข้อของ Course PDF กับสถานะการออกแบบและพัฒนาจริง (เช่น Auth, Catalog, Cart, Order, Seller Dashboard, Cost/Profit calculation, Fulfillment, Inventory)
- **`DATABASE_DESIGN.md`**: รายละเอียดตารางและความสัมพันธ์ของฐานข้อมูล

### 2. `FIgma/`
รวบรวมการออกแบบ UI/UX, Style Guide และโครงสร้างหน้าจอทั้งหมด
- **`UI_FRAMES_CATALOG.md` & `FIGMA_UI_TODO.md`**: บันทึกรายการ Frame ทั้งหมดกว่า 70+ Frames พร้อม Checklist สถานะการออกแบบ
- **`SVG/`**: แบ่งโฟลเดอร์ย่อยตาม Module เพื่อให้ง่ายต่อการนำ Asset ไปต่อยอดใน Frontend (เช่น auth, Shop & Browse, Checkout Flow, seller, profile, Buyer Account & Storefront, platform-admin)

### 3. `User Story & Flow/`
รวบรวมสเปกและพฤติกรรมผู้ใช้ของระบบ
- **`USER_STORIES.md`**: สเปกความต้องการของผู้ใช้แบ่งตาม User Story รหัส US-01 ถึง US-12 รวม 38 ข้อ แบบละเอียด
- **`User Flow/`**: โฟลเดอร์สำหรับนำภาพหน้าจอที่อธิบาย Flow ต่าง ๆ เข้ามาเก็บไว้

### 4. `Docker_compose_DB/`
เครื่องมือจำลองฐานข้อมูลสำหรับ Local Development
- **`LOCAL_DATABASE_GUIDE.md`**: คู่มือวิธีรัน `docker-compose up` และการเชื่อมต่อ DBeaver/DataGrip

---

## 🗺️ แผนผัง User Stories (US Overview)

| รหัส | ขอบเขตการทำงาน (Feature Scope) | รายละเอียด Flow / UI ที่รองรับ |
| :--- | :--- | :--- |
| **US-01** | User Authentication | สมัครสมาชิก, เข้าสู่ระบบ, กู้คืนรหัสผ่าน, Logout |
| **US-02** | Browse & Search Cards | ค้นหาการ์ด, กรองตามประเภท/ราคา/สภาพ, ดูหน้ารายละเอียด |
| **US-03** | Shopping Cart Management | เพิ่มลงตะกร้า, ปรับเพิ่ม/ลดจำนวน, ลบสินค้าออกจากตะกร้า |
| **US-04** | Order Placement | สั่งซื้อจากตะกร้า และสั่งซื้อทันที (Buy Now), คำนวณยอดรวม |
| **US-05** | Inventory & Listing CRUD | ผู้ขายเพิ่ม/แก้ไข/ลบการ์ด, ซ่อน/แสดงสินค้า, อัปเดตราคาและจำนวน |
| **US-06** | Seller Dashboard | สรุปยอดขาย, กำไร/ต้นทุน, สถิติคำสั่งซื้อ |
| **US-07** | Order Management | ผู้ขายตรวจสอบรายการคำสั่งซื้อ, ปรับสถานะ (Pending → Fulfilled/Cancelled) |
| **US-08** | User Profile Management | แก้ไขชื่อ ที่อยู่ เบอร์โทรศัพท์ และข้อมูลติดต่อ |
| **US-09** | Order History & Tracking | ผู้ซื้อดูประวัติการสั่งซื้อ และตรวจสอบสถานะการจัดส่ง |
| **US-10** | Card Collection & Verification | ระบบสร้าง Collection การ์ดสะสมส่วนตัว, ยื่นยืนยันตัวตน Seller และ Leaderboard |
| **US-11** | In-App Notifications | ระบบแจ้งเตือนในระบบ (เมื่อมีคนจองการ์ด, อัปเดตสถานะ, แจ้งเตือนสิทธิ์) |
| **US-12** | Platform Administration | ระบบผู้ดูแลระบบส่วนกลาง (Admin Dashboard, คิวอนุมัติ Seller, User & Audit Logs) |

---

## 🤝 การมีส่วนร่วมและแนวทางการใช้งาน

1. **การอัปเดต User Flow:** ให้นำภาพแผนผังหรือหน้าจอที่มีการอัปเดตล่าสุดมาบันทึกไว้ในโฟลเดอร์ `User Story & Flow/User Flow/`
2. **การอัปเดต UI/UX:** นำภาพที่ Export จาก Figma มาบันทึกไว้ใน `FIgma/SVG/<module>/` ให้ตรงตามหมวดหมู่
3. **การติดตามความรับผิดชอบ:** โปรดอ้างอิงและอัปเดตสถานะงานตาม [DACI Framework บน Canva](https://canva.link/jze669c3fkham3h)
