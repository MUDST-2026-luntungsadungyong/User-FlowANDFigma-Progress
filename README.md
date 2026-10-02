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
│   └── CORE_REQUIREMENTS_CROSSCHECK.md # ตรวจสอบและ Cross-check Core Requirements กับขอบเขตงานจริง
│
├── FIgma/                            # การออกแบบ UI/UX, Assets และ Catalog หน้าจอ
│   ├── FIGMA_UI_TODO.md              # รายการสิ่งที่ต้องทำและสถานะความคืบหน้าของ UI
│   ├── TCG DevOp Project_ui.pdf      # ไฟล์ Export UI Mockup รวมจาก Figma
│   ├── TCG DevOp Project_ui_Parsed.md# ข้อมูลสรุปและโครงสร้างที่สกัดจากไฟล์ UI PDF
│   ├── UI_FRAMES_CATALOG.md          # แคตตาล็อกแจกแจงรายละเอียดและ Flow ของทุก Frame
│   └── SVG/                          # ภาพ SVG แยกหมวดหมู่ตามหน้าจอและ Flow การใช้งาน
│       ├── auth/                     # หน้าจอระบบ Authentication (Login, Register, Reset Password)
│       ├── Buyer Account & Storefront/# หน้าจอฝั่ง Buyer, หน้าร้านค้า และ Storefront
│       ├── Checkout Flow/            # หน้าจอกระบวนการสั่งซื้อ ชำระเงิน และยืนยันคำสั่งซื้อ
│       ├── platform-admin/           # หน้าจอจัดการระบบระดับ Platform
│       ├── profile/                  # หน้าจอการจัดการโปรไฟล์และข้อมูลส่วนตัวของผู้ใช้
│       ├── seller/                   # หน้าจอ Seller Dashboard, จัดการสต็อก/สินค้า และออเดอร์
│       └── Shop & Browse/            # หน้าจอค้นหา เลือกดูการ์ด และ Filter แคตตาล็อก
│
├── UserFlow_and_UserStory/           # ผังการทำงาน (User Flow) และ User Story
│   ├── Old_User_Flow.pdf             # แผนผัง User Flow เวอร์ชันเดิม (Reference)
│   ├── USER_STORIES.md           # ข้อกำหนด User Stories ฉบับสมบูรณ์ (US-01 ถึง US-12 รวม 38 ข้อ)
│   ├── USER_STORIES_TODO.md          # รายการ Checklist สถานะการปรับแก้ User Stories
│   └── New_Flow&Story/               # User Flows ฉบับปรับปรุงใหม่ (Mermaid source + Exported SVG)
│       ├── New_Flows_Preview.md      # เอกสารสรุปพรีวิวและรายละเอียด Flow ทั้งหมด
│       ├── US-01-1_Register-Login.svg# Flow: การสมัครสมาชิกและการเข้าสู่ระบบ
│       ├── US-02-1_Browse-Cards.svg  # Flow: การค้นหาและดูรายละเอียดสินค้า/การ์ด
│       ├── US-03-*.svg               # Flow: การจัดการตะกร้าสินค้า (เพิ่ม/ลด/ลบ)
│       ├── US-04-*.svg / .mmd        # Flow: การสั่งซื้อสินค้า (Cart & Direct Purchase)
│       ├── US-05-*.svg / .mmd        # Flow: การจัดการสต็อกและสินค้าของผู้ขาย (CRUD Inventory)
│       ├── US-06-*.svg / .mmd        # Flow: หน้า Seller Dashboard & รายงานยอดขาย
│       ├── US-07-*.svg / .mmd        # Flow: การจัดการคำสั่งซื้อและสถานะออเดอร์ (Order Management)
│       ├── US-08-*.svg / .mmd        # Flow: การแก้ไขข้อมูลโปรไฟล์ผู้ใช้
│       ├── US-09-*.svg               # Flow: การดูและกรองประวัติการสั่งซื้อ (Order History)
│       └── US-10-*.svg / .mmd        # Flow: คลังสะสม (Collection) & Seller Verification
│
└── README.md                         # คำอธิบายโครงสร้างโปรเจกต์และเอกสารอ้างอิง
```

---

## 📌 สรุปรายละเอียดแต่ละโฟลเดอร์

### 1. `Architecture/`
รวบรวมเอกสารทางด้านข้อกำหนดและการวิเคราะห์เชิงเทคนิค
- **`CORE_REQUIREMENTS_CROSSCHECK.md`**: เอกสารสำคัญที่ระบุการ Cross-check ระหว่าง Requirement บังคับ 8 ข้อของ Course PDF กับสถานะการออกแบบและพัฒนาจริง (เช่น Auth, Catalog, Cart, Order, Seller Dashboard, Cost/Profit calculation, Fulfillment, Inventory)

### 2. `FIgma/`
รวบรวมการออกแบบ UI/UX, Style Guide และโครงสร้างหน้าจอทั้งหมด
- **`UI_FRAMES_CATALOG.md` & `FIGMA_UI_TODO.md`**: บันทึกรายการ Frame ทั้งหมดกว่า 70+ Frames พร้อม Checklist สถานะการออกแบบ
- **`SVG/`**: แบ่งโฟลเดอร์ย่อยตาม Module เพื่อให้ง่ายต่อการนำ Asset ไปต่อยอดใน Frontend:
  - **`auth`**: Login, Register, Forgot Password, Reset Password
  - **`Shop & Browse`**: Catalog, Search & Multi-filter, Card Detail Modal
  - **`Checkout Flow`**: Cart View, Shipping Address, Direct Checkout, Order Confirmation
  - **`seller`**: Seller Dashboard, Add/Edit Listing, Order Fulfillment, Stock Adjustment
  - **`profile`**: User Profile, Security Settings, Order History
  - **`Buyer Account & Storefront`**: หน้าร้านค้าของผู้ขายแต่ละคน มุมมองของ Buyer
  - **`platform-admin`**: หน้าจอผู้ดูแลระบบ

### 3. `UserFlow_and_UserStory/`
แผนผังการไหลของข้อมูลและพฤติกรรมผู้ใช้ (User Flows)
- **`USER_STORIES_TODO.md`**: สเปกความต้องการของผู้ใช้แบ่งตาม User Story รหัส US-01 ถึง US-10
- **`New_Flow&Story/`**: รวบรวมไฟล์ Diagram ในรูปแบบ **Mermaid (`.mmd`)** สำหรับแก้ไขโค้ดไดอะแกรม และ **SVG (`.svg`)** สำหรับนำไปแสดงผลหรือแปะในเอกสาร พร้อมไฟล์ **`New_Flows_Preview.md`** สำหรับเปิดดูพรีวิวรวมทั้งหมด

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

1. **การอัปเดต User Flow:** แนะนำให้แก้ไขผ่านไฟล์ Mermaid (`.mmd`) ใน `UserFlow_and_UserStory/New_Flow&Story/` แล้ว Export เป็น `.svg` เพื่อความสม่ำเสมอ
2. **การอัปเดต UI/UX:** นำภาพที่ Export จาก Figma มาบันทึกไว้ใน `FIgma/SVG/<module>/` ให้ตรงตามหมวดหมู่
3. **การติดตามความรับผิดชอบ:** โปรดอ้างอิงและอัปเดตสถานะงานตาม [DACI Framework บน Canva](https://canva.link/jze669c3fkham3h)
