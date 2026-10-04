# 🎴 Mythix TCG Platform — System User Stories Specification

> **Repository:** `User-FlowANDFigma-Progress`  
> **Source Baseline:** Synchronized with `main` branches of `tcg-store-frontend` and `tcg-store-backend`  
> **Version:** 3.0 (Complete System Scope — Updated with 10 additional discovered features)  
> **Architecture Model:** C2C Trading & Reservation Marketplace (P2P Settlement & Logistics)

---

## 📌 Executive Summary

ระบบ **Mythix TCG Platform** เป็นแพลตฟอร์มศูนย์กลางสำหรับการซื้อขาย แลกเปลี่ยน ค้นหา และสะสมการ์ดเกม Trading Card Game (TCG) โดยมีจุดเด่นคือ:
1. **Reservation-Based Order:** สั่งซื้อสินค้าเพื่อทำการล็อกและจองสต๊อกสินค้าทันที (Atomic Stock Reservation) โดยการชำระเงินและการจัดส่งดำเนินงานแบบ Peer-to-Peer (นอกระบบ)
2. **Contact-Handoff:** มีช่องทางสำหรับแลกเปลี่ยนข้อมูลการติดต่อระหว่างผู้ซื้อและผู้ขาย (Contact Information)
3. **Automated Ownership Transfer:** เมื่อผู้ขายยืนยันว่าได้รับเงินและจัดส่งสินค้าแล้ว ระบบจะโอนกรรมสิทธิ์การ์ดใบนั้นเข้าสู่อัลบั้มคอลเลกชันส่วนตัวของผู้ซื้อโดยอัตโนมัติ
4. **Platform Administration & Security:** ระบบผู้ดูแลระบบส่วนกลาง (Platform Admin) สำหรับตรวจสอบ Audit Log, ดูประวัติ Order ทั่วทั้งระบบ และอนุมัติ/ตรวจสอบคำขอเป็นผู้ขาย

---

## 📊 ตารางสรุปภาพรวม User Stories ทั้งหมดในระบบ (48 ข้อ)

