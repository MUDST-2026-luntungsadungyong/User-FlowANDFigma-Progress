# 🌟 Master Requirement & TCG Feature Enhancements (ฉบับสมบูรณ์)

เอกสารฉบับนี้รวบรวม **"ฟีเจอร์เฉพาะทาง (Niche Features)"** และ **"กรณีข้อยกเว้น/กันโกง (System Edge Cases)"** สำหรับยกระดับระบบ E-Commerce ทั่วไป ให้กลายเป็น **TCG Marketplace (Trading Card Game) ที่ปลอดภัยและน่าเชื่อถือ 100%** 

---

## 🎨 PART 1: Core TCG Features (ฟีเจอร์หลักหน้าบ้าน)

### 1. 🃏 ระบบข้อมูลเฉพาะของการ์ด (TCG Metadata)
ระบบขายสินค้าทั่วไปมีแค่ ชื่อ, ราคา, สต็อก แต่สำหรับวงการการ์ด "สภาพการ์ด" คือสิ่งกำหนดราคา
* **หน้า Add/Edit Product:** เพิ่ม Dropdown เลือก `Card Condition` (เช่น NM, LP, MP, HP, DMG) และ `Card Grading` (ระบุบริษัท PSA/BGS พร้อม Score และเลข Cert Number)

### 2. 👤 ตัวตนใน Community (Username/Store Alias)
ตลาดการ์ดขับเคลื่อนด้วยความน่าเชื่อถือของตัวบุคคล
* **หน้า Auth & Profile:** เพิ่มฟิลด์ `Username` ตอน Sign Up และ Edit Profile เพื่อใช้เป็นชื่อแสดงตนแทนชื่อ-นามสกุลจริง

---

## 🛒 PART 2: Checkout & 2-Leg Logistics (ระบบตะกร้าและขนส่ง)

### 3. ⏱️ ระบบล็อกสต็อกชั่วคราว (Inventory Concurrency)
การ์ดแรร์มักมีของ 1 ชิ้น ป้องกันคนแย่งซื้อและ Race Condition
* **หน้า Checkout:** เพิ่มแถบ **Countdown Timer (10:00 นาที)** หากเวลาหมด ระบบจะ Unlock สินค้าคืนกลับสู่ตลาดให้คิวถัดไป

### 4. 💳 การแจกแจงค่าธรรมเนียมตัวกลาง (Escrow & Security Fee)
* **หน้า Order Review / Checkout:** เพิ่มบรรทัด **`Security / Authentication Fee`** และแยกค่าส่ง **`Leg 2 Shipping (Hub -> Buyer)`** ให้ผู้ซื้อเห็นอย่างโปร่งใส

### 5. 🛡️ ระบบขนส่งแบบ 2-Leg & QC Hub (ตัวกลางตรวจสอบ)
* **หน้า Order Status:** ปรับ Flow ให้รองรับ 2 จังหวะ (`Seller -> QC Hub` และ `QC Hub -> Buyer`)
* **เพิ่มสถานะออเดอร์:** `Shipping to Hub`, `In QC Inspection`, `QC Passed`, `QC Failed`

---

## 🚨 PART 3: Edge Cases & Trust System (กรณีเฉพาะและระบบกันโกง)
*(ฟีเจอร์เชิงลึกที่ต้องนำไปวางโครงสร้างทั้งฝั่ง Backend และ UI/UX Figma)*

### 6. ⏳ ระบบนับเวลาตัดจบ (SLA Timers)
ระบบ Escrow ไม่สามารถล็อกเงินค้างไว้ตลอดกาลได้ ต้องมีกรอบเวลา
* **ฝั่ง Seller (48h Drop-off):** ต้องมีหน้าปัด/ข้อความเตือนใน Order ว่า "กรุณาส่งของภายใน 48 ชม. มิฉะนั้นระบบจะยกเลิกและคืนเงินผู้ซื้ออัตโนมัติ"
* **ฝั่ง Buyer (72h Acceptance):** เมื่อของส่งถึงมือผู้ซื้อ ต้องมีข้อความเตือนว่า "กรุณากดยืนยันรับสินค้าภายใน 72 ชม. หากไม่ดำเนินการ ระบบจะโอนเงินให้ร้านค้าอัตโนมัติ"

