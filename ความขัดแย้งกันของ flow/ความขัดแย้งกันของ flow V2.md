# 🚨 รายงานความขัดแย้งระหว่าง Flow กับ Figma (V2 - Verified Truth)

เอกสารฉบับนี้สรุป **"ความขัดแย้งและช่องโหว่"** ระหว่าง Requirement (Flow การทำงานของระบบ TCG) และ UI Design (Figma PDF) โดยอิงข้อมูลจากตัวอักษรและหน้าจอจริงในไฟล์ `TCG DevOp Project.pdf` 100% (ปราศจากการคาดเดา)

---

## 1. 👤 ระบบ Auth & Profile (ขาด Username)
*   **Figma (หน้า 2 และ 12):** หน้า Create Account มีเพียงช่อง `Email`, `Password`, `Confirm Password` และหน้า My Profile มีเพียง `Full Name`, `Email`, `Phone`
*   **Flow Requirement:** แพลตฟอร์มควรมี `Username` หรือ Store Name เพื่อใช้เป็นชื่ออ้างอิงในการซื้อขาย หรือแสดงตนใน Community
*   **🔥 ความขัดแย้ง:** Figma ไม่มีฟิลด์ Username ตั้งแต่ตอนสมัครและในหน้าแก้ไขโปรไฟล์
*   **🛠️ ทางแก้:** เพิ่มฟิลด์ `Username` ในหน้า Create Account และเพิ่มในหน้า Edit Profile

## 2. 🛒 ระบบ Checkout (ขาดการแจกแจงค่าธรรมเนียมและ Stock Timer)
*   **Figma (หน้า 30 - Order Review):** หน้าสรุปการสั่งซื้อแสดงข้อมูลพื้นฐาน ได้แก่ Shipping Address, Payment Method, Items, และ Order Summary (Subtotal, Shipping, Tax, Total) เท่านั้น
*   **Flow Requirement:** 
    1. แพลตฟอร์มเป็นระบบ 2-Leg Shipping ผู้ซื้อต้องจ่ายค่าส่ง "Leg 2 (Hub -> Buyer)" และต้องจ่าย "Security Fee (ค่าบริการตัวกลาง/QC)" 
    2. มีกฎ Business Logic ว่า "เมื่อเข้าหน้าชำระเงิน ให้ล็อก Stock 10 นาที (ถ้าไม่จ่ายให้คิวถัดไป)"
*   **🔥 ความขัดแย้ง:** 
    1. ใน Order Summary ของ Figma ไม่มีการแจกแจงบรรทัด **Security Fee / QC Fee** ให้ผู้ซื้อเห็นอย่างโปร่งใส
    2. หน้าจอ Checkout ไม่มี **ตัวเลขนับถอยหลัง (Countdown Timer 10:00)** เพื่อแสดงให้รู้ว่า Stock ถูกล็อกชั่วคราว
*   **🛠️ ทางแก้:** เพิ่มบรรทัด Security Fee ใน Order Summary และเพิ่มแถบ Countdown Timer ด้านบนของหน้า Checkout

## 3. 📦 สถานะออเดอร์ฝั่ง Seller (ขาดสถานะ QC Hub)
*   **Figma (หน้า 43 - My Orders):** แถบสถานะออเดอร์ของ Seller มีแค่ `All`, `Awaiting Ship`, `Shipped`, `Fulfilled`, `Cancelled` (เหมือนเว็บ E-commerce ส่งตรงปกติ)
*   **Flow Requirement:** แพลตฟอร์มนี้เป็นแบบ **QC Hub (ส่งเข้าศูนย์ตรวจก่อน)** ไม่ได้ส่งตรงถึงผู้ซื้อ 
*   **🔥 ความขัดแย้ง:** สถานะของ Figma ทำให้ Seller ไม่รู้ว่าของไปถึงไหนแล้วในกระบวนการ QC
*   **🛠️ ทางแก้:** ควรปรับ Tab สถานะให้ตรงกับบริบท 2-Leg เช่น `Awaiting Drop-off`, `Shipping to Hub`, `In QC Inspection`, `Fulfilled` (หรือ QC Passed/Failed)

## 4. 🃏 ระบบเพิ่มสินค้า Seller Inventory (ขาด Condition & Grading ของ TCG)
*   **Figma (หน้า 49 - Edit Product):** ฟิลด์ข้อมูลสินค้ามีเพียง `Product Name`, `Game`, `Sell Price`, `Cost`, `Stock`, และ `Image`
*   **Flow Requirement:** สินค้าประเภทการ์ด (TCG) ราคาจะขึ้นอยู่กับ **สภาพการ์ด (Condition)** เช่น NM, LP, MP หรือ **เกรดดิ้ง (Grading)** เช่น PSA 10, BGS 9.5
*   **🔥 ความขัดแย้ง:** Figma ออกแบบฟอร์มเพิ่มสินค้าเหมือนสินค้าทั่วไป ขาด Metadata ที่สำคัญที่สุดสำหรับวงการการ์ด
*   **🛠️ ทางแก้:** เพิ่ม Dropdown สำหรับเลือก `Condition` และฟิลด์ระบุ `Grading Company / Score` ในหน้า Add/Edit Product

## 5. 📹 ระบบหลักฐาน QC & Insurance (ขาด UI อัพโหลดวิดีโอ)
*   **Figma:** ไม่มี UI สำหรับให้ผู้ซื้อหรือผู้ขายดูวิดีโอ/รูปภาพหลักฐานการแพ็ค ทั้งในฝั่ง Order Detail ของ Buyer และ Seller
*   **Flow Requirement:** ในระบบมีการระบุเรื่อง **Shipping Insurance** และ **QC Proof** (ระบบต้องการ Unboxing video/photos เพื่อยืนยันว่า Hub/Courier ไม่ได้ทำของพัง)
*   **🔥 ความขัดแย้ง:** หากเกิดข้อพิพาท (Dispute) แพลตฟอร์มต้องการหลักฐานวิดีโอ แต่ Figma ไม่มีปุ่มให้อัพโหลดวิดีโอตอนแพ็คของส่ง หรือปุ่มดูภาพถ่ายจาก Hub ในหน้า Order Detail
*   **🛠️ ทางแก้:** เพิ่ม Section "QC & Evidence" ในหน้า Order Detail ให้ทั้งผู้ซื้อและผู้ขาย

---
*จัดทำขึ้นใหม่จากข้อมูลจริง 100% ใน TCG DevOp Project.pdf*