| รหัส US | ชื่อฟีเจอร์ (Feature Title) | ผู้ใช้หลัก (Actor) | ฝั่งที่เกี่ยวข้อง | สถานะ | สถานะ User Flow | ชื่อไฟล์ User Flow |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **US-01-1** | Customer Registration & Login | Customer | Frontend / Backend | ✅ Implemented | ❌ ยังไม่มี | - |
| **US-01-2** | Forgot & Reset Password Flow | Customer / Seller | Frontend / Backend | ✅ Implemented | ❌ ยังไม่มี | - |
| **US-01-3** | Seller Application Status Check | Customer / Seller | Frontend / Backend | ✅ Implemented | ❌ ยังไม่มี | - |
| **US-02-1** | Browse TCG Cards with Multi-Filters | Customer / Guest | Frontend / Backend | ✅ Implemented | ✅ มีแล้ว | US-02-1 - Browse TCG Cards with Multi-Filters.pdf |
| **US-02-2** | Multi-Seller Listing Comparison on Card Detail | Customer | Frontend / Backend | ✅ Implemented | ✅ มีแล้ว | US-03 - Shopping Cart System.pdf<br>[WF] US-03 - Shopping Cart System.pdf |
| **US-02-3** | Similar Cards Recommendation | Customer | Frontend | ✅ Implemented | ❌ ยังไม่มี | - |
| **US-02-4** | Homepage & Featured Cards Display | Guest / Customer | Frontend / Backend | ✅ Implemented | ❌ ยังไม่มี | - |
| **US-03-1** | Add Cards to Cart | Customer | Frontend / Backend | ✅ Implemented | ✅ มีแล้ว | US-03 - Shopping Cart System.pdf<br>[WF] US-03 - Shopping Cart System.pdf |
| **US-03-2** | Delete Cards from Cart | Customer | Frontend / Backend | ✅ Implemented | ✅ มีแล้ว | US-03 - Shopping Cart System.pdf<br>[WF] US-03 - Shopping Cart System.pdf |
| **US-03-3** | Decrease Quantity in Cart (Auto-remove at 0) | Customer | Frontend / Backend | ✅ Implemented | ✅ มีแล้ว | US-03 - Shopping Cart System.pdf<br>[WF] US-03 - Shopping Cart System.pdf |
| **US-03-4** | Increase Quantity in Cart (Clamped to Stock) | Customer | Frontend / Backend | ✅ Implemented | ✅ มีแล้ว | US-03 - Shopping Cart System.pdf<br>[WF] US-03 - Shopping Cart System.pdf |
| **US-04-1** | Place Order from Cart (Reservation-Based) | Customer | Frontend / Backend | ✅ Implemented | ❌ ยังไม่มี | - |
| **US-04-2** | Place Order Directly (Buy Now) | Customer | Frontend / Backend | ✅ Implemented | ❌ ยังไม่มี | - |
| **US-05-1** | Add Product Listing from Collection/Catalog | Seller | Frontend / Backend | ✅ Implemented | ❌ ยังไม่มี | - |
| **US-05-2** | Delete Product Listing | Seller | Frontend / Backend | ✅ Implemented | ❌ ยังไม่มี | - |
| **US-05-3** | Update Product Listing Details | Seller | Frontend / Backend | ✅ Implemented | ✅ มีแล้ว | US-05-3 - Update-Product.pdf<br>[WF] US-05-3 - Update-Product.pdf |
| **US-05-4** | View & Filter Seller Inventory List | Seller | Frontend / Backend | ✅ Implemented | ❌ ยังไม่มี | - |
| **US-05-5** | Toggle Listing Visibility (Show / Hide) | Seller | Frontend / Backend | ✅ Implemented | ❌ ยังไม่มี | - |
| **US-05-6** | Upload & Manage Product Image | Seller | Frontend / Backend | ✅ Implemented | ❌ ยังไม่มี | - |
| **US-06-1** | Seller Dashboard (Cost & Profit Metrics) | Seller | Frontend / Backend | ✅ Implemented | ❌ ยังไม่มี | - |
| **US-06-2** | Public Storefront & Custom Store Settings | Seller / Buyer | Frontend / Backend | ✅ Implemented | ❌ ยังไม่มี | - |
| **US-07-1** | View Seller Orders & Status Filter | Seller | Frontend / Backend | ✅ Implemented | ✅ มีแล้ว | US-07-2 - Update Order Status.pdf<br>[WF] US-07-2 - Update Order Status.pdf |
| **US-07-2** | Update Order Status (Pending → Fulfilled / Cancelled) | Seller | Frontend / Backend | ✅ Implemented | ✅ มีแล้ว | US-07-2 - Update Order Status.pdf<br>[WF] US-07-2 - Update Order Status.pdf |
| **US-07-3** | Automated Card Ownership Transfer | System / Buyer | Backend / Database | ✅ Implemented | ✅ มีแล้ว | US-07-2 - Update Order Status.pdf<br>[WF] US-07-2 - Update Order Status.pdf |
| **US-08-1** | Edit Contact Information | User | Frontend / Backend | ✅ Implemented | ✅ มีแล้ว | US-08 - Edit User Information.pdf |
| **US-08-2** | Edit Display Name | User | Frontend / Backend | ✅ Implemented | ✅ มีแล้ว | US-08 - Edit User Information.pdf |
| **US-08-3** | Edit Phone Number | User | Frontend / Backend | ✅ Implemented | ✅ มีแล้ว | US-08 - Edit User Information.pdf |
| **US-08-4** | Edit Profile Avatar | User | Frontend / Backend | ✅ Implemented | ❌ ยังไม่มี | - |
| **US-09-1** | View Buyer Order History | Customer | Frontend / Backend | ✅ Implemented | ✅ มีแล้ว | US-07-2 - Update Order Status.pdf<br>[WF] US-07-2 - Update Order Status.pdf |
| **US-09-2** | Filter Order History by Status | Customer | Frontend / Backend | ✅ Implemented | ✅ มีแล้ว | US-07-2 - Update Order Status.pdf<br>[WF] US-07-2 - Update Order Status.pdf |
| **US-10-1** | View Personal Collection Album | User | Frontend / Backend | ✅ Implemented | ❌ ยังไม่มี | - |
| **US-10-2** | Add Card to Collection from Catalog | User | Frontend / Backend | ✅ Implemented | ❌ ยังไม่มี | - |
| **US-10-3** | Remove Card from Collection | User | Frontend / Backend | ✅ Implemented | ❌ ยังไม่มี | - |
| **US-10-4** | Self-serve Seller Verification Form | Customer | Frontend / Backend | ✅ Implemented | ✅ มีแล้ว | US-10-4 - Seller Verification.pdf |
| **US-10-5** | Atomic Stock Reservation Semantics | System | Backend / Database | ✅ Implemented | ✅ มีแล้ว | US-10-5 - Atomic Stock Reservation Semantics.pdf |
| **US-10-6** | Public Collector Showcase & Leaderboard | User / Guest | Frontend / Backend | ✅ Implemented | ❌ ยังไม่มี | - |
| **US-10-7** | Add Card to Collection from Product Listing | User | Frontend / Backend | ✅ Implemented | ❌ ยังไม่มี | - |
| **US-11-1** | In-App Notifications Inbox & Status Alerts | User (All) | Frontend / Backend | ✅ Implemented | ❌ ยังไม่มี | - |
| **US-11-2** | Notification Badge & Unread Count | User (All) | Frontend | ✅ Implemented | ❌ ยังไม่มี | - |
| **US-12-1** | Platform Admin Dashboard & Metrics | Admin | Frontend / Backend | ✅ Implemented | ✅ มีแล้ว | US-12-1 - Platform Admin Dashboard & Metrics.pdf |
| **US-12-2** | Seller Application Review Queue | Admin | Frontend / Backend | ✅ Implemented | ✅ มีแล้ว | US-12-2 - Seller Application Review Queue.pdf |
| **US-12-3** | Admin User & Role Management | Admin | Frontend / Backend | ✅ Implemented | ✅ มีแล้ว | US-12-3 - Admin User & Role Management.pdf |
| **US-12-4** | Administrative & Security Audit Logs | Admin | Frontend / Backend | ✅ Implemented | ✅ มีแล้ว | US-12-4 - Administrative & Security Audit Logs.pdf |
| **US-12-5** | Platform-wide Order Logs Monitoring | Admin | Frontend / Backend | ✅ Implemented | ✅ มีแล้ว | US-12-5 - Platform-wide Order Logs Monitoring.pdf |
| **US-12-6** | Review Seller Application Decision | Admin | Frontend / Backend | ✅ Implemented | ✅ มีแล้ว | US-12-6 Review Seller Application Decision.pdf |

