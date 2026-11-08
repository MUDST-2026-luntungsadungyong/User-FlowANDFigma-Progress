# 🐳 คู่มือการติดตั้งและใช้งาน Docker Compose (Full Stack & Database)
### Mythix TCG Platform (DevOps Tasks: DO-01, DO-04, DO-05)

> เอกสารแนะนำการติดตั้งและใช้งานระบบ Mythix TCG Platform แบบครบวงจร (**PostgreSQL 16**, **Spring Boot Backend**, **React/Vite Frontend**)  
> รองรับทั้งการรันแบบ **Full Stack (Frontend + Backend + DB)** และการรันเฉพาะ **Database Only** สำหรับ Local Development

---

## 📁 1. โครงสร้างไฟล์และหน้าที่ของแต่ละส่วน

```text
c:\Devops_NEW\
├── docker-compose.yml              # ควบคุม Full Stack (Frontend + Backend + Postgres)
├── Docker_compose_DB\
│   ├── docker-compose.yml          # ควบคุม Full Stack จากโฟลเดอร์นี้
│   ├── LOCAL_DATABASE_GUIDE.md     # คู่มือฉบับนี้
│   └── init-db\
│       ├── 01-schema.sql           # โครงสร้างฐานข้อมูล 10 ตาราง (Revision 5)
│       └── 02-data.sql             # Seed Data การ์ด 2,000 ใบ + Users (Admin, Buyer, Seller)
├── Code_devops\
│   ├── tcg-store-backend\          # Spring Boot 3.3.4 (Java 21) + Dockerfile
│   └── tcg-store-frontend\         # React + Vite + Tailwind + Nginx + Dockerfile
```

---

## 📊 2. สรุปข้อมูลตั้งต้นในฐานข้อมูล (Seed Data Revision 6 - Enhanced)

### 🎴 การ์ด Pokémon กลาง (`global_cards` รวม 2,000 ใบ)
- ดึงข้อมูลจาก Official Pokémon TCG API โดยตรง (Master Catalog - Ownerless)
- คละความหายาก: Common, Uncommon, Rare, Rare Holo, Promo, EX, V, VMAX
- รองรับประเภท: Pokémon, Trainer, Energy

### 👥 บัญชีผู้ใช้ตัวอย่าง (`users` 20 บัญชี - รหัสผ่าน `password123` ทุกบัญชี)

| Role | Email | รหัสผ่านจริง | seller_status | คำอธิบาย |
| :--- | :--- | :--- | :--- | :--- |
| **Admin** | `admin@mythix.com` | `password123` | `NONE` | Platform Administrator สำหรับตรวจ Audit Log, อนุมัติ/ปฏิเสธ KYC ผู้ขาย, จัดการการ์ด Global |
| **Seller (อนุมัติแล้ว)** | `seller@mythix.com` | `password123` | `APPROVED` | ร้าน *"Pewter City Card Vault"* (Brock) มีสต๊อกสินค้าลงขาย 20 รายการ |
| **Seller (อนุมัติแล้ว)** | `blaine@mythix.com` | `password123` | `APPROVED` | ร้าน *"Cinnabar Volcano TCG"* (Blaine) เชี่ยวชาญการ์ดประเภท Fire/EX 15 รายการ |
| **Seller (อนุมัติแล้ว)** | `giovanni@mythix.com` | `password123` | `APPROVED` | ร้าน *"Viridian Syndicate Cards"* (Giovanni) การ์ด High-End/Vintage 15 รายการ |
| **Seller (รออนุมัติ KYC)**| `misty@mythix.com` | `password123` | `PENDING` | ร้าน *"Cerulean Water Gym Cards"* (ยื่นเอกสาร 4 วันก่อน รอแอดมินกดอนุมัติ) |
| **Seller (รออนุมัติ KYC)**| `erika@mythix.com` | `password123` | `PENDING` | ร้าน *"Celadon Flower Garden Cards"* (ยื่นเอกสาร 2 วันก่อน รอแอดมินกดอนุมัติ) |
| **Seller (รออนุมัติ KYC)**| `sabrina@mythix.com` | `password123` | `PENDING` | ร้าน *"Saffron Psychic Vault"* (ยื่นเอกสาร 1 วันก่อน รอแอดมินกดอนุมัติ) |
| **Seller (ถูกปฏิเสธ KYC)**| `jessie@mythix.com` | `password123` | `REJECTED` | ร้าน *"Rocket Secret Vault"* (โดน Reject: ภาพบัตรประชาชนไม่ชัดเจน/ชื่อไม่ตรง) |
| **Seller (ถูกปฏิเสธ KYC)**| `james@mythix.com` | `password123` | `REJECTED` | ร้าน *"Kojiro Luxury Binder"* (โดน Reject: เอกสารหน้าสมุดบัญชีธนาคารไม่สมบูรณ์) |
| **Buyer / VIP** | `leon@mythix.com` | `password123` | `NONE` | ลูกค้ากระเป๋าหนัก (Leon Champion) ประวัติสั่งซื้อการ์ดระดับ 30,000+ บาท |
| **Buyer (ลูกค้าประจำ)** | `buyer@mythix.com` | `password123` | `NONE` | ลูกค้าทั่วไป (Ash Ketchum) มีไอเทมในตะกร้าและประวัติการสั่งซื้อ |
| **Buyer / Collector** | `dawn@mythix.com`, `serena@mythix.com`, `may@mythix.com`, `volkner@mythix.com` | `password123` | `NONE` | ลูกค้าหลากหลายสายสะสม มีคำสั่งซื้อครบทุกสถานะ |
| **Collector (นักสะสม)**| `red@mythix.com`, `cynthia@mythix.com`, `steven@mythix.com`, `lance@mythix.com`, `gary@mythix.com` | `password123` | `NONE` | ผู้ใช้ที่มีการ์ดในแฟ้มสะสมส่วนตัว (`collection_items`) |