### 7. ✂️ การแยกคืนเงินรายชิ้น (Partial QC Fail & Split Order)
กรณีผู้ซื้อสั่งการ์ดหลายใบในออเดอร์เดียว แต่ Hub ตรวจพบว่าบางใบ "ไม่ตรงปก/ปลอม"
* **หน้าจอ QC Report (Admin/Buyer):** ระบบต้องรองรับการคืนเงินเฉพาะใบที่ตก QC (Partial Refund) และอัพเดตยอดเงินใน Order Summary ใหม่ โดยยังคงดำเนินการจัดส่งใบที่ผ่าน QC ต่อไปให้ผู้ซื้อ

### 8. 📹 ระบบหลักฐานและประกันพัสดุ (QC Evidence & Insurance Opt-in)
ป้องกันข้อพิพาท "ใครทำแผ่นการ์ดพับ/ยับ?"
* **หน้า Checkout / Fulfillment:** เพิ่ม Checkbox `ซื้อประกันพัสดุ (Shipping Insurance)` ให้ผู้ซื้อหรือผู้ขายเลือกจ่ายเพิ่ม
* **หน้า Order Details (Evidence Gallery):** เพิ่ม Section ให้ผู้ซื้อและผู้ขายสามารถกดดู **วิดีโอ Unboxing** หรือ **รูปถ่าย 4K Macro** ที่ QC Hub บันทึกไว้เป็นหลักฐานได้

### 9. 🔒 การล็อกชื่อบัญชีถอนเงิน (KYC Bank Lock)
ป้องกันมิจฉาชีพขโมยบัญชีผู้ใช้แล้วถอนเงินเข้าบัญชีม้า
* **หน้า Seller Payouts / Wallet:** ชื่อบัญชีธนาคารปลายทางที่จะผูกเพื่อถอนเงิน **ต้องถูกล็อกให้ตรงกับชื่อบนบัตรประชาชน (KYC)** ที่ใช้ยืนยันตัวตนเท่านั้น ไม่อนุญาตให้พิมพ์แก้ไขชื่อบัญชีอิสระ

---

## 📋 PART 4: Closed GitHub Issues ที่ยังไม่ได้รับการแก้ไขจริงในโปรเจค (Pending Implementation & Missing Artifacts)

> ⚠️ **คำเตือนสถานะโปรเจค:** รายการ Issue ด้านล่างนี้มีสถานะเป็น **`Closed`** บน GitHub Repository (`MUDST-2026-luntungsadungyong/User-Flow`) แล้ว แต่จากการตรวจสอบไฟล์งานในเครื่องและ Architecture ปัจจุบัน พบว่า **ยังไม่มีการจัดทำ Diagram, ขาด Swimlane User Flow หรือยังพัฒนาตกหล่นอยู่จริง** ต้องได้รับการแก้ไขและจัดทำ Artifacts ให้ครบถ้วน:

---

