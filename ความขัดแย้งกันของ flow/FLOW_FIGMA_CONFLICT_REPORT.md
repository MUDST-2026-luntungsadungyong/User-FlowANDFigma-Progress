# 📋 รายงานข้อขัดแย้งระหว่าง User Flow และ Figma Design พร้อมแนวทางแก้ไข
> **โปรเจกต์:** TCG Trading Platform (DevOps & Escrow Marketplace)  
> **ไฟล์อ้างอิง Flow:** `ALL_DevOps_User Flow.pdf` (Swimlane Pages 13–31)  
> **ไฟล์อ้างอิง Figma:** `ExportBlock/SVG/` (7 Modules / 75 Screens)  
> **สถานะ:** ⚠️ พบข้อขัดแย้งเชิงกระบวนการทำงาน 6 ประเด็นหลักที่ต้องปรับแก้

---

## 📑 สารบัญ (Table of Contents)
1. [ภาพรวมของปัญหา (Executive Summary)](#1-ภาพรวมของปัญหา-executive-summary)
2. [ตารางเปรียบเทียบจุดขัดแย้งทั้ง 6 ประเด็น](#2-ตารางเปรียบเทียบจุดขัดแย้งทั้ง-6-ประเด็น)
3. [รายละเอียดเจาะลึกและแนวทางแก้ไขราย Flow (Deep-Dive Analysis & Solutions)](#3-รายละเอียดเจาะลึกและแนวทางแก้ไขราย-flow)
   - [ประเด็นที่ 1: ขั้นตอน Checkout ข้าม Address & Payment Selection (US-04)](#ประเด็นที่-1-ขั้นตอน-checkout-ข้าม-address--payment-selection-us-04)
   - [ประเด็นที่ 2: การจัดส่งแบบ Monolithic vs 2-Leg Shipping & QC Hub (US-07)](#ประเด็นที่-2-การจัดส่งแบบ-monolithic-vs-2-leg-shipping--qc-hub-us-07)
   - [ประเด็นที่ 3: หน้าสมัครสมาชิก Register ขาดฟิลด์ Email (US-01)](#ประเด็นที่-3-หน้าสมัครสมาชิก-register-ขาดฟิลด์-email-us-01)
   - [ประเด็นที่ 4: การลงขายการ์ดแบบพิมพ์เอง vs Master Catalog & Condition Grading (US-05-1)](#ประเด็นที่-4-การลงขายการ์ดแบบพิมพ์เอง-vs-master-catalog--condition-grading-us-05-1)
   - [ประเด็นที่ 5: การมองสต็อกการ์ดรวม vs Multi-Seller Marketplace Listings (US-02, US-03)](#ประเด็นที่-5-การมองสต็อกการ์ดรวม-vs-multi-seller-marketplace-listings-us-02-us-03)
   - [ประเด็นที่ 6: ฟีเจอร์ที่มีใน Figma แต่ตกหล่นไม่มีใน Flow](#ประเด็นที่-6-ฟีเจอร์ที่มีใน-figma-แต่ตกหล่นไม่มีใน-flow)
4. [แผนผัง Swimlane ที่แก้ไขใหม่ (Corrected Swimlane Architecture)](#4-แผนผัง-swimlane-ที่แก้ไขใหม่)

---

## 1. ภาพรวมของปัญหา (Executive Summary)

จากการตรวจสอบเทียบกันระหว่าง **User Flow (Swimlane ปัจจุบัน)** กับ **Figma UI Screens ที่ออกแบบไว้จริง** พบว่า:
* **ปัญหาหลัก:** ตัว Flow ในเอกสาร PDF ยังอิงตามโมเดล **"ร้านค้าออนไลน์ทั่วไป (Simple E-Commerce)"** ที่ขายของชิ้นเดียว ส่งชิ้นเดียว
* **ความเป็นจริงใน Figma:** แพลตฟอร์มถูกออกแบบเป็น **"C2C / B2C Escrow Marketplace"** ที่มีการตรวจสอบของแท้ผ่าน **QC Hub** และมีการแข่งขันของร้านค้าหลายร้านในการ์ดใบเดียวกัน (Multi-Seller)
* หากไม่แก้ไข User Flow ให้ตรงกับ Figma จะทำให้การพัฒนา **Backend APIs, Database Schema, และ DevOps Automation (CI/CD, Monitoring)** ผิดทิศทาง

---

## 2. ตารางเปรียบเทียบจุดขัดแย้งทั้ง 6 ประเด็น

| ลำดับ | จุดที่พบปัญหา (Feature) | สิ่งที่ User Flow ระบุไว้ (Before / Current Flow) | สิ่งที่ Figma UI ออกแบบไว้จริง (After / Figma Reality) | ผลกระทบต่อระบบ (System Impact) |
| :---: | :--- | :--- | :--- | :--- |
| **1** | **Checkout Flow (US-04)** | ตะกร้าสินค้า ➔ สรุปคำสั่งซื้อ ➔ **ข้ามไปหน้า QR Code จ่ายเงินทันที** | ตะกร้า ➔ **เลือกที่อยู่ (`frame_2`)** ➔ **เลือกวิธีส่ง (`frame_3`)** ➔ **เลือกวิธีจ่ายเงิน (`frame_4`)** ➔ QR Code | ขาด Payload ที่อยู่และวิธีส่งในการยิง API สร้าง Order |
| **2** | **Order Fulfillment (US-07)** | แอดมินกด "จัดส่ง" ➔ กรอกเลขพัสดุ ➔ สถานะเป็น Fulfilled จบในขั้นตอนเดียว | แยก 2 จังหวะ: **Seller ส่งเข้า Hub (Leg 1)** ➔ **Hub ตรวจสภาพ Pass/Fail (`frame_4`)** ➔ **Hub ส่งหา Buyer (Leg 2)** | ไม่มี Decision Point การตรวจ QC Pass/Fail ซึ่งเป็นหัวใจของ Escrow |
| **3** | **Sign Up / Register (US-01)** | ฟอร์มกรอกแค่ **Username** และ **Password** (2 ฟิลด์) | ฟอร์มมี **Username**, **Email**, และ **Password** (3 ฟิลด์ใน `auth/frame_2`) | ไม่สามารถส่ง Email Verification และลืมรหัสผ่านไม่ได้ |
| **4** | **Add Product (US-05-1)** | พิมพ์ชื่อการ์ด, เลือกเกม, อัปโหลดรูป, ใส่ราคา/สต็อกเองอิสระ | **ค้นหาจาก Master Card DB** ➔ เลือก **Condition (Mint/NM/LP)** ➔ อัปโหลดรูปสภาพจริง | ข้อมูลชื่อการ์ดสะกดไม่ตรงกัน ไม่สามารถรวมกลุ่มการ์ดใบเดียวกันได้ |
| **5** | **Card Detail & Cart (US-02, US-03)** | มองการ์ด 1 ใบมีสต็อกรวม และขึ้น Error สต็อกไม่พอบนหน้าการ์ดตรงๆ | หน้ารายละเอียดการ์ดแสดง **หลายร้านค้าที่ลงขาย (Multi-Seller)** + กดแล้วเปิด **Cart Drawer (`frame_6`)** | Logic การจองสต็อกผิดพลาด เพราะผู้ซื้อต้องซื้อจาก Seller เจาะจง |
| **6** | **ฟีเจอร์ตกหล่น (Missing Flows)** | ไม่มี Flow ลืมรหัสผ่าน, ไม่มี Flow ถอนเงินกระเป๋า, ไม่มี Flow Bulk Upload | มี UI ครบ: **Forgot Password (`auth/3-6`)**, **Seller Wallet (`seller/9-11`)**, **Bulk CSV (`seller/8`)** | ทีมพัฒนาจะไม่ได้สร้าง API และ Database Table รองรับฟีเจอร์เหล่านี้ |

---

## 3. รายละเอียดเจาะลึกและแนวทางแก้ไขราย Flow

---

### ประเด็นที่ 1: ขั้นตอน Checkout ข้าม Address & Payment Selection (US-04)
* **ปัญหาใน Flow:** ในหน้า 13–14 ของ PDF เมื่อกด Checkout จะยิง API สรุปยอดและสร้าง QR Code ทันที โดยไม่มีขั้นตอนให้ผู้ใช้เลือกที่อยู่จัดส่ง และไม่มีขั้นตอนให้เลือกวิธีชำระเงิน
* **สิ่งที่ถูกต้องตาม Figma:** ในโฟลเดอร์ `Checkout Flow/` มีหน้าจอ 4 ขั้นตอนที่ต้องผ่าน:
  1. `frame_1.svg` — ตรวจสอบรายการในตะกร้า (Cart Review)
  2. `frame_2.svg` — เลือกที่อยู่จัดส่งจาก Address Book หรือเพิ่มที่อยู่ใหม่ (Select Shipping Address)
  3. `frame_3.svg` — เลือกรูปแบบขนส่งเข้า QC Hub (Standard vs Express Insured)
  4. `frame_4.svg` — เลือกช่องทางชำระเงิน (PromptPay QR, Credit Card, TrueMoney) พร้อมแสดงป้าย Escrow Protection
  5. `frame_5.svg` — แสดงหน้า Dynamic QR Code พร้อมเวลานับถอยหลัง (Timer)
* **แนวทางแก้ไข:** ปรับปรุง Swimlane US-04 ให้มี Step การเลือก Address และ Payment Method ก่อนสร้าง Transaction ใน DB

---

### ประเด็นที่ 2: การจัดส่งแบบ Monolithic vs 2-Leg Shipping & QC Hub (US-07)
* **ปัญหาใน Flow:** ในหน้า 20 (US-07) Flow เขียนเสมือนว่า "แอดมินคนเดียว" เป็นคนแพ็คของและใส่เลข Tracking แล้วจบเป็น Fulfilled
* **สิ่งที่ถูกต้องตาม Figma:**
  - แพลตฟอร์มนี้เป็นการส่งแบบ **2-Leg Shipping (ส่งผ่านคนกลาง)**:
    - **Leg 1 (Seller ➔ Hub):** ผู้ขายกดรับออเดอร์ ➔ พิมพ์ใบปะหน้าเข้า Hub (`seller/frame_6`) ➔ กรอกเลขพัสดุ Leg 1 (`seller/frame_7`)
    - **Hub Inspection:** เจ้าหน้าที่ QC Hub เปิดกล่องตรวจเช็ค ➔ มีหน้าต่างบันทึกผล **QC Pass / QC Fail** (`platform-admin/frame_4`)
    - **Leg 2 (Hub ➔ Buyer):** หากผ่าน QC ➔ Hub สั่งพิมพ์ใบปะหน้าส่งให้ลูกค้าปลายทาง (`platform-admin/frame_5`) ➔ ลูกค้าตรวจรับ ➔ ปลดล็อกเงิน Escrow
    - **QC Fail Path:** หากไม่ผ่าน ➔ ระงับ Escrow ➔ ทำเรื่อง Refund คืนเงินลูกค้า และส่งการ์ดคืนผู้ขาย
* **แนวทางแก้ไข:** แยก Swimlane US-07 ออกเป็น 2 ฝั่งชัดเจน คือ **Seller Fulfillment (Leg 1)** และ **QC Hub Processing (Leg 2 + QC Decision)**

---

### ประเด็นที่ 3: หน้าสมัครสมาชิก Register ขาดฟิลด์ Email (US-01)
* **ปัญหาใน Flow:** หน้า 30 ระบุเพียง "กรอก Username และ Password สำหรับสร้างบัญชีใหม่"
* **สิ่งที่ถูกต้องตาม Figma:** `auth/frame_2.svg` มีช่องกรอก `Username`, `Email`, และ `Password` ชัดเจน
* **แนวทางแก้ไข:** เพิ่มฟิลด์ `Email` ใน Swimlane US-01 พร้อมเพิ่มขั้นตอนตรวจสอบรูปแบบอีเมล (Email Regex Validation) และส่ง Verification Link

---

### ประเด็นที่ 4: การลงขายการ์ดแบบพิมพ์เอง vs Master Catalog & Condition Grading (US-05-1)
* **ปัญหาใน Flow:** หน้า 27 ระบุว่าให้ผู้ขายกรอกชื่อการ์ดและชื่อเกมเองแบบ Text ธรรมดา
* **สิ่งที่ถูกต้องตาม Figma:** ใน `seller/frame_3.svg` ระบบใช้โมเดล **Card Catalog Search**:
  - ผู้ขายพิมพ์ค้นหาการ์ดจากฐานข้อมูล Master ของระบบ (เพื่อดึงรูป Official, หมายเลขการ์ด, ชุด Booster)
  - ผู้ขายเลือก **สภาพการ์ด (Condition):** `Mint (M)`, `Near Mint (NM)`, `Lightly Played (LP)`, `Moderately Played (MP)` หรือ `Graded (PSA/BGS)`
  - ผู้ขายอัปโหลดภาพถ่ายสภาพจริง (Actual Photos) ของการ์ดตนเองเพื่อยืนยันตำหนิ
* **แนวทางแก้ไข:** ปรับ Swimlane US-05-1 ให้เริ่มจาก Query Master Database แทนการกรอกชื่อการ์ดแบบอิสระ

---

### ประเด็นที่ 5: การมองสต็อกการ์ดรวม vs Multi-Seller Marketplace Listings (US-02, US-03)
* **ปัญหาใน Flow:** Flow มองว่าการ์ด 1 ใบมีสต็อกรวมก้อนเดียว และโยน Error สต็อกไม่พอบนหน้า Product Detail โดยตรง
* **สิ่งที่ถูกต้องตาม Figma:** ใน `Shop & Browse/frame_3.svg` เป็นหน้าจอ Marketplace ที่แสดงว่า **"มีร้านค้าไหนบ้างที่กำลังลงขายการ์ดใบนี้ ในราคาและสภาพเท่าใด"**
* **แนวทางแก้ไข:** ปรับ Swimlane US-02/03 ให้ผู้ซื้อเลือกสินค้าจากร้านค้าเฉพาะเจาะจง (Selected Seller Listing) ก่อนเพิ่มลงตะกร้า

---

### ประเด็นที่ 6: ฟีเจอร์ที่มีใน Figma แต่ตกหล่นไม่มีใน Flow
1. **Forgot & Reset Password Flow:** ใน `auth/frame_3` ถึง `frame_6` มีหน้าจอกู้รหัสผ่านครบวงจร แต่ใน Flow ไม่มีเลย ➔ **ต้องเพิ่ม Sub-flow US-01-Forgot**
2. **Bulk CSV Inventory Upload:** ใน `seller/frame_8` มีหน้าอัปโหลดสต็อกทีละหลายสิบใบด้วย CSV ➔ **ต้องเพิ่ม Sub-flow US-05-Bulk**
3. **Seller Wallet & Withdrawal:** ใน `seller/frame_9, 10, 11` มีระบบกระเป๋าเงินและสั่งถอนเงิน ➔ **ต้องเพิ่ม Sub-flow US-Seller-Wallet**
4. **Dispute & Refund Resolution:** ใน `platform-admin/frame_7` มีหน้าตัดสินข้อพิพาทเมื่อการ์ดมีปัญหา ➔ **ต้องเพิ่ม Sub-flow US-QC-Dispute**

---

## 4. แผนผัง Swimlane ที่แก้ไขใหม่ (Corrected Architecture)

ดูภาพรวมของแผนผังที่ถูกต้องได้ที่ไฟล์:
- 🌐 **[Flow_Discrepancies_and_Fixes_Overview.html](file:///C:/Users/Fugle/Downloads/Flow_devops/ExportBlock/%E0%B8%84%E0%B8%A7%E0%B8%B2%E0%B8%A1%E0%B8%82%E0%B8%B1%E0%B8%94%E0%B9%81%E0%B8%A2%E0%B9%89%E0%B8%87%E0%B8%81%E0%B8%B1%E0%B8%99%E0%B8%82%E0%B8%AD%E0%B8%87%20flow/Flow_Discrepancies_and_Fixes_Overview.html)** (Interactive Visual Dashboard & Exporter)
- 📊 **[Flow_Conflicts_Comprehensive_Swimlane.svg](file:///C:/Users/Fugle/Downloads/Flow_devops/ExportBlock/%E0%B8%84%E0%B8%A7%E0%B8%B2%E0%B8%A1%E0%B8%82%E0%B8%B1%E0%B8%94%E0%B9%81%E0%B8%A2%E0%B9%89%E0%B8%87%E0%B8%81%E0%B8%B1%E0%B8%99%E0%B8%82%E0%B8%AD%E0%B8%87%20flow/Flow_Conflicts_Comprehensive_Swimlane.svg)** (Full Vector Flowchart)
