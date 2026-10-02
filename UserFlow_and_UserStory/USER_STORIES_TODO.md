# Mythix TCG Platform - User Stories To-Do List

## 🟢 กลุ่มที่ 1: US ที่ต้องแก้ไข (Modify)

| Status | User Story | Description | User Flow |
|--------|------------|-------------|-----------|
| ✅ | **US-04-1:** Place order from cart | รื้อหน้า Checkout ทิ้ง ตัดระบบ Payment/Shipping ออก เหลือแค่หน้าสรุปรายการสินค้า | [Page 10](../User%20flow/flow_page_10.png) |
| ✅ | **US-04-2:** Place order from product page | เหมือน US-04-1 (ตัดระบบ Payment/Shipping ทิ้งทั้งหมด) | [Page 10](../User%20flow/flow_page_10.png) |
| ✅ | **US-05-1 ถึง US-05-6:** CRUD Inventory | Seller จัดการได้เฉพาะสินค้าของร้านตัวเองเท่านั้น | [Page 1](../User%20flow/flow_page_1.png), [Page 2](../User%20flow/flow_page_2.png) |
| ✅ | **US-06-1:** Admin Dashboard System | เปลี่ยนเป็น "Seller Dashboard" ส่วนตัวของร้าน และเพิ่มระบบคำนวณ Cost/Profit | ❌ |
| ✅ | **US-07-1 ถึง US-07-2:** Order Management | Seller ดูได้เฉพาะ Order ของตัวเอง และตัดช่องกรอกเลขพัสดุออก | [Page 7](../User%20flow/flow_page_7.png), [Page 8](../User%20flow/flow_page_8.png) |
| ✅ | **US-08-1, 08-3, 08-4:** User Profile | เปลี่ยนบริบท "Shipping Address" เป็น "Contact Information" | [Page 6](../User%20flow/flow_page_6.png) |

## 🔵 กลุ่มที่ 3: US ที่ต้องเพิ่มใหม่ (Add - เปลี่ยนเป็น US-10)

| Status | User Story | Description | User Flow |
|--------|------------|-------------|-----------|
| ✅ | **US-10-1:** View Collection | ดูรายการสะสมการ์ดส่วนตัว | ❌ |
| ✅ | **US-10-2:** Add to Collection | เพิ่มการ์ดเข้าคอลเลกชันจาก TCG API Database | ❌ |
| ✅ | **US-10-3:** Remove from Collection | ลบการ์ดออกจากคอลเลกชัน | ❌ |
| ✅ | **US-10-4:** Seller Verification | ระบบสมัครและยืนยันตัวตนผู้ขายอัตโนมัติ | [Page 9](../User%20flow/flow_page_9.png) |
| ✅ | **US-10-5:** Stock Reservation | ระบบจองสต๊อกชั่วคราว ป้องกัน overselling | [Page 10](../User%20flow/flow_page_10.png) |
| ✅ | **US-10-6 / US-12:** Admin Monitoring | Dashboard, User/Order stats, Audit Logs | [Page 11-17](../User%20flow/flow_page_11.png) |

> 📖 **เอกสารฉบับสมบูรณ์ (Complete Specification):** อ่าน User Stories ทั้งหมด 38 ข้อได้ที่ [USER_STORIES.md](./USER_STORIES.md)

## ✅ กลุ่มที่ 4: US ที่คงไว้เหมือนเดิม (Keep - ทำใน Flow เดิมเสร็จแล้ว)

| Status | User Story | Description | User Flow |
|--------|------------|-------------|-----------|
| ✅ | **US-01-1:** Registration & Login | ระบบสมัครสมาชิกและเข้าสู่ระบบ | ❌ |
| ✅ | **US-02-1:** Browse Products | ระบบค้นหาและกรองการ์ด | [Page 5](../User%20flow/flow_page_5.png) |
| ✅ | **US-03-1 ถึง 4:** Shopping Cart | ระบบตะกร้าสินค้า เพิ่ม/ลด/ลบ จำนวน | [Page 3](../User%20flow/flow_page_3.png), [Page 4](../User%20flow/flow_page_4.png) |
| ✅ | **US-09-1 ถึง 2:** Order History | ดูประวัติคำสั่งซื้อทั้งหมด | ❌ |

## 🔴 กลุ่มที่ 2: US ที่ถูกลบทิ้งจากระบบ (Delete)
- ~[ ] US-01-2: Admin login (ไม่มี Admin กลางแล้ว)~
- ~[ ] US-08-2: Add new address (ไม่ต้องเก็บที่อยู่หลายที่เพราะไม่ส่งของแล้ว)~