### 1. 🔴 GitHub Issue #6: `[FLOW-FIX: US-02/03] ระบบค้นหาและตะกร้าสำหรับ Multi-Seller และ Cart Drawer`
* **สถานะปัจจุบัน:** `Closed บน GitHub` ❌ **แต่ในโปรเจคยังไม่มี Diagram (`US-02_Swimlane_User_Flow.svg` / `US-03_Swimlane_User_Flow.svg`)**
* **ปัญหาเดิม:** Flow เดิมมองว่าการ์ดแต่ละใบมีผู้ขายคนเดียวและสต็อกรวมก้อนเดียว ซึ่งขัดแย้งกับความเป็นจริงของระบบ Marketplace
* **รายละเอียดสิ่งที่ต้องทำอย่างละเอียด:**
  1. **Multi-Seller Listing on Card Detail Page (`Shop & Browse/frame_3.svg`):**
     * การ์ด 1 ใบ (เช่น *OP-05 Manga Luffy*) สามารถมีผู้ขายได้หลายร้านค้าพร้อมกัน
     * หน้ารายละเอียดการ์ดต้องแสดงตารางเปรียบเทียบผู้ขาย (Seller List Table):
       * ข้อมูลร้านค้า, ระดับสภาพการ์ด (Mint / NM / LP), รูปถ่ายสภาพจริง
       * ราคาขาย และจำนวนสต็อกคงเหลือของแต่ละร้าน
       * Seller Trust Rating และระยะเวลาเฉลี่ยในการส่งเข้า Hub
       * ปุ่ม **"Add to Cart"** และ **"Buy Now"** แยกราย Listing
  2. **Cart Drawer Interaction (`Shop & Browse/frame_6.svg`):**
     * เมื่อผู้ซื้อกด "Add to Cart" ระบบต้องแสดงแถบสไลด์ **Cart Drawer** ออกมาจากขอบจอด้านขวาทันทีโดยไม่ต้องโหลดหรือ Refresh หน้าใหม่
     * ระบบตะกร้าต้องจัดกลุ่มสินค้าแยกตามร้านค้า (**Group by Seller**) เพื่อเตรียมคำนวณค่าส่ง Leg 1 เข้า Hub แยกตามร้าน
     * รองรับการปรับจำนวน (+/-), ลบรายการการ์ด และคำนวณ Subtotal แบบ Real-time
  3. **Technical & Data Model Impact:**
     * Data Model ใน Cart ต้องผูกกับ `listing_id` (เฉพาะเจาะจงร้านและสภาพ) แทนที่จะผูกกับ `card_id` รวม

---

### 2. 🔴 GitHub Issue #7: `[FLOW-NEW: Seller/Admin] เพิ่ม User Flow ฟีเจอร์ที่ตกหล่น (Wallet, Bulk CSV, Dispute)`
* **สถานะปัจจุบัน:** `Closed บน GitHub` ❌ **แต่ในโปรเจคยังไม่มี Swimlane Diagram ทั้ง 3 ระบบนี้เลย**
* **รายละเอียดสิ่งที่ต้องทำอย่างละเอียด:**

#### 🔹 2.1 US-Seller-Wallet: ระบบกระเป๋าเงินและการถอนเงินของผู้ขาย (`seller/frame_9, 10, 11.svg`)
* **โครงสร้างยอดเงิน (Wallet Balance Engine):**
  * `Available Balance`: ยอดเงินที่ถอนได้ (ออเดอร์ผ่าน QC และส่งถึงผู้ซื้อเกิน 72 ชม. แล้ว)
  * `Escrow Held Balance`: ยอดเงินที่ยังถูกพักไว้ในระบบ Escrow (รอส่งเข้า Hub / รอตรวจ QC / รอผู้ซื้อตรวจรับ)
* **กระบวนการสั่งถอนเงิน (Withdrawal Flow):**
  * ร้านค้ากดสั่งถอนเงิน ➔ ระบุจำนวนเงิน ➔ ระบบคำนวณหักค่าธรรมเนียมโอน (Transfer Fee)
  * สร้างรายการธุรกรรมสถานะ `PENDING_PAYOUT` ➔ แอดมินหรือระบบอัตโนมัติโอนเงินเข้าบัญชีธนาคาร
* **ระบบความปลอดภัยและการป้องกันการฟอกเงิน (KYC Bank Lock):**
  * ชื่อบัญชีธนาคารที่ผูกเพื่อรับเงิน (`seller/frame_11.svg`) **ต้องถูกล็อกเป็นแบบ Read-only** ให้ตรงกับชื่อ-นามสกุลบนบัตรประชาชนที่ผ่านการยืนยันตัวตน KYC เท่านั้น ไม่อนุญาตให้พิมพ์แก้ไขเอง

