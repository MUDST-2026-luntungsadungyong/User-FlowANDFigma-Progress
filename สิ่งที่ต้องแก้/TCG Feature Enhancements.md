# 🌟 Master Requirement & TCG Feature Enhancements (ฉบับสมบูรณ์ พร้อมระบุหน้า)

เอกสารฉบับนี้รวบรวม **"ฟีเจอร์เฉพาะทาง (Niche Features)"** และ **"กรณีข้อยกเว้น/กันโกง (System Edge Cases)"** พร้อมระบุเป้าหมายหน้าจอในไฟล์ `TCG DevOp Project_ui` (อิงตามไฟล์ PDF) ที่ต้องนำไปแก้ไข

---

## 🎨 PART 1: Core TCG Features (ฟีเจอร์หลักหน้าบ้าน)

### 1. 🃏 ระบบข้อมูลเฉพาะของการ์ด (TCG Metadata)
* **ให้ไปแก้ในหน้า 49 ของไฟล์ TCG DevOp Project_ui (หน้า Edit Product):** 
  เพิ่ม Dropdown เลือก `Card Condition` (เช่น NM, LP, MP, HP, DMG) และ Option ให้เลือก `Card Grading` (ระบุบริษัท PSA/BGS พร้อม Score 1-10 และเลข Cert Number) ไว้ใต้ช่อง Product Name

### 2. 👤 ตัวตนใน Community (Username/Store Alias)
* **ให้ไปแก้ในหน้า 2 ของไฟล์ TCG DevOp Project_ui (หน้า Create Account):** 
  เพิ่มฟิลด์ `Username` เข้าไปในฟอร์มสมัครสมาชิก
* **และแก้ในหน้า 12 (หน้า Edit Personal Information):** 
  เพิ่มฟิลด์ `Username` หรือ `Store Name` เพื่อให้ผู้ใช้สามารถแก้ไขชื่อแสดงตนบน Marketplace ได้

---

## 🛒 PART 2: Checkout & 2-Leg Logistics (ระบบตะกร้าและขนส่ง)

### 3. ⏱️ ระบบล็อกสต็อกชั่วคราว (Inventory Concurrency)
* **ให้ไปแก้ในหน้า 30 ของไฟล์ TCG DevOp Project_ui (หน้า Order Review):** 
  เพิ่มแถบ **Countdown Timer (เช่น 10:00 นาที)** ไว้ด้านบนสุดของหน้าต่าง เพื่อแจ้งผู้ใช้ว่ากำลังล็อก Stock หากเวลาหมดจะนำสินค้ากลับสู่ตลาด

### 4. 💳 การแจกแจงค่าธรรมเนียมตัวกลาง (Escrow & Security Fee)
* **ให้ไปแก้ในหน้า 30 ของไฟล์ TCG DevOp Project_ui (หน้า Order Review):** 
  ในกล่อง Order Summary ให้เพิ่มบรรทัด **`Security / Authentication Fee`** ลงไปแยกต่างหาก และระบุค่าส่งเป็น `Leg 2 Shipping (Hub -> Buyer)` เพื่อให้ผู้ซื้อเห็นชัดเจนว่ามีการบวกค่าธรรมเนียมคนกลาง

### 5. 🛡️ ระบบขนส่งแบบ 2-Leg & QC Hub (ตัวกลางตรวจสอบ)
* **ให้ไปแก้ในหน้า 43 และ 60 ของไฟล์ TCG DevOp Project_ui (หน้า My Orders / Order Management):** 
  เปลี่ยนสถานะจากระบบส่งตรงธรรมดา ให้มีจังหวะของ 2-Leg โดยเพิ่มสถานะ `Shipping to Hub`, `In QC Inspection`, `QC Passed`, `QC Failed` เข้าไปใน Progress Bar หรือ Filter Tab

---

## 🚨 PART 3: Edge Cases & Trust System (กรณีเฉพาะและระบบกันโกง)

### 6. ⏳ ระบบนับเวลาตัดจบ (SLA Timers)
* **ให้ไปแก้ในหน้า 60 ของไฟล์ TCG DevOp Project_ui (หน้า Order Management : Detail):** 
  เพิ่มป้าย Badge หรือข้อความนับเวลาถอยหลัง (SLA Countdown) เช่น "กรุณาส่งของภายใน 48 ชม." สำหรับ Seller และ "ยืนยันรับสินค้าใน 72 ชม." สำหรับส่วนของ Buyer

### 7. ✂️ การแยกคืนเงินรายชิ้น (Partial QC Fail & Split Order)
* **ให้ไปแก้ในหน้า 13 ของไฟล์ TCG DevOp Project_ui (หน้า TCG Dashboard - QC Queue):** 
  ในกรณีมีสินค้าหลายชิ้นใน 1 ออเดอร์ ให้เพิ่ม UI Checkbox หน้าสินค้าแต่ละชิ้น เพื่อให้ Admin กดว่าชิ้นไหน `Pass` ชิ้นไหน `Fail` และมีปุ่ม `Partial Refund` แยกรายชิ้น

### 8. 📹 ระบบหลักฐานและประกันพัสดุ (QC Evidence & Insurance Opt-in)
* **ให้ไปแก้ในหน้า 30 ของไฟล์ TCG DevOp Project_ui (หน้า Order Review):** 
  เพิ่ม Checkbox `ซื้อประกันพัสดุ (Shipping Insurance)` ในกล่องตัวเลือกการจัดส่ง
* **และแก้ในหน้า 60 (หน้า Order Management : Detail):** 
  เพิ่มกล่องแกลเลอรีภาพ (Evidence Section) เพื่อให้ผู้ใช้งานกดเข้าไปดู **วิดีโอ Unboxing** หรือ **รูปถ่าย 4K Macro** ที่ถูกถ่ายไว้เป็นหลักฐานโดย QC Hub

### 9. 🔒 การล็อกชื่อบัญชีถอนเงิน (KYC Bank Lock)
* **ให้ไปแก้ในหน้า 61 ของไฟล์ TCG DevOp Project_ui (หน้า Payout History / Payout Settings):** 
  เพิ่มเครื่องหมายกุญแจล็อก หรือแสดงสถานะ `Verified by KYC` ตรงชื่อบัญชีธนาคารปลายทาง โดยมีข้อความระบุว่า "ไม่อนุญาตให้แก้ไขชื่อบัญชีธนาคาร ต้องตรงกับบัตรประชาชนเท่านั้น"
