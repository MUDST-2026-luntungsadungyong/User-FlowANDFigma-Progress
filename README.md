# 🎴 Mythix TCG Platform — User Flow, UI, Architecture & DevOps Specification

ยินดีต้อนรับสู่ Repository หลักของโปรเจกต์ **Mythix TCG Platform (DevOps Project)** สำหรับจัดเก็บเอกสารสถาปัตยกรรม, User Stories & User Flows, Figma UI/UX Design System, ฐานข้อมูลจำลอง, เอกสาร CI/CD Quality Gates และโครงสร้าง Docker / Jenkins Full-Stack Orchestration

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
├── Architecture/                         # เอกสารสถาปัตยกรรมและข้อกำหนดของระบบ
│   ├── build_detailed_erd.js             # สคริปต์สำหรับสร้าง ER Diagram แบบละเอียด
│   ├── CORE_REQUIREMENTS_CROSSCHECK.md   # ตรวจสอบและ Cross-check Core Requirements
│   ├── database_architecture_detailed.html # Interactive HTML สำหรับแสดงผล ER Diagram
│   ├── DATABASE_DESIGN.md                # เอกสารการออกแบบฐานข้อมูล (Revision 5, PostgreSQL 16)
│   └── database_er_diagram.png           # รูปภาพ ER Diagram ความละเอียดสูงของระบบ
│
├── Docker_compose_DB/                    # การตั้งค่า Docker และฐานข้อมูลจำลอง (Local DB)
│   ├── docker-compose.yml                # ไฟล์สำหรับรัน PostgreSQL ด้วย Docker
│   ├── LOCAL_DATABASE_GUIDE.md           # คู่มือการใช้งานและเชื่อมต่อฐานข้อมูล Local
│   └── init-db/                          # สคริปต์สร้าง Schema และข้อมูลตัวอย่างเริ่มต้น
│       ├── 01-schema.sql                 # สคริปต์สร้างตาราง (Tables schema)
│       └── 02-data.sql                   # สคริปต์เพิ่มข้อมูลตัวอย่าง (Mock data & tracking logs)
│
├── FIgma/                                # การออกแบบ UI/UX, Assets และ Catalog หน้าจอ
│   ├── FIGMA_UI_TODO.md                  # รายการสิ่งที่ต้องทำและสถานะความคืบหน้าของ UI
│   ├── TCG DevOp Project_ui.pdf          # ไฟล์ Export UI Mockup รวมจาก Figma
│   ├── TCG DevOp Project_ui_Parsed.md    # ข้อมูลสรุปและโครงสร้างที่สกัดจากไฟล์ UI PDF
│   ├── UI_FRAMES_CATALOG.md              # แคตตาล็อกแจกแจงรายละเอียดและ Flow ของทุก Frame
│   ├── figma_pics/                       # ภาพ PNG หน้าจอที่ Export จาก Figma แยกตามโมดูล
│   └── SVG/                              # ภาพ SVG แยกหมวดหมู่ตามหน้าจอและ Flow การใช้งาน
│       ├── auth/                         # หน้าจอระบบ Authentication
│       ├── Buyer Account & Storefront/   # หน้าจอฝั่ง Buyer และ Storefront
│       ├── Checkout Flow/                # หน้าจอกระบวนการสั่งซื้อ ชำระเงิน
│       ├── platform-admin/               # หน้าจอจัดการระบบระดับ Platform
│       ├── profile/                      # หน้าจอการจัดการโปรไฟล์
│       ├── seller/                       # หน้าจอ Seller Dashboard, จัดการสต็อก/สินค้า
│       └── Shop & Browse/                # หน้าจอค้นหา เลือกดูการ์ด และ Filter
│
├── User Story & Flow/                    # ผังการทำงาน (User Flow) และ User Story
│   ├── USER_STORIES.md                   # Phase 1 User Stories ฉบับสมบูรณ์ (US-01 ถึง US-12 รวม 43 ข้อ)
│   ├── final_user_story_phase_2.md       # Phase 2 Final Scope Agreement (US-13 ถึง US-29)
│   ├── check-process-phase2.md           # Checklist ตรวจสอบสถานะการพัฒนาฟีเจอร์ Phase 2
│   ├── user story phase 2.md             # เอกสารร่างและรายละเอียด Phase 2 (Auction & Extended)
│   ├── user story phase 2_ other.md      # ข้อกำหนดเพิ่มเติมสำหรับ Phase 2
│   └── User Flow/                        # แผนผัง User Flow (.pdf) และ Wireframe ([WF])
│
├── docs/                                 # เอกสารเทคนิค CI/CD และ Cloud Architecture
│   ├── CI_CD/                            # พอร์ทัลเอกสาร CI/CD Pipeline & Quality Gates
│   │   ├── README.md                     # ภาพรวมจังหวะการรัน Test และ CI/CD Portal
│   │   ├── ci_cd_pipelines_overview.md   # ภาพรวม Pipeline ของระบบ
│   │   ├── ci_cd_quality_gates_report.md # รายงาน Quality Gates
│   │   ├── jenkins_cicd_comprehensive_guide.md # คู่มือ Jenkins CI/CD ฉบับสมบูรณ์
│   │   ├── DockerBuild/                  # คู่มือ Docker Multi-Stage Build & Containerization
│   │   ├── E2E/                          # คู่มือ Cypress E2E Testing (4 Journeys + Custom Commands)
│   │   ├── Security Audit/               # คู่มือ Security & Dependency Audit
│   │   └── Unitest/                      # เอกสาร Unit & Component Tests (Frontend / Backend)
│   └── Cloud_Database/
│       └── spring_boot_local_vs_cloud_db.md # คู่มือการสลับ Local DB vs Cloud DB (12-Factor App)
│
├── Code_devops/                          # (Local Workspace) ซอร์สโค้ด Backend, Frontend และเอกสาร
│   ├── tcg-store-backend/                # Spring Boot Backend Service
│   ├── tcg-store-frontend/               # React + Vite Frontend Service
│   └── tcg-store-document/               # เอกสารประกอบโค้ด
│
├── docker-compose.yml                    # Full-Stack Orchestration (Postgres + Backend + Frontend)
├── docker-compose.jenkins.yml            # Docker Compose สำหรับรัน Jenkins Server (JDK 21)
├── Jenkinsfile                           # Pipeline อัตโนมัติสำหรับ Full-Stack Build, Test & Compose Check
└── README.md                             # คำอธิบายโครงสร้างโปรเจกต์และเอกสารอ้างอิง
```

---

## 📌 สรุปรายละเอียดแต่ละส่วน

### 1. `Architecture/`
รวบรวมเอกสารทางด้านข้อกำหนดและการวิเคราะห์เชิงเทคนิค
- **`CORE_REQUIREMENTS_CROSSCHECK.md`**: เอกสาร Cross-check ระหว่าง Requirement บังคับของรายวิชากับสถานะการออกแบบและพัฒนาจริง (Auth, Catalog, Cart, Order, Seller Dashboard, Cost/Profit calculation, Fulfillment, Inventory)
- **`DATABASE_DESIGN.md`**: เอกสารสถาปัตยกรรมฐานข้อมูล **Revision 5** บน PostgreSQL 16 (10 ตารางหลัก ตามหลัก 3NF + Snapshot Pattern, Seller KYC Gate, Audit Trail, Collection Privacy และ Order Parcel Tracking) พร้อม ER Diagram ทั้งแบบรูปภาพ 4K (`database_er_diagram.png`) และ Interactive HTML (`database_architecture_detailed.html`)

### 2. `FIgma/`
รวบรวมการออกแบบ UI/UX, Style Guide และโครงสร้างหน้าจอทั้งหมด
- **`UI_FRAMES_CATALOG.md` & `FIGMA_UI_TODO.md`**: บันทึกรายการ Frame ทั้งหมดกว่า 70+ Frames พร้อม Checklist สถานะการออกแบบ
- **`SVG/` & `figma_pics/`**: แบ่งโฟลเดอร์ย่อยตาม Module (`auth`, `Shop & Browse`, `Checkout Flow`, `seller`, `profile`, `Buyer Account & Storefront`, `platform-admin`) เพื่อให้ง่ายต่อการนำไปพัฒนา Frontend

### 3. `User Story & Flow/`
รวบรวมสเปกและพฤติกรรมผู้ใช้ของระบบ แบ่งเป็น 2 เฟสหลัก:
- **Phase 1 (`USER_STORIES.md`):** สเปกความต้องการของระบบ Core Marketplace (US-01 ถึง US-12 รวม **43 ข้อ** พร้อมสถานะ Implemented และไฟล์ Flow)
- **Phase 2 (`final_user_story_phase_2.md` & `check-process-phase2.md`):** ข้อกำหนดฉบับสุดท้ายและการติดตามสถานะพัฒนา (ระบบประมูลการ์ด US-13–US-19, รูปถ่ายจริง US-20, โปรโมชัน US-24, แจ้งเตือน/พยากรณ์สต๊อก US-26, รายงานแอดมิน US-27, แจ้งเตือนอีเมล 16 เหตุการณ์ US-29 รวมถึงฟีเจอร์เสริมที่พัฒนาแล้วอย่าง US-21, US-22, US-25, US-28)
- **`User Flow/`**: แผนผัง User Flow (`.pdf`) และ Wireframe (`[WF]`) ครอบคลุมทั้ง Phase 1 (US-01 ถึง US-12) และ Phase 2 (US-13, US-18)

### 4. `Docker_compose_DB/` & Full-Stack DevOps (`docker-compose.yml`, `Jenkinsfile`)
เครื่องมือจำลองฐานข้อมูลและระบบ Orchestration สำหรับพัฒนาและทดสอบ
- **`Docker_compose_DB/`**: คู่มือและไฟล์ `docker-compose.yml` สำหรับรัน PostgreSQL 16 เฉพาะตัวฐานข้อมูล พร้อมสคริปต์ `01-schema.sql` และ `02-data.sql` (รองรับข้อมูลตัวอย่าง Parcel Tracking และ Collection Privacy)
- **`docker-compose.yml` (Root)**: รันระบบ Full-Stack ครบชุด ได้แก่ `tcg_postgres` (Port `5432`), `tcg_backend` (Spring Boot Port `8080`), และ `tcg_frontend` (Nginx Port `3000`)
- **`docker-compose.jenkins.yml` & `Jenkinsfile`**: สำหรับรัน Jenkins (`jenkins/jenkins:lts-jdk21` บน Port `8088`) และ Pipeline ทดสอบแบบ Parallel (Backend `./mvnw clean test`, Frontend `npm run audit` / `npm test` / `npm run build`, และ `docker compose config`)

### 5. `docs/`
พอร์ทัลเอกสารด้าน DevOps, Quality Gates และ Cloud Architecture
- **`docs/CI_CD/`**: รวมคู่มือ **Unit Test** (Vitest + RTL / JUnit 5), **E2E Test** (Cypress 4 Journeys), **Security & Dependency Audit**, **Docker Multi-Stage Build**, และ **Jenkins CI/CD Guide**
- **`docs/Cloud_Database/spring_boot_local_vs_cloud_db.md`**: อธิบายกลไกการสลับเชื่อมต่อ Local PostgreSQL กับ Cloud Database (เช่น Neon) ผ่าน Environment Variables ใน `application.yml`

---

## 🗺️ แผนผัง User Stories (US Overview)

### Phase 1 — Core Marketplace (US-01 – US-12)
| รหัส | ขอบเขตการทำงาน (Feature Scope) | รายละเอียด Flow / UI ที่รองรับ |
| :--- | :--- | :--- |
| **US-01** | User Authentication | สมัครสมาชิก, เข้าสู่ระบบ, กู้คืนรหัสผ่าน, Logout |
| **US-02** | Browse & Search Cards | ค้นหาการ์ด, กรองหลายเงื่อนไข, เทียบผู้ขาย, การ์ดแนะนำ, หน้าแรก |
| **US-03** | Shopping Cart Management | เพิ่มลงตะกร้า, ปรับเพิ่ม/ลดจำนวน (Clamped to Stock), ลบสินค้า |
| **US-04** | Order Placement | สั่งซื้อจากตะกร้า และสั่งซื้อทันที (Buy Now) แบบ Reservation-Based |
| **US-05** | Inventory & Listing CRUD | ผู้ขายเพิ่ม/แก้ไข/ลบการ์ด, ซ่อน/แสดงสินค้า, จัดการคลังสินค้า |
| **US-06** | Seller Dashboard & Storefront | สรุปยอดขาย, กำไร/ต้นทุน, สถิติคำสั่งซื้อ, ตั้งค่าหน้าร้านสาธารณะ |
| **US-07** | Order Management | ผู้ขายตรวจสอบรายการคำสั่งซื้อ, ปรับสถานะการจัดส่งและเลขพัสดุ |
| **US-08** | User Profile Management | แก้ไขชื่อ ที่อยู่ เบอร์โทรศัพท์ และข้อมูลติดต่อ |
| **US-09** | Order History & Tracking | ผู้ซื้อดูประวัติการสั่งซื้อ และตรวจสอบสถานะ/เลขพัสดุการจัดส่ง |
| **US-10** | Card Collection & Verification | ระบบ Collection การ์ดสะสม, ยื่นยืนยันตัวตน Seller (KYC), Leaderboard |
| **US-11** | In-App Notifications | ระบบแจ้งเตือนในระบบ (Badge แจ้งเตือน, จองการ์ด, อัปเดตสถานะ) |
| **US-12** | Platform Administration | Admin Dashboard, คิวอนุมัติ Seller, จัดการผู้ใช้/สิทธิ์, Audit & Order Logs |

### Phase 2 — Card Auction & Extended Features (Final Scope)
| รหัส | ขอบเขตการทำงาน (Feature Scope) | ระดับความสำคัญ | รายละเอียดสำคัญ |
| :--- | :--- | :---: | :--- |
| **US-13** | Auction Listing & Setup | ⭐ **MUST HAVE** | สร้างรายการประมูล, Reserve Price, Buy-It-Now, ตั้งเวลา และยกเลิกก่อนกำหนด |
| **US-18** | Auction Analytics & Financials | ⭐ **MUST HAVE** | สถิติรายได้/กำไรสุทธิผู้ขาย, ค่าธรรมเนียมแพลตฟอร์ม, สถิติการชนะประมูลผู้ซื้อ |
| **US-20** | Card Image Upload Policy | 🚀 **RECOMMENDED** | เกณฑ์บังคับอัปโหลดภาพถ่ายจริงตามมูลค่าและสภาพการ์ด และ Zoom Magnifier |
| **US-24** | Promotions & Discount Codes | 🚀 **RECOMMENDED** | ระบบคูปองและโค้ดส่วนลดในขั้นตอน Checkout และระบบจัดการ Voucher |
| **US-26** | Out-of-Stock & Restock Prediction | 🚀 **RECOMMENDED** | แจ้งเตือนสินค้าหมดสต๊อก และพยากรณ์การเติมสต๊อก (Smart Restock Prediction) |
| **US-27** | Weekly Stock & Profit Admin Report | 🚀 **RECOMMENDED** | รายงานสรุปสินค้าคงคลังและกำไรรายสัปดาห์สำหรับผู้ดูแลระบบ |
| **US-29** | Multi-Channel Email & In-App Alerts | 🚀 **RECOMMENDED** | ระบบแจ้งเตือนในเว็บและอีเมลอัตโนมัติ (Transactional Outbox) 16 เหตุการณ์สำคัญ |
| **US-14, US-15, US-17, US-19** | Live Arena, Bidding, Settlement & Admin | 💡 **GOOD TO HAVE** | ห้องประมูลสด (WebSocket), Auto-Bid, ตัดสินผู้ชนะ/โอนเข้า Binder และศูนย์จัดการข้อพิพาท |
| **US-21, US-22, US-25, US-28** | Extended E-Commerce Features | ✅ **IMPLEMENTED** | ค่าธรรมเนียม Escrow & กราฟรายเดือน, Privacy Showcase, 1-Click Reorder/PDF, ค้นหาภาษาไทย/Typo-Tolerant |

---

## 🚀 การเริ่มต้นใช้งาน (Quick Start)

### รันเฉพาะฐานข้อมูล Local PostgreSQL
ดูรายละเอียดเพิ่มเติมใน [Docker_compose_DB/LOCAL_DATABASE_GUIDE.md](Docker_compose_DB/LOCAL_DATABASE_GUIDE.md)
```bash
docker compose -f Docker_compose_DB/docker-compose.yml up -d
```

### รันระบบ Full-Stack (Database + Backend + Frontend)
*(ต้องมีซอร์สโค้ดอยู่ใน `Code_devops/tcg-store-backend` และ `Code_devops/tcg-store-frontend`)*
```bash
docker compose up -d --build
```
- **Frontend:** `http://localhost:3000`
- **Backend API:** `http://localhost:8080`
- **PostgreSQL:** `localhost:5432`

### รัน Jenkins CI Server (ทางเลือก)
```bash
docker compose -f docker-compose.jenkins.yml up -d
```
- **Jenkins UI:** `http://localhost:8088`

---

## 🤝 การมีส่วนร่วมและแนวทางการใช้งาน

1. **การอัปเดต User Flow:** บันทึกไฟล์แผนผังหรือหน้าจอล่าสุดไว้ในโฟลเดอร์ `User Story & Flow/User Flow/`
2. **การอัปเดต UI/UX:** นำภาพที่ Export จาก Figma มาบันทึกไว้ใน `FIgma/SVG/<module>/` และ `FIgma/figma_pics/<module>/` ให้ตรงตามหมวดหมู่
3. **เอกสาร CI/CD & Testing:** ศึกษาแนวทางการทดสอบ (Unit Test, Cypress E2E, Security Audit) ได้ที่ [docs/CI_CD/README.md](docs/CI_CD/README.md)
4. **การติดตามความรับผิดชอบ:** อ้างอิงและอัปเดตสถานะงานตาม [DACI Framework บน Canva](https://canva.link/jze669c3fkham3h)