---

## 📑 รายละเอียดจำเพาะ User Stories แต่ละหมวดหมู่

### 🔐 หมวด US-01: Authentication & User Management
* **US-01-1: Customer Registration & Login**
  * **EN:** As a customer, I want to register and log in to the system using email and password so that I can access personalized features like Cart, Orders, and Collection.
  * **TH:** ในฐานะลูกค้า ฉันต้องการสมัครสมาชิกและเข้าสู่ระบบด้วยอีเมลและรหัสผ่าน เพื่อเข้าใช้งานฟังก์ชันเฉพาะตัวของระบบได้
  * **Key Criteria:** รหัสผ่านถูกเข้ารหัสด้วย BCrypt, ส่ง JWT Token ในการยืนยันตัวตน, มี Validation แจ้งเตือนเมื่อข้อมูลไม่ถูกต้อง
  * **Endpoints:** `POST /auth/register`, `POST /auth/login`, `GET /auth/me`

* **US-01-2: Forgot & Reset Password Flow**
  * **EN:** As a user who forgot my password, I want to request a password reset email and set a new password so that I can regain access to my account.
  * **TH:** ในฐานะผู้ใช้ที่ลืมรหัสผ่าน ฉันต้องการขอรับลิงก์รีเซ็ตรหัสผ่านและตั้งรหัสผ่านใหม่ เพื่อเข้าถึงบัญชีได้อีกครั้ง
  * **Endpoints:** `POST /auth/forgot-password`, `POST /auth/reset-password`

* **US-01-3: Seller Application Status Check**
  * **EN:** As a customer who has applied to become a seller, I want to check the current status of my seller application (Pending, Approved, or Rejected) from my profile so that I can track whether I have been approved.
  * **TH:** ในฐานะลูกค้าที่ได้ยื่นคำขอเปิดร้าน ฉันต้องการตรวจสอบสถานะของคำขอเป็นผู้ขาย (รออนุมัติ, อนุมัติแล้ว, ปฏิเสธ) จากหน้าโปรไฟล์ เพื่อติดตามว่าได้รับการอนุมัติหรือยัง
  * **Endpoints:** `GET /api/sellers/verify/status`
  * **UI Components:** `ProfileInfoSection`, `SellerVerificationPage`

---

### 🔍 หมวด US-02: Browse Products & Catalog Discovery
* **US-02-1: Browse TCG Cards with Multi-Filters**
  * **EN:** As a customer, I want to browse and search TCG cards with multiple filters (set, price, condition, rarity, stock) so that I can find the cards I want to purchase.
  * **TH:** ในฐานะลูกค้า ฉันต้องการค้นหาและกรองดูการ์ด TCG ทั้งหมดในระบบ (พร้อมรูปภาพ ราคา สภาพการ์ด) เพื่อหาสินค้าที่ตรงใจ
  * **Endpoints:** `GET /cards`, `GET /products`