#### 🔹 2.2 US-Seller-Bulk: ระบบนำเข้าสต็อกการ์ดจำนวนมากผ่าน CSV (`seller/frame_8.svg`)
* **กระบวนการทำงาน (Bulk CSV Import Flow):**
  * ร้านค้าดาวน์โหลดไฟล์ Template CSV (มีคอลัมน์ `master_card_id`, `condition`, `price`, `quantity`, `photo_urls`)
  * ร้านค้าอัปโหลดไฟล์ CSV เข้าสู่ระบบ
  * Backend Background Worker ทำการ Validate ข้อมูลทุกแถว:
    * ตรวจสอบว่า `master_card_id` มีอยู่จริงในระบบหรือไม่
    * ตรวจสอบความถูกต้องของค่า Condition Enum (Mint/NM/LP/MP/HP/DMG)
  * Batch Insert เข้าตาราง `seller_listings`
  * แสดงหน้าต่างสรุปผลลัพธ์: จำนวนแถวที่สำเร็จ (Success) และรายการแถวที่เกิดข้อผิดพลาด (Failed Rows พร้อมเหตุผล)

#### 🔹 2.3 US-Admin-Dispute: ศูนย์ระงับข้อพิพาทและการเคลมสินค้า (`platform-admin/frame_7.svg`)
* **กระบวนการตัดสินข้อพิพาท (Dispute Resolution Flow):**
  * ผู้ซื้อเปิดคำร้องข้อพิพาท (Dispute Case) กรณีอ้างว่าการ์ดชำรุด, สลับของ, หรือสูญหาย
  * เจ้าหน้าที่ Admin เปิดเคสในระบบ ➔ เข้าดู **QC Camera Proof Gallery** (คลิปวิดีโอ Unboxing และภาพถ่าย 4K Macro ตอนที่การ์ดมาถึง Hub)
  * **จุดตัดสินใจของ Admin (Decision Point):**
    * **Approve Claim (ผู้ซื้อถูก / สินค้าเสียหายจริงก่อนถึง Hub):** ระงับการจ่ายเงินให้ร้านค้า ➔ คืนเงิน Escrow ให้ผู้ซื้อ 100% ➔ ทำเรื่องเคลมประกันพัสดุ (Leg 1/Leg 2)
    * **Reject Claim (ผู้ซื้อแจ้งเท็จ / การ์ดสภาพตรงกับที่ Hub ตรวจรับและส่งออก):** ปฏิเสธคำร้อง ➔ ปลดล็อกเงิน Escrow โอนให้ผู้ขายตามปกติ ➔ บันทึก Audit Log คดี

---

### 3. 🟡 GitHub Issue #3 (ตกหล่นบางส่วน): `ระบบ Partial QC Fail & Split Orders ใน US-07`
* **สถานะปัจจุบัน:** `Closed บน GitHub` ⚠️ **มีไฟล์ `US-07_Swimlane_User_Flow.svg` แล้ว แต่ยังขาด Logic การตรวจแยกรายใบ**
* **รายละเอียดสิ่งที่ต้องปรับปรุง:**
  * ปรับ Swimlane จากเดิมที่ตัดสินใจ Pass/Fail ทั้งออเดอร์ ให้รองรับ **Multi-Item QC Inspection (`platform-admin/frame_4.svg`)**:
    * มี Checklist / Toggle Pass-Fail **แยกอิสระทีละใบ**
    * **ใบที่ผ่าน QC:** รวมส่งต่อ Leg 2 ไปยังที่อยู่ผู้ซื้อตามเดิม
    * **ใบที่ไม่ผ่าน QC:** ระบบทำการตัดยอดและทำ **Partial Refund** คืนเงินเฉพาะมูลค่าของการ์ดใบนั้นเข้าบัญชี/บัตรของผู้ซื้อโดยอัตโนมัติ พร้อมส่งการ์ดใบที่ตก QC คืนกลับให้ผู้ขาย

---
*เอกสารนี้ครอบคลุมความต้องการของระบบ TCG marketplace ตั้งแต่หน้าบ้าน (UI) ไปจนถึงหลังบ้าน (Business Logic, Edge cases และการติดตาม GitHub Issues)*
