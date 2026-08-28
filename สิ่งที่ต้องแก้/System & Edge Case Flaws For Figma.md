# 🎨 รายงานสิ่งที่ต้องปรับแก้ใน Figma Design (System & Edge Case Flaws for Figma)
> **เอกสารสำหรับ:** UI/UX Designers, Product Owners และ Frontend Developers  
> **ที่ตั้งไฟล์:** `Flow_devops/ExportBlock/Git/สิ่งที่ต้องแก้/System & Edge Case Flaws For Figma.md`  
> **อ้างอิงเอกสารหลัก:** `System & Edge Case FlawsMD.md` และ `FLOW_FIGMA_CONFLICT_REPORT.md`

---

## 📑 สารบัญ (Table of Contents)
1. [ภาพรวมการเชื่อมโยงระหว่าง Figma กับ User Flow](#1-ภาพรวมการเชื่อมโยงระหว่าง-figma-กับ-user-flow)
2. [ตาราง Matrix สรุปการเชื่อมโยง (Figma ➔ Flow ➔ Flaws Issue Mapping)](#2-ตาราง-matrix-สรุปการเชื่อมโยง)
3. [รายละเอียดสิ่งที่ต้องแก้ใน Figma รายข้อ พร้อมการเชื่อมโยงกับ Flow](#3-รายละเอียดสิ่งที่ต้องแก้ใน-figma-รายข้อ)
   - [ข้อที่ 1: แถบนับเวลาถอยหลัง SLA Timers (เชื่อมโยง FlawsMD ข้อ 2)](#ข้อที่-1-แถบนับเวลาถอยหลัง-sla-timers)
   - [ข้อที่ 2: ระบบตรวจสภาพการ์ดแยกรายใบและแสดงผล Partial Refund (เชื่อมโยง FlawsMD ข้อ 3)](#ข้อที่-2-ระบบตรวจสภาพการ์ดแยกรายใบและแสดงผล-partial-refund)
   - [ข้อที่ 3: แถบนับถอยหลังล็อกสต็อก 10 นาทีในหน้าชำระเงิน (เชื่อมโยง FlawsMD ข้อ 4)](#ข้อที่-3-แถบนับถอยหลังล็อกสต็อก-10-นาทีในหน้าชำระเงิน)
   - [ข้อที่ 4: หน้าต่างรายงานตำหนิให้ผู้ซื้อตัดสินใจ & การแยกค่าส่ง (เชื่อมโยง FlawsMD ข้อ 5 & 5.2)](#ข้อที่-4-หน้าต่างรายงานตำหนิให้ผู้ซื้อตัดสินใจ--การแยกค่าส่ง)
   - [ข้อที่ 5: Checkbox ซื้อประกันพัสดุ & แกลเลอรีดูคลิปแกะกล่อง QC Hub (เชื่อมโยง FlawsMD ข้อ 6 & 6.2)](#ข้อที่-5-checkbox-ซื้อประกันพัสดุ--แกลเลอรีดูคลิปแกะกล่อง-qc-hub)
   - [ข้อที่ 6: การล็อกชื่อบัญชีถอนเงินให้ตรงกับ KYC (เชื่อมโยง FlawsMD ข้อ 7)](#ข้อที่-6-การล็อกชื่อบัญชีถอนเงินให้ตรงกับ-kyc)

---

## 1. ภาพรวมการเชื่อมโยงระหว่าง Figma กับ User Flow

ในการพัฒนาแพลตฟอร์ม **TCG Escrow Marketplace** หน้าจอ UI ใน Figma จะต้องทำหน้าที่เป็น **"กระจกสะท้อน (Visual Representation)"** ของ Business Logic และ User Flow เสมอ 

เมื่อระบบมีกฎทางธุรกิจใหม่ (เช่น การตรวจสภาพการ์ด 2-Leg, สัญญาคนกลาง Escrow, และการจัดการสินค้าชำรุด) หน้าจอ UI จะต้องมี Component, Timer, Badge, และ Modal เพื่อรองรับ State Machine เหล่านั้นอย่างครบถ้วน

---

## 2. ตาราง Matrix สรุปการเชื่อมโยง

| ลำดับ | สิ่งที่ต้องเพิ่ม/แก้ใน Figma | หน้าจอ/Frame ใน Figma | เชื่อมโยงกับ User Flow ข้อไหน | อ้างอิงปัญหาใน `FlawsMD` |
| :---: | :--- | :--- | :--- | :--- |
| **1** | **SLA Countdown Badges (48h & 72h)** | `seller/frame_5, 6`<br>`Checkout Flow/frame_7` | • `US-07` (Seller Fulfillment)<br>• `US-09` (Buyer Tracking) | **ข้อ 2:** SLA Timers & Escrow Transitions |
| **2** | **Item-Level QC Checkboxes & Partial Refund Display** | `platform-admin/frame_4`<br>`Checkout Flow/frame_7` | • `US-07` (QC Hub Processing)<br>• `US-09` (Order History) | **ข้อ 3:** Partial QC Fail & Split Orders |
| **3** | **10-Min Stock Hold Timer Bar** | `Checkout Flow/frame_4, 5` | • `US-04` (Place Order & Checkout) | **ข้อ 4:** Stock Hold & Concurrency |
| **4** | **[NEW] Defect Mismatch Decision Modal & Shipping Split** | `Buyer Order Detail`<br>`Checkout Flow/frame_1, 4` | • `US-04` (Checkout Summary)<br>• `US-07` (QC Mismatch Decision) | **ข้อ 5:** Logistics & Defect Decision (4.1) |
| **5** | **Opt-in Insurance Checkboxes & [NEW] QC Camera Gallery** | `seller/frame_6`<br>`Checkout Flow/frame_4`<br>`Buyer & Seller Order View` | • `US-04` (Checkout Insurance)<br>• `US-07` (Leg 1 Insurance & QC Proof) | **ข้อ 6:** Insurance & QC Proof (5.1) |
| **6** | **KYC Locked Bank Account Name** | `seller/frame_11` | • `US-Seller-Wallet` (Payout Settings) | **ข้อ 7:** KYC & Anti-Fraud Payout |

---

## 3. รายละเอียดสิ่งที่ต้องแก้ใน Figma รายข้อ

---

### ข้อที่ 1: แถบนับเวลาถอยหลัง SLA Timers
* **อ้างอิงปัญหาใน `System & Edge Case FlawsMD`:** **ข้อ 2 (SLA Timers & Escrow Transitions)**
* **เชื่อมโยงกับฝั่ง User Flow อย่างไร:**
  - **เชื่อมกับ Flow `US-07 (Seller Fulfillment)`:** ใน Flow มีจุดเช็คเงื่อนไขว่า *“ร้านค้าส่งของเข้า Hub ภายใน 48 ชม. หรือไม่?”* ถ้าเกินเวลา ระบบจะ Auto-Cancel และคืนเงินให้ผู้ซื้อ 100%
  - **เชื่อมกับ Flow `US-09 (Order Tracking)`:** ใน Flow มีจุดเช็คเงื่อนไขว่า *“ผู้ซื้อตรวจรับของภายใน 72 ชม. หรือไม่?”* ถ้าเกินเวลา ระบบจะ Auto-Release โอนเงิน Escrow ให้ร้านค้าอัตโนมัติ
* **สิ่งที่ต้องเพิ่มใน Figma:**
  1. **ใน `seller/frame_5.svg` และ `frame_6.svg` (ฝั่งร้านค้า):**  
     - เพิ่มแถบสถานะสีส้มเตือนใจ: `⏳ กรุณาจัดส่งเข้า Hub ภายใน 47:59:00 ชม. (มิฉะนั้นระบบจะยกเลิกออเดอร์)`
  2. **ใน `Checkout Flow/frame_7.svg` / Buyer Order Detail (ฝั่งผู้ซื้อ):**  
     - เมื่อสถานะขึ้น `DELIVERED` เพิ่มแถบเตือนสีฟ้า: `📦 ได้รับสินค้าแล้ว กรุณาตรวจรับภายใน 71:59:00 ชม. (ระบบจะปล่อยเงินให้อัตโนมัติ)`

---

### ข้อที่ 2: ระบบตรวจสภาพการ์ดแยกรายใบและแสดงผล Partial Refund
* **อ้างอิงปัญหาใน `System & Edge Case FlawsMD`:** **ข้อ 3 (Partial QC Fail in Multi-Item Orders)**
* **เชื่อมโยงกับฝั่ง User Flow อย่างไร:**
  - **เชื่อมกับ Flow `US-07 (QC Hub Processing)`:** ใน Flow เจ้าหน้าที่ Hub ต้องมีเส้นทางแยกระหว่าง *“การ์ดใบที่ผ่าน QC”* (ส่งต่อ Leg 2) กับ *“การ์ดใบที่ไม่ผ่าน QC”* (ทำเรื่องคืนเงินเฉพาะใบนั้น 500฿ และส่งการ์ดคืนร้านค้า)
  - **เชื่อมกับ Flow `US-09 (Order History)`:** แสดงรายการออเดอร์ที่มี 2 สถานะย่อยในคำสั่งซื้อเดียวกัน
* **สิ่งที่ต้องเพิ่มใน Figma:**
  1. **ใน `platform-admin/frame_4.svg` (Modal บันทึกผล QC ของ Hub):**  
     - ปรับจากปุ่ม Pass/Fail ทั้งออเดอร์ ให้กลายเป็น **ตารางรายการการ์ดในออเดอร์ พร้อมปุ่ม Checkbox / Toggle ติ๊ก [Pass] หรือ [Fail] แยกทีละใบ** พร้อมช่องกรอกหมายเหตุตำหนิรายใบ
  2. **ใน `Checkout Flow/frame_7.svg` (หน้าติดตามสถานะของ Buyer):**  
     - แสดงแถบการ์ด A และ C สถานะ `กำลังจัดส่ง Leg 2`
     - แสดงแถบการ์ด B สถานะ `ไม่ผ่าน QC (การ์ดชำรุด) - คืนเงินแล้ว 500 บาท`

---

### ข้อที่ 3: แถบนับถอยหลังล็อกสต็อก 10 นาทีในหน้าชำระเงิน
* **อ้างอิงปัญหาใน `System & Edge Case FlawsMD`:** **ข้อ 4 (10-Minute Stock Hold & Concurrency)**
* **เชื่อมโยงกับฝั่ง User Flow อย่างไร:**
  - **เชื่อมกับ Flow `US-04 (Place Order & Checkout)`:** เมื่อผู้ซื้อกด *"Proceed to Checkout"* ระบบจะยิง API จองสต็อกไว้ 10 นาที (Redis Lock) หากผู้ซื้อไม่จ่ายเงินภายใน 10 นาที Flow จะตีกลับเป็น `PAYMENT_TIMEOUT` และปลดสต็อกคืนสู่ระบบ
* **สิ่งที่ต้องเพิ่มใน Figma:**
  1. **ใน `Checkout Flow/frame_4.svg` และ `frame_5.svg` (หน้าเลือกวิธีจ่ายเงิน & หน้า QR Code):**  
     - เพิ่มแถบเวลา Countdown ด้านบนสุด: `⏳ กรุณาชำระเงินภายใน 09:59 นาที เพื่อรักษาสิทธิ์คำสั่งซื้อการ์ดใบนี้` พร้อมหลอด Progress Bar สีแดง/ส้ม ค่อยๆ ลดลง

---

### ข้อที่ 4: หน้าต่างรายงานตำหนิให้ผู้ซื้อตัดสินใจ & การแยกค่าส่ง
* **อ้างอิงปัญหาใน `System & Edge Case FlawsMD`:** **ข้อ 5 (Logistics Cost Allocation & Defect Decision 4.1)**
* **เชื่อมโยงกับฝั่ง User Flow อย่างไร:**
  - **เชื่อมกับ Flow `US-04 (Checkout Summary)`:** ผู้ซื้อต้องเห็นค่าจัดส่ง Leg 2 แยกกับค่าบริการความปลอดภัย 100%
  - **เชื่อมกับ Flow `US-07 (QC Mismatch Sub-flow)`:** เมื่อ Hub พบตำหนิที่ไม่ได้แจ้ง Flow จะหยุดรอการตัดสินใจของผู้ซื้อ (`Waiting for Buyer Decision`) ➔ ส่งแจ้งเตือนให้ผู้ซื้อเปิดป๊อปอัปตัดสินใจ
* **สิ่งที่ต้องเพิ่มใน Figma:**
  1. **ใน `Checkout Flow/frame_1.svg` และ `frame_4.svg`:**  
     - ในกล่องสรุปยอดเงิน (Order Summary) ให้แจกแจง: `ค่าส่ง Leg 2 ถึงบ้าน: 50฿` + `ค่าบริการการันตีความปลอดภัยและตรวจแท้ (100% Security Fee): 30฿`
  2. **[สร้าง Modal ใหม่] หน้าต่างรายงานตำหนิ `Condition Mismatch Decision Modal` (ฝั่ง Buyer):**  
     - หัวข้อ: `⚠️ รายงานผลตรวจสภาพการ์ด: พบตำหนิที่ไม่ได้ระบุไว้`
     - แสดงภาพเปรียบเทียบ: **รูปถ่าย Macro 4K จาก Hub vs รูปเดิมของร้านค้า**
     - แสดงปุ่ม 2 ทางเลือก:
       - 🟢 **`[ ยอมรับสินค้าตามสภาพนี้ ]`** (ส่งต่อ Leg 2)
       - 🔴 **`[ ปฏิเสธสินค้าและขอเงินคืน 100% ]`** (คืนเงิน Escrow ทันที)

---

### ข้อที่ 5: Checkbox ซื้อประกันพัสดุ & แกลเลอรีดูคลิปแกะกล่อง QC Hub
* **อ้างอิงปัญหาใน `System & Edge Case FlawsMD`:** **ข้อ 6 (Shipping Insurance & QC Proof 5.1)**
* **เชื่อมโยงกับฝั่ง User Flow อย่างไร:**
  - **เชื่อมกับ Flow `US-04` และ `US-07`:** Flow มีจุดเลือกซื้อประกันพัสดุเพิ่มเติมทั้งฝั่งร้านค้า (Leg 1) และฝั่งผู้ซื้อ (Leg 2)
  - **เชื่อมกับ Flow `US-Admin-Dispute`:** เมื่อเกิดข้อพิพาท ทั้ง Buyer, Seller และ Admin ต้องสามารถเปิดดูวิดีโอแกะกล่องพัสดุและภาพถ่ายสภาพจริงของ Hub เพื่อเป็นพยานหลักฐาน
* **สิ่งที่ต้องเพิ่มใน Figma:**
  1. **ใน `Checkout Flow/frame_4.svg` (ฝั่งผู้ซื้อ):**  
     - เพิ่ม Checkbox: `[x] ซื้อประกันคุ้มครองพัสดุเสียหายระหว่างขนส่ง Leg 2 (+20฿)`
  2. **ใน `seller/frame_6.svg` (ฝั่งร้านค้าพิมพ์ใบปะหน้า Leg 1):**  
     - เพิ่ม Checkbox: `[x] ซื้อประกันพัสดุ Leg 1 ส่งเข้าศูนย์ Hub (+20฿)`
  3. **[สร้าง Modal/Viewer ใหม่] แกลเลอรีดูหลักฐาน `QC Camera Proof Viewer`:**  
     - ปุ่มบนหน้า Order Detail: `[ 🎥 ดูคลิปแกะกล่อง & ภาพถ่ายสภาพการ์ดจาก QC Hub ]`
     - วิดีโอ Player แสดงคลิปแกะกล่อง Unboxing และรูปภาพความละเอียดสูง 4 มุม

---

### ข้อที่ 6: การล็อกชื่อบัญชีถอนเงินให้ตรงกับ KYC
* **อ้างอิงปัญหาใน `System & Edge Case FlawsMD`:** **ข้อ 7 (KYC & Anti-Fraud Payout)**
* **เชื่อมโยงกับฝั่ง User Flow อย่างไร:**
  - **เชื่อมกับ Flow `US-Seller-Wallet`:** ในขั้นตอนการผูกบัญชีธนาคารเพื่อถอนเงิน ระบบจะไม่อนุญาตให้ผู้ขายพิมพ์ชื่อบัญชีเอง แต่จะดึงชื่อ-นามสกุลจากฐานข้อมูล KYC ที่ผ่านการอนุมัติแล้วมาล็อกไว้โดยอัตโนมัติ เพื่อป้องกันการฟอกเงิน
* **สิ่งที่ต้องเพิ่มใน Figma:**
  1. **ใน `seller/frame_11.svg` (หน้าตั้งค่าบัญชีธนาคาร):**  
     - ช่อง *"ชื่อเจ้าของบัญชี (Account Holder Name)"* ให้ปรับเป็นสีเทา (Disabled/Read-only)
     - มีไอคอนแม่กุญแจพร้อมป้ายกำกับ: `🔒 ล็อกชื่อบัญชีให้ตรงกับบัตรประชาชนที่ยืนยันตัวตน (นาย กันตินันท์ ศรีสุวรรณ) เท่านั้น`

---

## 🎯 สรุป Checklist สำหรับ Designer ในการอัปเดต Figma

- [ ] **Modal ใหม่ 1:** สร้างหน้าต่าง `Condition Mismatch Decision Modal` ในฝั่ง Buyer UI
- [ ] **Modal ใหม่ 2:** สร้างหน้าต่าง `QC Camera Proof Viewer` (วิดีโอ + รูปถ่าย 4K)
- [ ] **Checkout Flow (`frame_4, 5`):** ใส่แถบนับเวลา 10 นาที + Checkbox ประกันพัสดุ + แยกค่า Security Fee
- [ ] **Seller Center (`frame_5, 6`):** ใส่แถบ SLA Timer 48 ชม. + Checkbox ประกัน Leg 1
- [ ] **Seller Settings (`frame_11`):** ล็อกชื่อบัญชีธนาคารตรงกับ KYC
- [ ] **QC Hub Modal (`frame_4`):** เปลี่ยนเป็นการตรวจแบบ Item-Level Pass/Fail แยกรายใบ
- [ ] **Buyer Order Tracking (`frame_7`):** ใส่แถบ SLA Timer 72 ชม. + แสดงผล Partial Refund