* **US-02-2: Multi-Seller Listing Comparison on Card Detail**
  * **EN:** As a customer viewing a card detail page, I want to compare listings from multiple sellers offering that card so that I can choose the best offer based on price, condition, and seller rating.
  * **TH:** ในฐานะลูกค้าที่ดูรายละเอียดการ์ด ฉันต้องการเปรียบเทียบรายการขายการ์ดใบนี้จากผู้ขายแต่ละร้าน (ราคา สภาพ จำนวนคงเหลือ) เพื่อเลือกซื้อจากผู้ขายที่คุ้มค่าที่สุด
  * **UI Components:** `CardDetailPage`, `SellerOffersSection`, `SellerOfferRow`

* **US-02-3: Similar Cards Recommendation**
  * **EN:** As a customer, I want to see recommended similar cards on the card detail page so that I can discover related cards for my deck or collection.
  * **TH:** ในฐานะลูกค้า ฉันต้องการเห็นการ์ดแนะนำที่มีความเกี่ยวข้อง เพื่อช่วยในการค้นหาการ์ดเพิ่มเติมเข้าชุดสะสม

* **US-02-4: Homepage & Featured Cards Display**
  * **EN:** As a guest or customer, I want to see a visually engaging homepage with a hero banner, featured cards, and high-value card highlights so that I can discover trending content and navigate to browse or register.
  * **TH:** ในฐานะผู้เยี่ยมชมหรือลูกค้า ฉันต้องการเห็นหน้าแรกที่มี Hero Banner, การ์ดแนะนำ และการ์ดมูลค่าสูง เพื่อค้นพบสินค้าที่น่าสนใจและเข้าสู่ระบบหรือเริ่มเลือกซื้อ
  * **UI Components:** `HomePage` — Hero Section, Featured Cards Grid, Expensive Cards Showcase, CTA Sections
  * **Endpoints:** `GET /cards` (สำหรับดึงรายการการ์ดมาแสดงหน้าแรก)

---

### 🛒 หมวด US-03: Shopping Cart Management
* **US-03-1: Add Cards to Cart**
  * **EN:** As a customer, I want to add card listings to my cart so that I can collect items for checkout.
  * **TH:** ในฐานะลูกค้า ฉันต้องการเพิ่มการ์ดที่ต้องการซื้อลงในตะกร้าสินค้า
  * **Endpoints:** `POST /cart/items`

* **US-03-2: Delete Cards from Cart**
  * **EN:** As a customer, I want to remove items from my cart that I decide not to buy.
  * **TH:** ในฐานะลูกค้า ฉันต้องการลบสินค้าออกจากตะกร้าเมื่อไม่ต้องการซื้อ
  * **Endpoints:** `DELETE /cart/items/{listingId}`

* **US-03-3: Decrease Quantity in Cart**
  * **EN:** As a customer, I want to decrease item quantity in my cart, and automatically remove it if quantity reaches zero.
  * **TH:** ในฐานะลูกค้า ฉันต้องการลดจำนวนการ์ดในตะกร้าลงได้ (หากลดเหลือ 0 ให้ลบรายการออกอัตโนมัติ)
  * **Endpoints:** `PATCH /cart/items/{listingId}`

* **US-03-4: Increase Quantity in Cart**
  * **EN:** As a customer, I want to increase item quantity in my cart, clamped by available inventory (`onHand - reserved`).
  * **TH:** ในฐานะลูกค้า ฉันต้องการเพิ่มจำนวนการ์ดในตะกร้าได้ โดยไม่เกินจำนวนสต๊อกที่ว่างจริง

---

### 📦 หมวด US-04: Place Order & Reservation
* **US-04-1: Place Order from Cart (Reservation-Based)**
  * **EN:** As a customer, I want to review my order summary and confirm the order to atomically reserve stock and receive the seller's contact details for external payment and shipping.
  * **TH:** ในฐานะลูกค้า ฉันต้องการตรวจสอบรายการในตะกร้าและกดยืนยันสั่งซื้อเพื่อล็อกจองสต๊อกสินค้า พร้อมรับข้อมูลติดต่อของผู้ขายเพื่อนัดชำระเงินและรับสินค้า
  * **Endpoints:** `POST /orders` (supports `Idempotency-Key`)

* **US-04-2: Place Order Directly (Buy Now)**
  * **EN:** As a customer, I want to place an order directly from the product detail page (Buy Now) to reserve cards instantly without manual cart steps.
  * **TH:** ในฐานะลูกค้า ฉันต้องการกดสั่งซื้อทันที (Buy Now) จากหน้ารายละเอียดการ์ดเพื่อจองสินค้าได้โดยตรง

---

