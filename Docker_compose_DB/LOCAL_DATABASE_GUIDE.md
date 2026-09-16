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

## 📊 2. สรุปข้อมูลตั้งต้นในฐานข้อมูล (Seed Data Revision 5)

### 🎴 การ์ด Pokémon กลาง (`global_cards` รวม 2,000 ใบ)
- ดึงข้อมูลจาก Official Pokémon TCG API โดยตรง (Master Catalog - Ownerless)
- คละความหายาก: Common, Uncommon, Rare, Rare Holo, Promo, EX, V, VMAX
- รองรับประเภท: Pokémon, Trainer, Energy

### 👥 บัญชีผู้ใช้ตัวอย่าง (`users` - รหัสผ่าน `password123` ทุกบัญชี)

| Role | Email | รหัสผ่านจริง | seller_status | คำอธิบาย |
| :--- | :--- | :--- | :--- | :--- |
| **Admin** | `admin@mythix.com` | `password123` | `NONE` | Platform Administrator สำหรับตรวจ Audit Log, อนุมัติผู้ขาย, จัดการการ์ด Global |
| **Seller (อนุมัติแล้ว)** | `seller@mythix.com` | `password123` | `APPROVED` | บัญชีร้านค้า *"Pewter City Card Vault"* (Brock) มีสต๊อกสินค้าลงขายแล้ว 20 รายการ |
| **Seller (รออนุมัติ KYC)**| `misty@mythix.com` | `password123` | `PENDING` | บัญชีผู้ขายยื่นเอกสารบัตรประชาชนและบัญชีธนาคารแล้ว รอแอดมินกดอนุมัติ |
| **Buyer (ลูกค้า)** | `buyer@mythix.com` | `password123` | `NONE` | ลูกค้าทั่วไป (Ash Ketchum) มีไอเทมในตะกร้าและประวัติการสั่งซื้อ |
| **Collector (นักสะสม)**| `red@mythix.com` | `password123` | `NONE` | ผู้ใช้ที่มีการ์ดในแฟ้มสะสมส่วนตัว (`collection_items`) |

### 🏷️ สินค้าลงขายจริงของร้านค้า (`local_cards` 20 รายการ)
- สินค้าเป็นกรรมสิทธิ์ของผู้ขาย Brock (`seller_id = 2`) ผูกกับ `global_card_id`
- ระบุสภาพการ์ดตามมาตรฐาน: `NM` (Near Mint), `LP` (Lightly Played)
- มีราคากลาง, ราคาขายจริง (`price`), ต้นทุน (`cost`), สต๊อก (`on_hand`), และยอดจอง (`reserved`)

### 📦 ประวัติคำสั่งซื้อและไทม์ไลน์ (`orders`, `order_items`, `order_status_logs`)
- มีคำสั่งซื้อตัวอย่าง `ORD-2026-001` (สถานะ `FULFILLED`) และ `ORD-2026-002` (สถานะ `PAID`)
- มีบันทึก Event Timeline ทุกขั้นตอน พร้อม Tracking Number สำหรับทดสอบแสดงผลบนหน้าเว็บ

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
