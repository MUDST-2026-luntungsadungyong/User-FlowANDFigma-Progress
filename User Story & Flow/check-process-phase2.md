# 📊 Mythix TCG Platform — Phase 2 Feature Implementation & Process Checklist
> **เอกสารตรวจสอบสถานะและกระบวนการพัฒนาฟีเจอร์ประจำ Phase 2 (Implementation & Verification Checklist)**  
> **อ้างอิงหลักเกณฑ์จาก:** `final_user_story_phase_2.md` และ `user story phase 2_ other.md` (Strict Phase 2 Requirements Baseline)  
> **Repository:** `User-FlowANDFigma-Progress`  
> **Directory:** `/User Story & Flow/check-process-phase2.md`  
> **Target Branch:** `main`  
> **วันจัดทำ/ปรับปรุง:** พฤศจิกายน 2026  

---

## 📑 สารบัญ (Table of Contents)
1. [เกณฑ์การประเมินและการยึดสเปก Phase 2 เป็นหลัก (Evaluation Baseline)](#1-เกณฑ์การประเมินและการยึดสเปก-phase-2-เป็นหลัก-evaluation-baseline)
2. [บทสรุปสถานะภาพรวม (Executive Summary)](#2-บทสรุปสถานะภาพรวม-executive-summary)
3. [ตารางสรุปตามหมวดหมู่หลัก (Master Priority Matrix with Implementation Status)](#3-ตารางสรุปตามหมวดหมู่หลัก-master-priority-matrix-with-implementation-status)
4. [ตารางตรวจสอบเจาะลึกกลุ่ม Deferred เปรียบเทียบ Phase 1 vs Phase 2 Requirements](#4-ตารางตรวจสอบเจาะลึกกลุ่ม-deferred-เปรียบเทียบ-phase-1-vs-phase-2-requirements)
5. [ตารางตรวจสอบรายฟีเจอร์อย่างละเอียดทุกข้อ (Detailed User Stories Feature Checklist)](#5-ตารางตรวจสอบรายฟีเจอร์อย่างละเอียดทุกข้อ-detailed-user-stories-feature-checklist)
   - [5.1 กลุ่ม Must-Have: แกนหลักระบบประมูล (US-13, US-18)](#51-กลุ่ม-must-have-แกนหลักระบบประมูล-us-13-us-18)
   - [5.2 กลุ่ม Recommended to Develop: ฟีเจอร์ยกระดับตามคำแนะนำอาจารย์ (US-20, US-24, US-27)](#52-กลุ่ม-recommended-to-develop-ฟีเจอร์ยกระดับตามคำแนะนำอาจารย์-us-20-us-24-us-27)
   - [5.3 กลุ่ม Good to Have: วงจรประมูลสดและการส่งมอบ (US-14, US-15, US-16, US-17)](#53-กลุ่ม-good-to-have-วงจรประมูลสดและการส่งมอบ-us-14-us-15-us-16-us-17)
   - [5.4 กลุ่ม Deferred / Out of Scope: การตรวจเช็กเทียบสเปก Phase 2 (US-21 ถึง US-28)](#54-กลุ่ม-deferred--out-of-scope-การตรวจเช็กเทียบสเปก-phase-2-us-21-ถึง-us-28)
6. [สรุปข้อบกพร่องและสิ่งที่ต้องพัฒนาเพิ่มตามสเปก Phase 2 (Deficit Analysis & Action Plan)](#6-สรุปข้อบกพร่องและสิ่งที่ต้องพัฒนาเพิ่มตามสเปก-phase-2-deficit-analysis--action-plan)

---

## 1. เกณฑ์การประเมินและการยึดสเปก Phase 2 เป็นหลัก (Evaluation Baseline)

> ⚠️ **หลักการประเมินที่เคร่งครัด (Strict Compliance Rule):**  
> หากฟีเจอร์ใดมีโค้ดเก่าจาก Phase 1 แต่ **ยังทำงานไม่ได้ตามเกณฑ์การยอมรับ (Acceptance Criteria) และ API Endpoints ที่ระบุไว้ในเอกสาร User Story Phase 2** จะถือว่า **"ยังไม่ครบ (Incomplete)"** หรือ **"ยังไม่มีตามสเปก Phase 2"** ทันที จะไม่นับว่าเสร็จสมบูรณ์เพียงเพราะมีหน้าเว็บหรือตารางเดิมของ Phase 1

---

## 2. บทสรุปสถานะภาพรวม (Executive Summary)

จากการตรวจสอบระบบล่าสุดบน Branch `main` ของทั้ง **Backend (`tcg-store-backend`)** และ **Frontend (`tcg-store-frontend`)** โดยยึดข้อกำหนดของ Phase 2 เป็นเกณฑ์หลัก:

1. **กลุ่ม Must-Have (US-13, US-18): เสร็จสมบูรณ์ 100% (8/8 ข้อ)**  
   - ระบบประมูลครบวงจร: สร้างห้อง, ตั้งเวลา, Reserve Price, Buy-It-Now, แดชบอร์ดผู้ขาย, การหัก Commission และพอร์ตประมูลของผู้ซื้อ
2. **กลุ่ม Recommended to Develop (US-20, US-24, US-27): เสร็จ 60% (3/5 ข้อ)**  
   - `US-20` (Image Upload Policy & Zoom Magnifier): **ครบถ้วน 100%**
   - `US-24` (Promo/Voucher Engine): **ครบฝั่ง Buyer & Checkout** แต่ *ยังขาดหน้า Admin Promo Campaign UI (`US-24-2`)*
   - `US-27` (Weekly Stock & Profit Admin Report): **ยังไม่มีในระบบ (0%)**
3. **กลุ่ม Good-to-Have (US-14, US-15, US-16, US-17): เสร็จ 85% (17/20 ข้อ)**  
   - ระบบห้องประมูลสด WebSocket, กลไกเคาะราคา Manual/Proxy, Masked Identity, การตัดสินผู้ชนะ และโอนการ์ดเข้า Binder ทำงานได้จริง
4. **กลุ่ม Deferred / Extended (US-21, US-22, US-23, US-25, US-26, US-28): เมื่อยึดตามสเปก Phase 2 พบว่า "ยังไม่ครบเกือบทั้งหมด"**  
   - `US-21`: **ยังไม่ครบ** (ขาดค่าธรรมเนียมคำสั่งซื้อทั่วไป และขาด Monthly Dashboard/CSV ของผู้ขาย)
   - `US-22`: **ยังไม่ครบ** (ขาดปุ่ม Toggle Public/Private ใน My Collection และขาด Card Comparison Helper)
   - `US-23`: **ยังไม่ครบ** (กรองได้แค่การ์ดเดี่ยว ขาดหมวด Booster Pack, Box และ Accessories)
   - `US-25`: **ยังไม่ครบ** (ดูได้แค่ประวัติ ขาด 1-Click Reorder และขาด PDF Invoice Export)
   - `US-26`: **ยังไม่มี** (ขาด Low/Out of Stock Alert และ Prediction)
   - `US-28`: **มีเฉพาะค้นหาภาษาไทย (US-28-2)** แต่ *ยังขาด Typo Fuzzy Search (US-28-1)*

---

## 3. ตารางสรุปตามหมวดหมู่หลัก (Master Priority Matrix with Implementation Status)

> ตารางด้านล่างนำโครงสร้างดั้งเดิมจาก **หัวข้อที่ 2 ของ `final_user_story_phase_2.md`** มาเพิ่มคอลัมน์ประเมินสถานะตามเกณฑ์ข้อกำหนดของ Phase 2 อย่างเคร่งครัด:

| รหัสหมวด | ชื่อหมวดหมู่ (Module Title) | สถานะความสำคัญตามคำแนะนำอาจารย์ | จำนวน US ย่อย | เป้าหมายการส่งมอบ | มีในระบบหรือยัง (Status in System) | ผลการตรวจเทียบตาม Requirement Phase 2 อย่างเคร่งครัด |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| **US-13** | **Auction Listing & Setup**<br>*(สร้าง/ตั้งค่าประมูล, Reserve, Buy-It-Now)* | ⭐ **MUST HAVE** | 5 ข้อ | **Sprint 1 (Priority 1)** | 🟢 **ครบ 100%** | มีครบทุกฟังก์ชันตาม Acceptance Criteria (Draft, Schedule, Cancel, Reserve, Buyout) |
| **US-18** | **Auction Analytics & Financials**<br>*(คำนวณค่าธรรมเนียม, สถิติกำไรผู้ขาย/ผู้ซื้อ)* | ⭐ **MUST HAVE** | 3 ข้อ | **Sprint 1 (Priority 1)** | 🟢 **ครบ 100%** | มี Seller Analytics, Commission Deduction Policy และ Buyer Portfolio |
| **US-20** | **Card Image Upload Policy & Criteria Gate**<br>*(เกณฑ์บังคับรูปจริง vs ตัวเลือกเสริม + แว่นขยาย)* | 🚀 **RECOMMENDED** | 2 ข้อ | **Sprint 1 (Priority 1)** | 🟢 **ครบ 100%** | เกณฑ์ Mandatory/Optional ตรวจสอบเรียลไทม์ และแว่นขยาย Hover Zoom 2.5x ในหน้ารายละเอียดการ์ด |
| **US-24** | **Promotions & Discount Codes Engine**<br>*(ระบบคูปองและโค้ดส่วนลด Checkout)* | 🚀 **RECOMMENDED** | 2 ข้อ | **Sprint 2 (Priority 1)** | 🟡 **มีบางส่วน (70%)** | ใช้งานใน Checkout ได้จริง (`US-24-1`) แต่**ยังขาดหน้า Admin จัดการแคมเปญ (`US-24-2`)** |
| **US-27** | **Weekly Stock & Profit Admin Report**<br>*(รายงานสินค้าคงคลังและผลกำไรประจำสัปดาห์)* | 🚀 **RECOMMENDED** | 1 ข้อ | **Sprint 2 (Priority 1)** | 🔴 **ยังไม่มี (0%)** | **ยังไม่มีในระบบ** ไม่มี Scheduled Sunday Cron, รายงาน Stagnant 60 วัน และปุ่ม Export |
| **US-14** | **Auction Discovery & Live Arena**<br>*(หน้ารวมประมูล, WebSocket Room, Watchlist)* | 💡 **GOOD TO HAVE** | 5 ข้อ | **Sprint 2 (Priority 2)** | 🟢 **ครบ 100%** | หน้ารวมประมูลพร้อมแท็บด่วน, ห้องประมูลสด WebSocket, Mask Identity, Watchlist และ Badge การ์ดเกรด |
| **US-15** | **Bidding Engine & Proxy Bids**<br>*(เคาะสด, บิดอัตโนมัติ Max Bid, แจ้งเตือน Outbid)* | 💡 **GOOD TO HAVE** | 5 ข้อ | **Sprint 2 (Priority 2)** | 🟢 **ครบ 100%** | ระบบเคาะ Manual, Proxy Bidding บิดสู้แทนอัตโนมัติ, บันไดราคา Dynamic Increment และแจ้งเตือน Outbid |
| **US-16** | **Fair-Play & Anti-Fraud Controls**<br>*(Dynamic Anti-Sniping 3 นาที, ป้องกันปั่นราคา)* | 💡 **GOOD TO HAVE** | 4 ข้อ | **Sprint 2 (Priority 2)** | 🟡 **มีบางส่วน (75%)** | มี Anti-Shill ป้องกันผู้ขายเคาะการ์ดตัวเอง, ห้ามถอนบิด แต่ Anti-Sniping ยังไม่ได้ต่อ Trigger ขยายเวลาอัตโนมัติ |
| **US-17** | **Resolution, Settlement & Ownership**<br>*(ตัดสินผู้ชนะ, ชำระเงิน 48 ชม., โอนเข้า Binder)* | 💡 **GOOD TO HAVE** | 6 ข้อ | **Sprint 2 (Priority 2)** | 🟢 **เกือบครบ (90%)** | มี Daemon ตัดสินผู้ชนะ, เคลียร์ Reserve Not Met, โอนการ์ดเข้า Binder อัตโนมัติ, Second-Chance Offer |
| `US-21` | *Middleman Escrow Fee & Monthly Dashboard* | ⏸️ *DEFERRED (ข้ามไปก่อน)* | 2 ข้อ | รวมอยู่ใน US-18 แล้ว | ❌ **ยังไม่ครบตามสเปก** | **ไม่ครบ:** Phase 2 สั่งให้เก็บค่าตัวกลางใน**ทุกออเดอร์ทั่วไป** (`US-21-1`) และมี **Monthly Dashboard รายเดือน** (`US-21-2`) แต่ระบบปัจจุบันมีเฉพาะของ Auction |
| `US-22` | *Collection Privacy & Showcase Viewer* | ⏸️ *DEFERRED (ข้ามไปก่อน)* | 2 ข้อ | Phase 1 มี US-10-6 แล้ว | ❌ **ยังไม่ครบตามสเปก** | **ไม่ครบ:** Phase 1 มีแค่หน้าส่องการ์ดคนอื่น แต่**ไม่มีปุ่ม Toggle Public/Private** (`US-22-1`) และ**ไม่มีฟังก์ชัน Card Comparison Helper** (`US-22-2`) |
| `US-23` | *Product Categories & Advanced Filtering* | ⏸️ *DEFERRED (ข้ามไปก่อน)* | 1 ข้อ | ใช้ตัวกรองเดิม US-02-1 | ❌ **ยังไม่ครบตามสเปก** | **ไม่ครบ:** Phase 1 กรองได้เฉพาะการ์ดเดี่ยว (Single Cards) แต่**ไม่มีหมวด Booster Pack, Booster Box, Accessories** และไม่มี Dropdown บน Navbar |
| `US-25` | *Order History & Reorder, PDF Summary Export* | ⏸️ *DEFERRED (ข้ามไปก่อน)* | 2 ข้อ | ยกยอดหลังส่งมอบหลัก | ❌ **ยังไม่ครบตามสเปก** | **ไม่ครบ:** Phase 1 มีแค่ดูประวัติคำสั่งซื้อ แต่**ไม่มีปุ่ม 1-Click Reorder** (`US-25-1`) และ**ไม่มีปุ่มดาวน์โหลด PDF Invoice** (`US-25-2`) |
| `US-26` | *Out of Stock Alert & Smart Restock Prediction* | ⏸️ *DEFERRED (ข้ามไปก่อน)* | 2 ข้อ | ซับซ้อนเกินกรอบเวลา | 🔴 **ยังไม่มีในระบบ (0%)** | ไม่มีทั้ง Low/Out of Stock Alert, ปุ่ม Notify Me When Available และสูตรพยากรณ์ Restock |
| `US-28` | *Tolerant Search (Typo) & Multilingual Search* | ⏸️ *DEFERRED (ข้ามไปก่อน)* | 2 ข้อ | โบนัสเสริม ยกยอดไว้ก่อน | 🟡 **มีเฉพาะภาษาไทย (50%)** | **มีเฉพาะ US-28-2:** ค้นหาภาษาไทยผ่าน `card_search_names` (V19) แต่**ยังขาด Typo-Tolerant Fuzzy Search (US-28-1)** |

---

## 4. ตารางตรวจสอบเจาะลึกกลุ่ม Deferred เปรียบเทียบ Phase 1 vs Phase 2 Requirements

> เพื่อตอบคำถามอย่างโปร่งใสว่า **"ของเดิมใน Phase 1 ครบตาม Requirement ที่เขียนใน Phase 2 หรือไม่"** ตารางนี้แสดงช่องว่าง (Gap Analysis) ชัดเจนข้อต่อข้อ:

| รหัส US | สิ่งที่ Phase 2 ระบุไว้ใน Acceptance Criteria | สิ่งที่มีอยู่จริงจาก Phase 1 ในปัจจุบัน | สถานะตามสเปก Phase 2 | ช่องว่างที่ยังขาดอยู่จริง (Missing Gaps) |
| :---: | :--- | :--- | :---: | :--- |
| **US-21-1** | หักค่าตัวกลางจากทุกออเดอร์ปกติ (`/api/platform/fee-policy`), แสดงในหน้า Checkout และสรุปบัญชีกลาง | Phase 1 เป็นระบบ Contact Handoff ฟรี ไม่มีการหักค่าธรรมเนียมในคำสั่งซื้อปกติ | ❌ **ยังไม่ครบ** | ระบบคิดค่าธรรมเนียมเฉพาะระบบประมูล (Auction) แต่ยังไม่มีในออเดอร์ซื้อตรงทั่วไป |
| **US-21-2** | เมนู Seller Dashboard มีแท็บดูยอดขายรายเดือน พร้อม Dropdown เลือกเดือน/ปี, กราฟ 12 เดือน และปุ่ม Export CSV | Phase 1 มีแดชบอร์ดสรุปยอดขายสะสมรวมแบบตลอดกาล ไม่มีการจัดกลุ่มรายเดือน | ❌ **ยังไม่ครบ** | ขาดตัวเลือกฟิลเตอร์ปฏิทินรายเดือน, ขาดกราฟ 12 เดือนย้อนหลัง และขาดปุ่มดาวน์โหลด CSV |
| **US-22-1** | ปุ่มสวิตช์ Toggle Public vs. Private ใน `/my-collection`, ถ้า Private ต้องซ่อนจาก Leaderboard และบล็อก URL สาธารณะ (HTTP 403) | Phase 1 เก็บการ์ดเข้าอัลบั้มและแสดงใน Leaderboard เสมอ ไม่สามารถตั้งค่าปิดบังได้ | ❌ **ยังไม่ครบ** | ขาดฟิลด์ `is_private` ในฐานข้อมูล, ขาดสวิตช์ในหน้าเว็บ และขาด Logic บล็อกสิทธิ์เข้าชม |
| **US-22-2** | หน้าชมคอลเลกชันคนอื่น พร้อมฟังก์ชัน **Card Comparison Helper** (ป้ายบอกว่าคุณมีแล้วกี่ใบ/ยังไม่มี) และปุ่มแชร์ลิงก์ | Phase 1 มีหน้า `/collections/:userId` แสดงการ์ดของผู้อื่น | ❌ **ยังไม่ครบ** | ขาดระบบ Comparison Helper ที่เปรียบเทียบการ์ดคนอื่นกับการ์ดตนเอง และขาดปุ่มคัดลอกแชร์ URL |
| **US-23-1** | สถาปัตยกรรม 4 หมวดหมู่ (Single Cards, Booster Packs, Booster Boxes, Accessories) พร้อม Dropdown บน Navbar และตัวกรอง Dynamic | Phase 1 เป็นแคตตาล็อกการ์ดเดี่ยว (Single Cards) เท่านั้น มีตัวกรองสภาพและราคา | ❌ **ยังไม่ครบ** | ขาดหมวดหมู่กล่อง ซอง และอุปกรณ์สะสม, ขาด Dropdown บน Navbar และ API หมวดหมู่แยก |
| **US-25-1** | ปุ่ม **"1-Click Reorder"** ในหน้ารายละเอียดออเดอร์ ดึงสินค้าเดิมเข้าตะกร้าพร้อมตรวจสอบสต๊อกปัจจุบัน | Phase 1 มีหน้าดูประวัติคำสั่งซื้อ (`/profile/orders`) | ❌ **ยังไม่ครบ** | ขาดปุ่มสั่งซื้อซ้ำ, ขาดระบบตรวจสอบสต๊อกอัตโนมัติ และขาด API `POST /api/orders/{id}/reorder` |
| **US-25-2** | ปุ่ม **"Download PDF Invoice"** สร้างเอกสาร PDF ใบเสร็จพร้อม QR Code สแกนตรวจสอบสถานะออเดอร์ | Phase 1 แสดงรายละเอียดคำสั่งซื้อเป็น HTML ธรรมดาบนหน้าเว็บ | ❌ **ยังไม่ครบ** | ขาด Template PDF, ขาดไลบรารีสร้าง PDF และขาด API `GET /api/orders/{id}/invoice-pdf` |
| **US-26-1** | ระบบแจ้งเตือนสต๊อกหมด (ผู้ขาย) และปุ่ม **"Notify Me When Available"** ให้ผู้ซื้อกดติดตามการ์ดที่หมดสต๊อก | Phase 1 แสดงเพียงสถานะ Out of Stock บนการ์ดที่จำนวนเหลือ 0 | ❌ **ยังไม่มี** | ขาดระบบสมัครรับแจ้งเตือนสินค้ากลับมา (Back-in-stock Subscription) ทั้ง Frontend/Backend |
| **US-26-2** | AI / Smart Restock Prediction คำนวณความเร็วในการขาย (Sales Velocity) ทำนายวันหมดสต๊อกล่วงหน้า | Phase 1 ไม่มีระบบวิเคราะห์แนวโน้ม | ❌ **ยังไม่มี** | ขาดสูตรคำนวณและหน้า Dashboard แสดงป้ายเตือนการเติมสต๊อก |
| **US-28-1** | Typo-Tolerant Search ค้นหาคำสะกดผิด เช่น `"pokamon"` แล้วแสดงผลของ `"pokemon"` พร้อมข้อความแนะนำ | Phase 1 ใช้การค้นหาแบบ `ILIKE` ตรงตัวอักษร หากสะกดผิดจะไม่พบผลลัพธ์ | ❌ **ยังไม่ครบ** | ขาด Fuzzy Search Engine (Trigram / Levenshtein Distance) |
| **US-28-2** | ค้นหาชื่อการ์ดภาษาไทยข้ามภาษา เช่น ค้นหา `"ลิซาร์ดอน"` แล้วพบการ์ดภาษาอังกฤษ `"Charizard"` | มีตาราง `card_search_names` (Migration V19) และฐานข้อมูลคำศัพท์ภาษาไทยกว่า 2,052 คำ | 🟢 **มีตามสเปก** | ใช้งานได้แล้วใน Backend Catalog Service |

---

## 5. ตารางตรวจสอบรายฟีเจอร์อย่างละเอียดทุกข้อ (Detailed User Stories Feature Checklist)

### 5.1 กลุ่ม Must-Have: แกนหลักระบบประมูล (US-13, US-18)

| รหัส US | ชื่อฟีเจอร์ (Feature Title) | สถานะตามสเปก Phase 2 | รายละเอียดการ Implement ในระบบ |
| :--- | :--- | :---: | :--- |
| **US-13-1** | Create Card Auction Listing from Catalog/Collection | 🟢 **ครบถ้วน** | `POST /api/seller/auctions`, `AuctionWizardPage.tsx`, ตรวจสอบ Seller KYC, ดึงต้นแบบ, ล็อกสต๊อกการ์ด |
| **US-13-2** | Configure Hidden Reserve Price & Buy-It-Now Option | 🟢 **ครบถ้วน** | ฟิลด์ `reservePrice`, `buyItNowPrice`, `isReserveMet` ซ่อนตัวเลข Reserve จากผู้ซื้อ แสดงเฉพาะสถานะ |
| **US-13-3** | Schedule Auction Start Time & Duration | 🟢 **ครบถ้วน** | `POST /api/seller/auctions/schedule`, เลือกเริ่มทันทีหรือตั้งเวลาล่วงหน้า, เลือกระยะเวลา 24h, 3d, 5d, 7d |
| **US-13-4** | Seller Auction Dashboard & Draft Management | 🟢 **ครบถ้วน** | `GET /api/seller/auctions`, `MyAuctionsPage.tsx`, แท็บ Drafts, Active, Ended, Completed, แก้ไข/ลบ Draft ได้ |
| **US-13-5** | Seller Auction Early Cancellation Rules | 🟢 **ครบถ้วน** | `AuctionCancellationService.java`, `AuctionCancellation.tsx` (ยกเลิกได้เองถ้า 0 Bids, มีบิดต้องส่งหลักฐานให้แอดมิน) |
| **US-18-1** | Seller Auction Revenue, Cost & Net Margin Analytics | 🟢 **ครบถ้วน** | `GET /api/seller/auctions/analytics`, `AuctionAnalyticsPage.tsx` แสดง Gross Volume, Total Cost, Net Profit, Margin % |
| **US-18-2** | Platform Auction Fee & Commission Auto-Deduction | 🟢 **ครบถ้วน** | `AuctionCommissionService.java`, `AuctionCommissionPage.tsx`, หักค่าธรรมเนียมและแสดงใน Settlement Summary |
| **US-18-3** | Buyer Personal Auction Portfolio & Win-Rate Stats | 🟢 **ครบถ้วน** | `GET /api/user/auction-portfolio`, `AuctionPortfolioPage.tsx` แสดง Bids Placed, Wins, Win Rate %, Total Volume |

---

### 5.2 กลุ่ม Recommended to Develop: ฟีเจอร์ยกระดับตามคำแนะนำอาจารย์ (US-20, US-24, US-27)

| รหัส US | ชื่อฟีเจอร์ (Feature Title) | สถานะตามสเปก Phase 2 | รายละเอียดการ Implement ในระบบ |
| :--- | :--- | :---: | :--- |
| **US-20-1** | Mandatory vs. Optional Real Card Image Upload Gate | 🟢 **ครบถ้วน** | `ListingImagePolicy.java`, `imagePolicy.ts`, ประเมินเกณฑ์เรียลไทม์ (ราคา >= ฿500, การ์ดเกรด, มีตำหนิ บังคับรูปจริง >= 2 รูป) |
| **US-20-2** | High-Resolution Card Gallery with Zoom Magnifier | 🟢 **ครบถ้วน** | `CardPhotoMagnifierViewer.tsx`, `CardDetailPage.tsx` แท็บสลับ Official vs Actual Photos พร้อม Hover ซูม 2.5x |
| **US-24-1** | Promo Code / Voucher Application at Checkout | 🟢 **ครบถ้วน** | `VoucherController.java` (`/api/vouchers/validate`), `CheckoutVoucherModal.tsx`, หักส่วนลดจาก Subtotal ก่อนสั่งซื้อ |
| **US-24-2** | Admin Promo Campaign Management | 🟡 **มีบางส่วน (ขาด UI)** | มีตาราง `vouchers` (Flyway V13) และ Seed ในฐานข้อมูล แต่**ยังไม่มีหน้าเว็บ Admin UI สำหรับสร้างโค้ดใหม่** |
| **US-27-1** | Automated Weekly Stock & Profit Platform Governance Report | 🔴 **ยังไม่มี (0%)** | **ยังไม่มีในระบบ** ขาด Scheduled Sunday Cron, รายงาน Stagnant 60 วัน และปุ่ม Export สรุปประจำสัปดาห์ |

---

### 5.3 กลุ่ม Good to Have: วงจรประมูลสดและการส่งมอบ (US-14, US-15, US-16, US-17)

| รหัส US | ชื่อฟีเจอร์ (Feature Title) | สถานะตามสเปก Phase 2 | รายละเอียดการ Implement ในระบบ |
| :--- | :--- | :---: | :--- |
| **US-14-1** | Browse Auctions Hub with Multi-Filter & Ending Soon | 🟢 **ครบถ้วน** | `BuyerAuctionsPage.tsx` แท็บ Ending Soon, Hot Bids, Buy-It-Now, No Reserve และตัวกรอง |
| **US-14-2** | Live Auction Room with Real-Time WebSocket Ticker | 🟢 **ครบถ้วน** | `BuyerAuctionDetailPage.tsx` เชื่อมต่อ WebSocket `/auctions/{id}/live`, นับถอยหลังซิงก์ Server UTC |
| **US-14-3** | Transparent Public Bid History (Masked Identities) | 🟢 **ครบถ้วน** | `maskIdentity` แสดงชื่อนิรนาม `p***a` บนกระดานประมูล |
| **US-14-4** | Auction Watchlist & Ending Countdown Alert | 🟢 **ครบถ้วน** | `AuctionWatchlistService.java`, ปุ่มบันทึก Watchlist และแจ้งเตือนก่อนปิดประมูล |
| **US-14-5** | High-Value & Graded Card Verification Badge Display | 🟢 **ครบถ้วน** | แสดง Badge สถาบันเกรดพร้อมลิงก์ตรวจสอบเลขใบรับรอง (`buildCertificationUrl`) |
| **US-15-1** | Manual Direct Bidding with Real-Time Validation | 🟢 **ครบถ้วน** | `placeManualBid` ใน `AuctionBidService.java`, บันไดราคา Dynamic Increment Ladder |
| **US-15-2** | Automated Proxy Bidding Engine (Max Bid) | 🟢 **ครบถ้วน** | `placeProxyBid` ใน `AuctionBidService.java`, เคาะสู้แทนอัตโนมัติตามเพดาน Max Bid |
| **US-15-3** | Instant Buy-It-Now Purchase Flow | 🟢 **ครบถ้วน** | `executeBuyout`, ปิดห้องประมูลและสร้าง Order ทันที (`BUYOUT_COMPLETED`) |
| **US-15-4** | Instant Outbid In-App & Push Notification | 🟢 **ครบถ้วน** | `notifyOutbid`, ส่ง In-App Notification แจ้งเตือนผู้ที่โดนเคาะแซงทันที |
| **US-15-5** | Bid Confirmation Modal & Increment Ladder Helper | 🟢 **ครบถ้วน** | Modal ยืนยันการเคาะราคาและปุ่มลัดสเต็ป (+฿50, +฿100, +฿500) |
| **US-16-1** | Anti-Shill Bidding & Self-Bid Restrictions | 🟢 **ครบถ้วน** | ไม่อนุญาตให้ผู้ขายเคาะการ์ดของตนเอง (`You cannot bid on your own auction`) |
| **US-16-2** | Dynamic Anti-Sniping Engine (3-Minute Soft Close) | 🟡 **มีโครงสร้าง** | State Machine รองรับสถานะ `EXTENDED` แต่ยังไม่ได้ต่อ Event ขยายเวลา +3 นาทีอัตโนมัติใน Service |
| **US-16-3** | Bidder Eligibility & Deposit Credit Hold | 🟡 **มีโครงสร้าง** | ตรวจสอบสิทธิ์บัญชีผู้ใช้ แต่ยังไม่ได้บังคับล็อกวงเงินมัดจำเครดิต |
| **US-16-4** | Strict Bid Retraction Policy Enforcement | 🟢 **ครบถ้วน** | ห้ามผู้ซื้อกดยกเลิกบิดที่เคาะแล้วทุกกรณี |
| **US-17-1** | Automated Closing & Winner Determination Service | 🟢 **ครบถ้วน** | `AuctionLifecycle.java` และ `AuctionSettlementService.java` ตัดสินผู้ชนะเมื่อหมดเวลา |
| **US-17-2** | Settlement for Reserve-Not-Met & Unsold Auctions | 🟢 **ครบถ้วน** | ปิดสถานะ `RESERVE_NOT_MET` / `UNSOLD` และปลดล็อกการ์ดคืนสต๊อกผู้ขายอัตโนมัติ |
| **US-17-3** | Winner Checkout & Payment Gateway Window | 🟢 **ครบถ้วน** | สร้าง Order เชื่อมต่อ Flow ชำระเงิน |
| **US-17-4** | Automated Card Ownership Transfer into Personal Binder | 🟢 **ครบถ้วน** | `transferAuctionCardToPersonalBinder` โอนการ์ดเข้าอัลบั้มสะสมทันทีเมื่อออเดอร์เสร็จสิ้น |
| **US-17-5** | Second-Chance Offer for Runner-up Bidders | 🟢 **ครบถ้วน** | `sendSecondChanceOffer`, `respondSecondChanceOffer`, ตาราง `auction_second_chance_offers` |
| **US-17-6** | Defaulting Bidder Penalty & Cancelled Order Sync | 🟢 **ครบถ้วน** | ยกเลิกออเดอร์และคืนสิทธิ์การขายให้ผู้ขายเมื่อผู้ชนะไม่ติดต่อ |

---

### 5.4 กลุ่ม Deferred / Out of Scope: การตรวจเช็กเทียบสเปก Phase 2 (US-21 ถึง US-28)

| รหัส US | ชื่อฟีเจอร์ตามสเปก Phase 2 | ผลการตรวจสอบในระบบ | สรุปสถานะตามสเปก Phase 2 |
| :---: | :--- | :--- | :---: |
| **US-21-1** | Platform Fee ในทุกออเดอร์ปกติ | มีเฉพาะใน Auction ขาดใน Marketplace ทั่วไป | ❌ **ยังไม่ครบ** |
| **US-21-2** | Monthly Sales Dashboard & CSV Export | ขาดตัวเลือกฟิลเตอร์รายเดือน และขาด Export CSV | ❌ **ยังไม่ครบ** |
| **US-22-1** | Collection Privacy Toggle (Public vs Private) | ไม่มีสวิตช์ Toggle และไม่มีการล็อก 403 Forbidden | ❌ **ยังไม่ครบ** |
| **US-22-2** | Community Showcase + Comparison Helper | มีหน้าดูการ์ดคนอื่น แต่ไม่มี Card Comparison Helper | ❌ **ยังไม่ครบ** |
| **US-23-1** | Categories (Booster Pack, Box, Accessories) | มีแค่ Single Card ขาดกล่อง ซอง และอุปกรณ์เสริม | ❌ **ยังไม่ครบ** |
| **US-25-1** | 1-Click Fast Reorder Flow | มีแค่ดูประวัติคำสั่งซื้อ ขาดปุ่มสั่งซื้อซ้ำ | ❌ **ยังไม่ครบ** |
| **US-25-2** | Print Order Summary as PDF | ขาด Template PDF และปุ่มดาวน์โหลดใบเสร็จ | ❌ **ยังไม่ครบ** |
| **US-26-1** | Out of Stock & Back-in-Stock Alert | ไม่มีทั้งฝั่งเตือนผู้ขาย และฝั่ง Notify Me ผู้ซื้อ | 🔴 **ยังไม่มี (0%)** |
| **US-26-2** | Smart Restock Prediction based on Trends | ไม่มีสูตรพยากรณ์และหน้าวิเคราะห์แนวโน้ม | 🔴 **ยังไม่มี (0%)** |
| **US-28-1** | Typo-Tolerant Search (Fuzzy Matching) | ค้นหาแบบ `ILIKE` ตรงตัว ขาด Fuzzy String Matching | ❌ **ยังไม่ครบ** |
| **US-28-2** | Multilingual Search (Thai Card Search) | มีตาราง `card_search_names` (V19) ค้นหาภาษาไทยได้จริง | 🟢 **ครบถ้วน** |

---

## 6. สรุปข้อบกพร่องและสิ่งที่ต้องพัฒนาเพิ่มตามสเปก Phase 2 (Deficit Analysis & Action Plan)

เมื่อยึดข้อกำหนดของ Phase 2 เป็นเกณฑ์หลัก รายการฟีเจอร์ที่ระบบของเรายังขาดและต้องพัฒนาเพิ่มเติมแบ่งเป็น 2 ลำดับความสำคัญ:

### 🔴 ระดับวิกฤต (สิ่งที่อยู่ใน Scope หลักของ Phase 2 แต่ยังค้างอยู่):
1. **US-27-1 (Admin Weekly Governance Report):**  
   - ต้องเขียน Spring `@Scheduled` Job สรุปยอดทุกคืนวันอาทิตย์ (23:59 UTC)
   - ต้องสร้างตารางเก็บรายงานสรุปมูลค่าสต๊อก, ค่าธรรมเนียม, การ์ดขายดี, และการ์ดค้างสต๊อกเกิน 60 วัน (Stagnant Inventory)
   - ต้องทำหน้า Admin UI และปุ่ม Export ไฟล์
2. **US-24-2 (Admin Promo Campaign Manager):**  
   - ต้องสร้างหน้า UI ในส่วนแอดมินสำหรับสร้างโค้ดคูปอง กำหนดประเภทส่วนลด วันหมดอายุ และโควตาสิทธิ์ใช้งาน

### 🟡 ระดับส่วนขยาย (หากต้องการเก็บตกกลุ่ม Deferred ให้ครบตามสเปก Phase 2):
1. **US-22 (Collection Privacy & Comparison):** เพิ่มสวิตช์ Toggle Public/Private ใน `/my-collection` และทำป้าย Card Comparison Helper ในหน้า Showcase
2. **US-25 (Reorder & PDF Invoice):** เพิ่มปุ่ม Reorder เช็กสต๊อกลงตะกร้า และสร้างเอกสารสรุป PDF จากออเดอร์
3. **US-28-1 (Typo Tolerance):** เสริม PostgreSQL `pg_trgm` ในระบบค้นหาเพื่อรองรับการพิมพ์คำสะกดผิด
4. **US-21 (Marketplace Escrow Fee):** นำระบบคิดค่าธรรมเนียมจาก Auction ไปประยุกต์ใช้กับคำสั่งซื้อ Direct Sale ทั่วไป

---
> 📌 *เอกสารฉบับนี้จัดทำขึ้นโดยยึดตามข้อกำหนด User Stories Phase 2 อย่างเคร่งครัด เพื่อใช้เป็นเกณฑ์ตัดสินความสมบูรณ์ของโครงงานก่อนการประเมินผล*