### 🏷️ หมวด US-05: Seller Inventory & Listing CRUD
* **US-05-1: Add Product Listing from Collection/Catalog**
  * **EN:** As a seller, I want to list a card for sale by selecting from my collection or catalog and setting the price, stock, and condition.
  * **TH:** ในฐานะผู้ขาย ฉันต้องการนำการ์ดจากคอลเลกชันหรือแคตตาล็อกมาวางขาย พร้อมกำหนดราคา จำนวน และสภาพการ์ด
  * **Endpoints:** `POST /seller/products`

* **US-05-2: Delete Product Listing**
  * **EN:** As a seller, I want to delete a product listing from my inventory, provided that no active pending orders exist for it.
  * **TH:** ในฐานะผู้ขาย ฉันต้องการลบสินค้าที่วางขาย (ระบบจะไม่อนุญาตถ้ามีออเดอร์ค้างรอชำระอยู่)
  * **Endpoints:** `DELETE /seller/products/{id}`

* **US-05-3: Update Product Listing Details**
  * **EN:** As a seller, I want to edit product details like price and available inventory.
  * **TH:** ในฐานะผู้ขาย ฉันต้องการแก้ไขราคาและจำนวนสต๊อกของการ์ดที่วางขายอยู่
  * **Endpoints:** `PUT /seller/products/{id}`

* **US-05-4: View & Filter Seller Inventory List**
  * **EN:** As a seller, I want to view and filter my inventory list by status, card name, and stock levels.
  * **TH:** ในฐานะผู้ขาย ฉันต้องการเปิดดูและกรองรายการสินค้าทั้งหมดของร้านตนเอง
  * **Endpoints:** `GET /seller/products`

* **US-05-5: Toggle Listing Visibility (Show / Hide)**
  * **EN:** As a seller, I want to toggle a product's visibility between `SHOW` and `HIDE` without deleting it.
  * **TH:** ในฐานะผู้ขาย ฉันต้องการเปิด/ปิดสถานะการมองเห็นของการ์ดบนหน้าร้านได้
  * **Endpoints:** `PATCH /seller/products/{id}/status`

* **US-05-6: Upload & Manage Product Image**
  * **EN:** As a seller, I want to upload and replace product images (JPEG, PNG, WEBP up to 5MB) for my listings so that buyers can see clear photos of the cards I'm selling.
  * **TH:** ในฐานะผู้ขาย ฉันต้องการอัปโหลดหรือเปลี่ยนรูปภาพสินค้า (JPEG, PNG, WEBP ขนาดไม่เกิน 5MB) สำหรับการ์ดที่วางขาย เพื่อให้ผู้ซื้อเห็นภาพถ่ายจริงของการ์ด
  * **Endpoints:** `POST /seller/products/{id}/image`
  * **Key Criteria:** รองรับไฟล์ JPEG, PNG, WEBP ขนาดไม่เกิน 5MB, จัดเก็บในระบบไฟล์ท้องถิ่นและให้บริการผ่าน `/seller-images/**`

---

### 📊 หมวด US-06: Seller Dashboard, Profit & Storefront
* **US-06-1: Seller Dashboard (Cost & Profit Metrics)**
  * **EN:** As a seller, I want to input purchase costs and track my store's estimated sales, revenue, and net profit calculated from purchase-time cost snapshots.
  * **TH:** ในฐานะผู้ขาย ฉันต้องการกรอกต้นทุนการ์ดแต่ละใบ และดูการคำนวณยอดขายรวมพร้อมกำไรสุทธิ `(Price - Cost) * Quantity` จากแดชบอร์ดส่วนตัว
  * **Endpoints:** `GET /seller/orders/profit-summary`

* **US-06-2: Public Storefront & Custom Store Settings**
  * **EN:** As a seller, I want to customize my store name, bio, and settings, and have a public storefront URL (`/stores/:sellerId`) displaying all my active listings.
  * **TH:** ในฐานะผู้ขาย ฉันต้องการตั้งค่าข้อมูลร้านค้าและมีหน้าเว็บร้านค้าของตัวเองให้ผู้ซื้อเข้ามาเลือกดูการ์ดทั้งหมดที่ร้านฉันวางขายได้โดยตรง
  * **Endpoints:** `GET /api/sellers/{sellerId}/store`, `PUT /api/seller/store-profile`

---

### 📋 หมวด US-07: Seller Order Management & Fulfillment
* **US-07-1: View Seller Orders & Status Filter**
  * **EN:** As a seller, I want to view orders containing items from my shop and filter them by status (`PENDING`, `FULFILLED`, `CANCELLED`).
  * **TH:** ในฐานะผู้ขาย ฉันต้องการดูรายการคำสั่งซื้อเฉพาะของร้านตนเอง และกรองตามสถานะได้
  * **Endpoints:** `GET /seller/orders`