### 🏷️ สินค้าลงขายจริงของร้านค้า (`local_cards` รวม 50 รายการจาก 3 ร้านค้า)
- **ร้าน Brock (ID 2):** 20 รายการ (การ์ดทั่วไป, Holo, Promo)
- **ร้าน Blaine (ID 12):** 15 รายการ (เน้นการ์ด Fire, Charizard, Arcanine)
- **ร้าน Giovanni (ID 13):** 15 รายการ (การ์ดสะสม High-End เช่น Charizard 1st Ed มูลค่า 31,401.65 บาท, Dark Blastoise, Dark Dragonite)

### 📦 ประวัติคำสั่งซื้อและเงินในระบบ (`orders`, `order_items`, `order_status_logs` รวม 21 คำสั่งซื้อ)
- **ยอดเงินหมุนเวียนรวม (Platform GMV):** กว่า **75,000+ บาท**
- **ค่าธรรมเนียมแพลตฟอร์ม (Platform Fee 5%):** รวมกว่า **3,700+ บาท**
- **ยอดเงินสุทธิที่ผู้ขายได้รับ (Seller Net Payout 95%):** รวมกว่า **71,000+ บาท**
- **สถานะคำสั่งซื้อครอบคลุมทุกวงจร:**
  - `FULFILLED` (สำเร็จ 10 รายการ)
  - `SENT` (กำลังจัดส่ง 3 รายการ มี Tracking: Kerry, Flash, EMS)
  - `CONFIRMED` (ชำระเงินแล้ว รอจัดส่ง 3 รายการ)
  - `PENDING` (รอชำระเงิน 3 รายการ)
  - `CANCELLED` (ยกเลิก 2 รายการ จากหมดเวลาชำระเงิน หรือลูกค้ายกเลิก)
- **บันทึกไทม์ไลน์ Event (34 logs):** แสดงขั้นตอนละเอียดตั้งแต่สร้างออเดอร์, ยืนยันชำระเงิน, เลขพัสดุ, จนถึงลูกค้าได้รับของ


---

## 🚀 3. ขั้นตอนการรันระบบด้วย Docker Compose

### วิธีที่ 1: รันทั้งระบบแบบครบวงจร (Full Stack: Frontend + Backend + Database)
เปิด Terminal ในโฟลเดอร์ `c:\Devops_NEW\` แล้วสั่ง:

```bash
docker compose up -d --build
```

* **Frontend Web:** เข้าผ่านเบราว์เซอร์ได้ที่ [http://localhost:3000](http://localhost:3000)
* **Backend REST API:** เข้าถึงได้ที่ [http://localhost:8080/api](http://localhost:8080/api)
* **Database (PostgreSQL 16):** พอร์ต `5432`

---

### วิธีที่ 2: รันเฉพาะ Database (สำหรับนักพัฒนาที่รันโค้ดบน IDE เครื่องตัวเอง)
หากต้องการรันเฉพาะเซิร์ฟเวอร์ฐานข้อมูล PostgreSQL:

```bash
docker compose up -d postgres
```

ตรวจสอบสถานะ:
```bash
docker compose ps
```

---

## 🛠️ 4. ข้อมูลการเชื่อมต่อฐานข้อมูล (Connection Config)

นำข้อมูลนี้ไปใช้ในโปรแกรมจัดการฐานข้อมูล (DBeaver, DataGrip, pgAdmin) หรือ `application.yml`:

* **Host:** `localhost`
* **Port:** `5432`
* **Database Name:** `tcg_store`
* **Username:** `postgres`
* **Password:** `postgres`
* **JDBC URL:** `jdbc:postgresql://localhost:5432/tcg_store`

---

## 🛑 5. คำสั่งจัดการอื่นๆ

* **ปิดการทำงานทั้งหมด:** `docker compose down`
* **ลบข้อมูลใน Database เพื่อเริ่มใหม่หมดจด:** `docker compose down -v`
* **ดู Logs ของระบบ:** `docker compose logs -f` หรือ `docker compose logs -f backend`
