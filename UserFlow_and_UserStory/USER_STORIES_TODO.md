# Mythix TCG Platform - User Stories To-Do List

## 🟢 กลุ่มที่ 1: US ที่ต้องแก้ไข (Modify)
- [x] **US-04-1: Place order from cart**
  *(ต้องแก้ไขให้: รื้อหน้า Checkout ทิ้ง ตัดที่อยู่จัดส่ง การจ่ายเงิน ภาษี และค่าจัดส่งออก เหลือแค่หน้าสรุปรายการสินค้า กดยืนยันเพื่อจองสต๊อก และแสดงข้อมูลสำหรับติดต่อ Seller หลังกดสั่งซื้อ)*
- [x] **US-04-2: Place order from product page (Buy Now)**
  *(ต้องแก้ไขให้: เหมือนกับ US-04-1 คือตัดระบบ Payment/Shipping ทิ้งทั้งหมด)*
- [x] **US-05-1 ถึง US-05-6: CRUD Inventory Management**
  *(ต้องแก้ไขให้: เปลี่ยนสิทธิ์จากที่ Admin คุมทั้งระบบ เป็นระบบเช็ค `sellerId` ให้ Seller สามารถจัดการ (Add, Edit, Delete, Hide) และมองเห็นได้เฉพาะสินค้าของร้านตัวเองเท่านั้น)*
- [x] **US-06-1: Admin Dashboard System**
  *(ต้องแก้ไขให้: เปลี่ยนจากหน้าแสดงกราฟ Report ของทั้งระบบ เป็น "Seller Dashboard" ส่วนตัวของร้าน และเพิ่มระบบคำนวณ Cost/profit (Estimated Sales & Profit) ต่อชิ้นหรือต่อออเดอร์แทน)*
- [x] **US-07-1 ถึง US-07-2: Order Management System**
  *(ต้องแก้ไขให้: Seller ดูได้เฉพาะ Order ที่สั่งสินค้าของตัวเอง และตอนกดอัปเดตสถานะ (Pending -> Fulfilled / Cancelled) ให้ตัดช่อง "กรอกเลขพัสดุ (Tracking No.)" และปุ่ม "พิมพ์ใบปะหน้า" ออกทั้งหมด)*
- [x] **US-08-1, US-08-3, US-08-4: User Profile System**
  *(ต้องแก้ไขให้: เปลี่ยนบริบทจากคำว่า "Shipping Address (ที่อยู่จัดส่ง)" เป็น "Contact Information (ข้อมูลการติดต่อ)" เพื่อให้แพลตฟอร์มมีช่องทางติดต่อของผู้ซื้อและผู้ขายไว้แสดงให้ทั้งสองฝ่ายทักไปคุยกันเอง)*

## 🔵 กลุ่มที่ 3: US ที่ต้องเพิ่มใหม่ (Add - เปลี่ยนเป็น US-10)
- [x] **US-10-1: View Collection (ดูรายการสะสม)**
  * As a user, I want to view my personal card collection.
- [x] **US-10-2: Add to Collection (เพิ่มการ์ดเข้าคอลเลกชัน)**
  * As a user, I want to add cards from the TCG API Database to my collection.
- [x] **US-10-3: Remove from Collection (ลบการ์ดออก)**
  * As a user, I want to remove cards I no longer own from my collection.
- [x] **US-10-4: Self-serve Seller Verification (ระบบสมัครผู้ขายอัตโนมัติ)**
  * As a customer, I want to fill out a seller profile form and get instantly verified so that I can start selling my cards without waiting for manual admin approval.
- [x] **US-10-5: Stock Reservation Semantics (ระบบจองสต๊อก)**
  * As a system, I want to validate cart quantity against `onHand - reserved` stock and reserve the stock when an order is placed, so that overselling is prevented.
- [ ] **US-10-6: หน้า admin สำหรับการ monitor (เกิน requirement)**
  * จำนวน user และ seller ทั้งหมด , จำนวนการซื้อขายทั้งหมด , เก็บ LOG การซื้อขาย


## ✅ กลุ่มที่ 4: US ที่คงไว้เหมือนเดิม (Keep - ทำใน Flow เดิมเสร็จแล้ว)
- [x] **US-01-1:** Registration & Login System (Customer register & login)
- [x] **US-02-1:** Browse Products System (Browse TCG cards with filters)
- [x] **US-03-1:** Shopping Cart System (Add cards to cart)
- [x] **US-03-2:** Shopping Cart System (Delete cards from cart)
- [x] **US-03-3:** Shopping Cart System (Decrease amount of cards)
- [x] **US-03-4:** Shopping Cart System (Increase amount of cards)
- [x] **US-09-1:** Order History System (View all of my orders)
- [x] **US-09-2:** Order History System (Filter order by status)

## 🔴 กลุ่มที่ 2: US ที่ถูกลบทิ้งจากระบบ (Delete)
- ~[ ] US-01-2: Admin login (ไม่มี Admin กลางแล้ว)~
- ~[ ] US-08-2: Add new address (ไม่ต้องเก็บที่อยู่หลายที่เพราะไม่ส่งของแล้ว)~