* **US-07-2: Update Order Status (Pending → Fulfilled / Cancelled)**
  * **EN:** As a seller, I want to update order status to `FULFILLED` once external payment is received, or `CANCELLED` to release reserved stock.
  * **TH:** ในฐานะผู้ขาย ฉันต้องการปรับสถานะคำสั่งซื้อเป็น Fulfilled หรือ Cancelled หลังตรวจสอบการชำระเงินกับผู้ซื้อแล้ว
  * **Endpoints:** `PATCH /seller/orders/{orderId}/status`

* **US-07-3: Automated Card Ownership Transfer upon Order Fulfillment**
  * **EN:** As a buyer, when the seller marks my order as fulfilled/sent, I want the purchased cards to be automatically added to my personal collection album.
  * **TH:** ในฐานะผู้ซื้อ เมื่อผู้ขายกดยืนยันการจัดส่ง/ได้รับเงินแล้ว ฉันต้องการให้ระบบโอนกรรมสิทธิ์การ์ดเข้าคอลเลกชันส่วนตัวของฉันโดยอัตโนมัติ

---

### 👤 หมวด US-08: User Profile & Contact Channels
* **US-08-1: Edit Contact Information**
  * **EN:** As a user, I want to edit my contact channels (Phone, Line ID, Facebook) so trading partners can contact me to settle deals.
  * **TH:** ในฐานะผู้ใช้ ฉันต้องการแก้ไขช่องทางการติดต่อ เพื่อให้ผู้ซื้อ/ผู้ขายติดต่อสื่อสารกันได้
  * **Endpoints:** `PUT /users/me`

* **US-08-2: Edit Display Name**
  * **EN:** As a user, I want to update my public display name or full name.
  * **TH:** ในฐานะผู้ใช้ ฉันต้องการแก้ไขชื่อ-นามสกุล หรือชื่อแสดงตน

* **US-08-3: Edit Phone Number**
  * **EN:** As a user, I want to update my primary phone number.
  * **TH:** ในฐานะผู้ใช้ ฉันต้องการแก้ไขเบอร์โทรศัพท์

* **US-08-4: Edit Profile Avatar**
  * **EN:** As a user, I want to set or update my profile avatar URL so that my profile picture is displayed across the platform.
  * **TH:** ในฐานะผู้ใช้ ฉันต้องการตั้งค่าหรือเปลี่ยนรูปโปรไฟล์ (Avatar URL) เพื่อให้แสดงรูปภาพประจำตัวบนแพลตฟอร์ม
  * **Endpoints:** `PUT /users/me` (field: `avatarUrl`)

---

### 📜 หมวด US-09: Buyer Order History & Tracking
* **US-09-1: View Buyer Order History**
  * **EN:** As a customer, I want to view my order history and see reserved items along with seller contact information.
  * **TH:** ในฐานะลูกค้า ฉันต้องการดูประวัติคำสั่งซื้อทั้งหมดที่ตัวเองเคยสั่ง พร้อมข้อมูลติดต่อผู้ขาย
  * **Endpoints:** `GET /orders/me`, `GET /orders/{id}`

* **US-09-2: Filter Order History by Status**
  * **EN:** As a customer, I want to filter my order history by status (`PENDING`, `FULFILLED`, `CANCELLED`).
  * **TH:** ในฐานะลูกค้า ฉันต้องการกรองประวัติคำสั่งซื้อตามสถานะของออเดอร์ได้

---

### 🌟 หมวด US-10: Collection System, Leaderboard & Reservation Engine
* **US-10-1: View Personal Collection Album**
  * **EN:** As a user, I want to view my personal card collection album with rarity and condition details.
  * **TH:** ในฐานะผู้ใช้ ฉันต้องการเปิดดูอัลบั้มคอลเลกชันการ์ดสะสมส่วนตัวของฉัน
  * **Endpoints:** `GET /collection`

* **US-10-2: Add Card to Collection from Catalog**
  * **EN:** As a user, I want to add cards from the card catalog database into my collection.
  * **TH:** ในฐานะผู้ใช้ ฉันต้องการค้นหาและเพิ่มการ์ดจากแคตตาล็อกเข้าคอลเลกชัน
  * **Endpoints:** `POST /collection`

* **US-10-3: Remove Card from Collection**
  * **EN:** As a user, I want to remove cards I no longer own from my collection.
  * **TH:** ในฐานะผู้ใช้ ฉันต้องการลบการ์ดออกจากคอลเลกชัน
  * **Endpoints:** `DELETE /collection/{id}`

* **US-10-4: Self-serve Seller Verification Form**
  * **EN:** As a customer, I want to submit a seller profile form to apply for seller status.
  * **TH:** ในฐานะลูกค้า ฉันต้องการกรอกข้อมูลร้านค้าเพื่อยื่นขอสิทธิ์เปิดร้านขายการ์ด
  * **Endpoints:** `POST /api/sellers/verify`

* **US-10-5: Atomic Stock Reservation Semantics**
  * **EN:** As a system, I want to validate cart quantity against `onHand - reserved` stock and reserve stock atomically upon order placement to prevent overselling.
  * **TH:** ในฐานะระบบ ระบบต้องตรวจสอบสต๊อกคงเหลือจริง (`onHand - reserved`) และล็อกจองสต๊อกทันทีเมื่อมีการสร้างออเดอร์ เพื่อป้องกันปัญหาแย่งกันซื้อ (Overselling)

* **US-10-6: Public Collector Showcase & Top Collector Leaderboard**
  * **EN:** As a collector, I want to showcase my collection album publicly (`/collections/:userId`) and view the community leaderboard of top collectors ranking by rare card counts.
  * **TH:** ในฐานะนักสะสม ฉันต้องการเปิดหน้าคอลเลกชันของฉันให้ผู้อื่นเข้าชมได้ และสามารถดูตารางอันดับ Leaderboard ของนักสะสมที่มีการ์ดระดับ Rare มากที่สุดในระบบ
  * **Endpoints:** `GET /collections/leaderboard`, `GET /collections/{userId}`

* **US-10-7: Add Card to Collection from Product Listing**
  * **EN:** As a user, I want to add a card directly from a product listing page to my collection, without needing to find the card in the catalog separately.
  * **TH:** ในฐานะผู้ใช้ ฉันต้องการเพิ่มการ์ดจากหน้ารายการสินค้า (Product Listing) เข้าคอลเลกชันโดยตรง โดยไม่ต้องค้นหาการ์ดในแคตตาล็อกแยกต่างหาก
  * **Endpoints:** `POST /collection/from-listing/{listingId}`

---

### 🔔 หมวด US-11: In-App Notifications Center
* **US-11-1: In-App Notifications Inbox & Status Alerts**
  * **EN:** As a user (buyer or seller), I want to receive in-app inbox notifications when cards are reserved, when an order status changes, or when my seller application is processed, and be able to mark them as read or delete them.
  * **TH:** ในฐานะผู้ใช้ (ทั้งผู้ซื้อและผู้ขาย) ฉันต้องการได้รับการแจ้งเตือนในระบบเมื่อมีคนมาจองการ์ด, เมื่อสถานะออเดอร์มีความคืบหน้า หรือเมื่อการสมัครเป็นผู้ขายได้รับการอนุมัติ/ปฏิเสธ พร้อมทั้งสามารถกดอ่านแล้วหรือลบการแจ้งเตือนได้
  * **Endpoints:** `GET /notifications`, `PATCH /notifications/{id}/read`, `DELETE /notifications/{id}`

* **US-11-2: Notification Badge & Unread Count**
  * **EN:** As a user, I want to see a notification bell icon with an unread count badge in the navigation bar so that I can immediately know when I have new notifications without navigating to the inbox page.
  * **TH:** ในฐานะผู้ใช้ ฉันต้องการเห็นไอคอนกระดิ่งแจ้งเตือนพร้อมตัวเลขจำนวนข้อความที่ยังไม่อ่านบน Navbar เพื่อให้ทราบทันทีว่ามีการแจ้งเตือนใหม่โดยไม่ต้องเปิดหน้า Inbox
  * **UI Components:** `NotificationBell` (ใน Navbar), Badge Counter

---

### 🛡️ หมวด US-12: Platform Administration & Governance
* **US-12-1: Platform Admin Dashboard & Metrics**
  * **EN:** As an admin, I want to view a central platform dashboard displaying key operational metrics (total users, registered sellers, pending applications, and total trading volume) to monitor platform health.
  * **TH:** ในฐานะผู้ดูแลระบบ ฉันต้องการดูภาพรวมสถิติของระบบ เช่น จำนวนผู้ใช้ทั้งหมด, จำนวนผู้ขาย, คำขอสมัครที่รอตรวจ และยอดการซื้อขายรวม
  * **Endpoints:** `GET /api/admin/dashboard`

* **US-12-2: Seller Application Review Queue**
  * **EN:** As an admin, I want to view and filter the queue of pending seller verification applications.
  * **TH:** ในฐานะผู้ดูแลระบบ ฉันต้องการดูและกรองรายการคำขอเปิดร้านของผู้ขายที่รอการตรวจสอบ
  * **Endpoints:** `GET /api/admin/seller-applications`

* **US-12-3: Admin User & Role Management**
  * **EN:** As an admin, I want to search registered users, view their seller status, promote users to admin role, or manage administrative accounts.
  * **TH:** ในฐานะผู้ดูแลระบบ ฉันต้องการค้นหารายชื่อผู้ใช้, ดูสถานะผู้ขาย, แต่งตั้งสิทธิ์ Admin ให้กับผู้ใช้ หรือจัดการบัญชีแอดมิน
  * **Endpoints:** `GET /api/admin/users`, `POST /api/admin/users`, `DELETE /api/admin/users/{id}`

* **US-12-4: Administrative & Security Audit Logs**
  * **EN:** As an admin, I want to search and filter audit logs by action type, actor, target, and date range so that all critical operations can be tracked and audited.
  * **TH:** ในฐานะผู้ดูแลระบบ ฉันต้องการค้นหาและกรองดูบันทึก Audit Log ตามประเภทการกระทำ, ผู้กระทำ, หรือช่วงเวลา เพื่อความโปร่งใสและตรวจสอบความปลอดภัยของระบบได้
  * **Endpoints:** `GET /api/admin/audit-logs`

* **US-12-5: Platform-wide Order Logs Monitoring**
  * **EN:** As an admin, I want to inspect a centralized, read-only log of all orders across the platform with status filtering to monitor trade volume and troubleshoot issues.
  * **TH:** ในฐานะผู้ดูแลระบบ ฉันต้องการดูรายการคำสั่งซื้อทั้งหมดที่เกิดขึ้นในระบบ (ข้ามทุกร้านค้า) พร้อมตัวกรองสถานะเพื่อตรวจสอบปัญหาและติดตามธุรกรรม
  * **Endpoints:** `GET /api/admin/orders`

* **US-12-6: Review Seller Application Decision**
  * **EN:** As an admin, I want to review the details of a submitted seller application and make a decision to approve or reject it with a provided reason.
  * **TH:** ในฐานะผู้ดูแลระบบ ฉันต้องการพิจารณารายละเอียดคำขอเปิดร้านของผู้ขาย และทำการตัดสินใจอนุมัติหรือปฏิเสธพร้อมระบุเหตุผล
  * **Endpoints:** `PATCH /api/admin/seller-applications/{id}/approve`, `PATCH /api/admin/seller-applications/{id}/reject`

---

### ⚙️ หมวด US-13: System Reliability & Error Handling
* **US-13-1: System Health Check Endpoint**
  * **EN:** As a DevOps engineer or monitoring system, I want a health check endpoint that returns the system's operational status so that I can monitor uptime and detect outages automatically.
  * **TH:** ในฐานะวิศวกร DevOps หรือระบบ Monitoring ฉันต้องการ Endpoint ตรวจสอบสถานะระบบ เพื่อตรวจวัดเสถียรภาพและตรวจจับปัญหาได้โดยอัตโนมัติ
  * **Endpoints:** `GET /health` → `{"status": "UP"}`

* **US-13-2: Error Boundary & 404 Not Found Page**
  * **EN:** As a user, when I navigate to a non-existent page or encounter an unexpected application error, I want to see a friendly error page with navigation options so that I can recover without losing context.
  * **TH:** ในฐานะผู้ใช้ เมื่อฉันเข้าถึงหน้าที่ไม่มีอยู่หรือเกิดข้อผิดพลาดในแอป ฉันต้องการเห็นหน้าแจ้งข้อผิดพลาดที่เป็นมิตรพร้อมปุ่มนำทาง เพื่อให้สามารถกลับไปใช้งานต่อได้
  * **UI Components:** `ErrorBoundary`, `NotFoundPage` (route: `*`)

* **US-13-3: Idempotent Order Creation (Duplicate Prevention)**
  * **EN:** As a system, I want to support idempotent order creation via `Idempotency-Key` header so that network retries or double-clicks by users do not result in duplicate orders and double stock reservations.
  * **TH:** ในฐานะระบบ ระบบต้องรองรับการสร้างออเดอร์แบบ Idempotent ผ่าน `Idempotency-Key` Header เพื่อป้องกันไม่ให้การ retry ของเครือข่ายหรือการกดซ้ำทำให้เกิดออเดอร์ซ้ำและจองสต๊อกซ้ำ
  * **Key Criteria:** Order table มี `idempotency_key` column ที่เป็น UNIQUE constraint, ระบบตรวจสอบก่อนสร้าง Order ใหม่
  * **Endpoints:** `POST /orders` (header: `Idempotency-Key`)
