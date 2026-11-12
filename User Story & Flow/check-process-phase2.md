# 📊 Mythix TCG Platform — Phase 2 Feature Implementation & Process Checklist
> **เอกสารตรวจสอบสถานะและกระบวนการพัฒนาฟีเจอร์ประจำ Phase 2 (Implementation & Verification Checklist)**  
> **อ้างอิงหลักเกณฑ์จาก:** `final_user_story_phase_2.md` และ `user story phase 2_ other.md` (Strict Phase 2 Requirements Baseline)  
> **Repository:** `User-FlowANDFigma-Progress`  
> **Directory:** `/User Story & Flow/check-process-phase2.md`  
> **Target Branch:** `main`  
> **วันจัดทำ/ปรับปรุงล่าสุด:** 12 พฤศจิกายน 2026 (11:45 น.)  

---

## 📑 สารบัญ (Table of Contents)
1. [เกณฑ์การประเมินและการยึดสเปก Phase 2 เป็นหลัก (Evaluation Baseline)](#1-เกณฑ์การประเมินและการยึดสเปก-phase-2-เป็นหลัก-evaluation-baseline)
2. [บทสรุปสถานะภาพรวม (Executive Summary)](#2-บทสรุปสถานะภาพรวม-executive-summary)
3. [ตารางสรุปตามหมวดหมู่หลัก (Master Priority Matrix with Implementation Status)](#3-ตารางสรุปตามหมวดหมู่หลัก-master-priority-matrix-with-implementation-status)
4. [ตารางตรวจสอบเจาะลึกกลุ่ม Deferred เปรียบเทียบ Phase 1 vs Phase 2 Requirements](#4-ตารางตรวจสอบเจาะลึกกลุ่ม-deferred-เปรียบเทียบ-phase-1-vs-phase-2-requirements)
5. [ตารางตรวจสอบรายฟีเจอร์อย่างละเอียดทุกข้อ (Detailed User Stories Feature Checklist)](#5-ตารางตรวจสอบรายฟีเจอร์อย่างละเอียดทุกข้อ-detailed-user-stories-feature-checklist)
   - [5.1 กลุ่ม Must-Have: แกนหลักระบบประมูล (US-13, US-18)](#51-กลุ่ม-must-have-แกนหลักระบบประมูล-us-13-us-18)
   - [5.2 กลุ่ม Recommended to Develop: ฟีเจอร์ยกระดับตามคำแนะนำอาจารย์ (US-20, US-24, US-27)](#52-กลุ่ม-recommended-to-develop-ฟีเจอร์ยกระดับตามคำแนะนำอาจารย์-us-20-us-24-us-27)
   - [5.3 กลุ่ม Good to Have: วงจรประมูลสดและการกำกับดูแล (US-14, US-15, US-17, US-19)](#53-กลุ่ม-good-to-have-วงจรประมูลสดและการกำกับดูแล-us-14-us-15-us-17-us-19)
   - [5.4 กลุ่ม Deferred / Out of Scope: การตรวจเช็กเทียบสเปก Phase 2 (US-21 ถึง US-28)](#54-กลุ่ม-deferred--out-of-scope-การตรวจเช็กเทียบสเปก-phase-2-us-21-ถึง-us-28)
   - [5.5 หมวด US-29: ระบบการแจ้งเตือนหลายช่องทางและอีเมลอัตโนมัติ (US-29 Multi-Channel In-App & Email)](#55-หมวด-us-29-ระบบการแจ้งเตือนหลายช่องทางและอีเมลอัตโนมัติ-multi-channel-in-app--email-notification-system)
6. [สรุปข้อบกพร่องและสิ่งที่ต้องพัฒนาเพิ่มตามสเปก Phase 2 (Deficit Analysis & Action Plan)](#6-สรุปข้อบกพร่องและสิ่งที่ต้องพัฒนาเพิ่มตามสเปก-phase-2-deficit-analysis--action-plan)
7. [สรุปสถานะการทดสอบระบบของ Phase 2 (Automated Testing & Quality Gates)](#7-สรุปสถานะการทดสอบระบบของ-phase-2-automated-testing--quality-gates)

---

## 1. เกณฑ์การประเมินและการยึดสเปก Phase 2 เป็นหลัก (Evaluation Baseline)

> ⚠️ **หลักการประเมินที่เคร่งครัด (Strict Compliance Rule):**  
> หากฟีเจอร์ใดมีโค้ดเก่าจาก Phase 1 แต่ **ยังทำงานไม่ได้ตามเกณฑ์การยอมรับ (Acceptance Criteria) และ API Endpoints ที่ระบุไว้ในเอกสาร User Story Phase 2** จะถือว่า **"ยังไม่ครบ (Incomplete)"** หรือ **"ยังไม่มีตามสเปก Phase 2"** ทันที จะไม่นับว่าเสร็จสมบูรณ์เพียงเพราะมีหน้าเว็บหรือตารางเดิมของ Phase 1

---

## 2. บทสรุปสถานะภาพรวม (Executive Summary)

จากการตรวจสอบระบบล่าสุดบน Branch `main` ของทั้ง **Backend (`tcg-store-backend`)** และ **Frontend (`tcg-store-frontend`)** โดยยึดข้อกำหนดของ Phase 2 เป็นเกณฑ์หลัก:

1. **กลุ่ม Must-Have (US-13, US-18): เสร็จสมบูรณ์ 100% (8/8 ข้อ)**  
   - ระบบประมูลครบวงจร: สร้างห้อง, ตั้งเวลา, Reserve Price, Buy-It-Now, แดชบอร์ดผู้ขาย, การหัก Commission และพอร์ตประมูลของผู้ซื้อ
2. **กลุ่ม Recommended to Develop (US-20, US-24, US-27): เสร็จ ~90% (4.5/5 ข้อ)**  
   - `US-20` (Image Upload Policy & Zoom Magnifier): **ครบถ้วน 100%**
   - `US-24` (Promo/Voucher Engine): **ครบฝั่ง Buyer & Checkout (70%)** แต่ *ยังขาดหน้า Admin Promo Campaign UI (`US-24-2`)*
   - `US-27` (Weekly Stock & Profit Admin Report): **🟢 พัฒนาฝั่ง Frontend ครบถ้วน 100% บน `main` (พร้อม Cypress E2E) / Backend พัฒนาครบแล้วใน Branch `fix/weekly-admin-reports`** มีหน้า `AdminWeeklyReportsPage.tsx`, Service `weeklyReports.ts`, กราฟสรุปรายสัปดาห์, การ์ด Top Revenue/Top Profit, ตาราง Stagnant Inventory (ค้างสต๊อกเกิน 60 วัน) และปุ่ม Export CSV
3. **กลุ่ม Good-to-Have (US-14, US-15, US-17, US-19): เสร็จสมบูรณ์ 100% (20/20 ข้อ)**  
   - ระบบห้องประมูลสด WebSocket, กลไกเคาะราคา Manual/Proxy, Masked Identity, การตัดสินผู้ชนะ, โอนการ์ดเข้า Binder และการกำกับดูแล/ระงับฉุกเฉิน/จัดการข้อพิพาทสำหรับแอดมิน (`US-19`) **ครบถ้วน 100%** บน `main` (มี `AdminAuctionMonitorPage.tsx` สำหรับมอนิเตอร์กระดานประมูลสด, `AdminAuctionDisputesPage.tsx` & `ParticipantDisputesPage.tsx` สำหรับ Dispute Resolution Center ตรวจสอบสินค้าชำรุด/ของปลอม, `AuctionDisputeService.java`, `AuctionDisputeController.java`, ตาราง `auction_disputes`, `auction_emergency_controls` (V22) และ Audit Trail (V23))
   - *(หมายเหตุ: `US-16` ถูกตัดออกจาก Scope ตามมติกลุ่มเพื่อบริหารเวลาอย่างมีประสิทธิภาพ)*
4. **กลุ่ม Deferred / Extended (US-21, US-22, US-25, US-28): ผลการตรวจเช็กเทียบสเปก Phase 2**  
   - `US-21` (Middleman Escrow Fee & Monthly Dashboard): **🟢 พัฒนาเสร็จสมบูรณ์ 100%** (เพิ่ง merge เข้าสู่ `main` ล่าสุด — รองรับค่าธรรมเนียม Direct-Sale Checkout, ตารางนโยบาย `platform_fee_policy` (V21), แดชบอร์ดรายเดือน กราฟ 12 เดือน และปุ่ม Export CSV)
   - `US-25` (1-Click Reorder & PDF Invoice): **🟢 พัฒนาเสร็จสมบูรณ์ 100%** (merge เข้าสู่ `main` แล้ว)
   - `US-22` (Collection Privacy & Showcase): **🟢 พัฒนาเสร็จสมบูรณ์ 100%** (มีสวิตช์ Toggle Public/Private, บันทึกฐานข้อมูล V14, บล็อกสิทธิ์ 403, ปุ่มแชร์ URL, ตัวกรองชุดการ์ด, Secret Rare/Badges และฟังก์ชัน Card Comparison Helper ครบถ้วน)
   - `US-28` (Tolerant & Multilingual Search): **🟢 พัฒนาเสร็จสมบูรณ์ 100%** (มี Typo-Tolerant Fuzzy Search (Edit Distance <= 2), Did-you-mean Banner พร้อมปุ่มค้นหาคำเดิม, ค้นหาภาษาไทย V19 และ Hybrid Search ภาษาไทย + หมายเลขการ์ด)
5. **กลุ่มที่ตัดออกจาก Scope อย่างเป็นทางการ (De-scoped by Group Decision):**  
   - `US-16` (Fair-Play & Anti-Fraud Controls): **⚪ ตัดออกจาก Scope** เนื่องจากข้อจำกัดด้านเวลาและอยู่นอกขอบเขตหลัก (คงเหลือเฉพาะตรรกะพื้นฐานเดิม เช่น Anti-Shill ป้องกันผู้ขายเคาะการ์ดตัวเอง และห้ามถอนบิด)
   - `US-23` (Product Categories & Advanced Filtering): **⚪ ตัดออกจาก Scope** เนื่องจากข้อจำกัดด้านเวลา และระบบปัจจุบันรองรับการค้นหาและกรองการ์ดเดี่ยว (Single Cards) ได้อย่างสมบูรณ์แล้ว
   - `US-26` (Out of Stock Alert & Smart Restock Prediction): **⚪ ตัดออกจาก Scope** เนื่องจากความซับซ้อนของโมเดลพยากรณ์และข้อจำกัดด้านเวลา จัดเป็นฟีเจอร์นอกขอบเขตหลัก
6. **กลุ่มระบบแจ้งเตือนหลายช่องทาง (US-29 Multi-Channel In-App & Email Notification): 🟢 โครงสร้าง Backend Outbox & Frontend พร้อมทำงาน**  
   - Backend มีโครงสร้างสถาปัตยกรรม Transactional Outbox Pattern (`NotificationEmailDeliveryWorker.java`, `NotificationEmailService.java`, `notification_email_outbox` table V25/V28, และ `spring-boot-starter-mail`)
   - รองรับการส่งอีเมลครอบคลุมเหตุการณ์หลักตามสเปก 16 ข้อ (คำสั่งซื้อใหม่, ยกเลิกออเดอร์, แจ้งจัดส่งพร้อมเลขพัสดุและไฟล์แนบ PDF, ผลอนุมัติผู้ขาย, ผลการประมูล, การถูกเคาะแซง, เตือนผู้ชนะชำระเงิน, และผลตัดสินข้อพิพาท)
   - รองรับข้อมูลการจัดส่งและเลขพัสดุ (`tracking_number`, `shipping_carrier` V26) พร้อมหน้าตรวจยืนยันออเดอร์สาธารณะ (`OrderVerificationPage.tsx`) และระบบรีเซ็ตรหัสผ่านผ่านอีเมล (`ResetPasswordPage.tsx`, V29)

---

## 3. ตารางสรุปตามหมวดหมู่หลัก (Master Priority Matrix with Implementation Status)

> ตารางด้านล่างนำโครงสร้างดั้งเดิมจาก **หัวข้อที่ 2 ของ `final_user_story_phase_2.md`** มาเพิ่มคอลัมน์ประเมินสถานะตามเกณฑ์ข้อกำหนดของ Phase 2 อย่างเคร่งครัด:

| รหัสหมวด | ชื่อหมวดหมู่ (Module Title) | สถานะความสำคัญตามคำแนะนำอาจารย์ | จำนวน US ย่อย | เป้าหมายการส่งมอบ | มีในระบบหรือยัง (Status in System) | ผลการตรวจเทียบตาม Requirement Phase 2 อย่างเคร่งครัด |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| **US-13** | **Auction Listing & Setup**<br>*(สร้าง/ตั้งค่าประมูล, Reserve, Buy-It-Now)* | ⭐ **MUST HAVE** | 5 ข้อ | **Sprint 1 (Priority 1)** | 🟢 **ครบ 100%** | มีครบทุกฟังก์ชันตาม Acceptance Criteria (Draft, Schedule, Cancel, Reserve, Buyout) |
| **US-18** | **Auction Analytics & Financials**<br>*(คำนวณค่าธรรมเนียม, สถิติกำไรผู้ขาย/ผู้ซื้อ)* | ⭐ **MUST HAVE** | 3 ข้อ | **Sprint 1 (Priority 1)** | 🟢 **ครบ 100%** | มี Seller Analytics, Commission Deduction Policy และ Buyer Portfolio |
| **US-20** | **Card Image Upload Policy & Criteria Gate**<br>*(เกณฑ์บังคับรูปจริง vs ตัวเลือกเสริม + แว่นขยาย)* | 🚀 **RECOMMENDED** | 2 ข้อ | **Sprint 1 (Priority 1)** | 🟢 **ครบ 100%** | เกณฑ์ Mandatory/Optional ตรวจสอบเรียลไทม์ และแว่นขยาย Hover Zoom 2.5x ในหน้ารายละเอียดการ์ด |
| **US-24** | **Promotions & Discount Codes Engine**<br>*(ระบบคูปองและโค้ดส่วนลด Checkout)* | 🚀 **RECOMMENDED** | 2 ข้อ | **Sprint 2 (Priority 1)** | 🟡 **มีบางส่วน (70%)** | ใช้งานใน Checkout ได้จริง (`US-24-1`) แต่**ยังขาดหน้า Admin จัดการแคมเปญ (`US-24-2`)** |
| **US-27** | **Weekly Stock & Profit Admin Report**<br>*(รายงานสินค้าคงคลังและผลกำไรประจำสัปดาห์)* | 🚀 **RECOMMENDED** | 1 ข้อ | **Sprint 2 (Priority 1)** | 🟢 **Frontend ครบ 100% บน main / Backend พร้อมใน branch** | Frontend มีหน้า `AdminWeeklyReportsPage.tsx`, `weeklyReports.ts`, กราฟสรุป, ตารางสินค้าค้างสต๊อก 60 วัน, ปุ่มดาวน์โหลด CSV และ Cypress E2E `07_weekly_reports.cy.ts` / Backend โค้ดเสร็จสมบูรณ์ใน `fix/weekly-admin-reports` รอ Merge |
| **US-14** | **Auction Discovery & Live Arena**<br>*(หน้ารวมประมูล, WebSocket Room, Watchlist)* | 💡 **GOOD TO HAVE** | 5 ข้อ | **Sprint 2 (Priority 2)** | 🟢 **ครบ 100%** | หน้ารวมประมูลพร้อมแท็บด่วน, ห้องประมูลสด WebSocket, Mask Identity, Watchlist และ Badge การ์ดเกรด |
| **US-15** | **Bidding Engine & Proxy Bids**<br>*(เคาะสด, บิดอัตโนมัติ Max Bid, แจ้งเตือน Outbid)* | 💡 **GOOD TO HAVE** | 5 ข้อ | **Sprint 2 (Priority 2)** | 🟢 **ครบ 100%** | ระบบเคาะ Manual, Proxy Bidding บิดสู้แทนอัตโนมัติ, บันไดราคา Dynamic Increment และแจ้งเตือน Outbid |
| **US-16** | **Fair-Play & Anti-Fraud Controls**<br>*(Dynamic Anti-Sniping 3 นาที, ป้องกันปั่นราคา)* | ⚪ **OUT OF SCOPE**<br>*(ตัดออกจาก Scope)* | 4 ข้อ | **Sprint 2 (De-scoped)** | ⚪ **ตัดออกจาก Scope (De-scoped)** | **มติกลุ่มไม่พัฒนาต่อ:** เนื่องจากข้อจำกัดด้านเวลาและอยู่นอกขอบเขตหลัก (คงตรรกะพื้นฐานเดิม เช่น ห้ามเคาะการ์ดตัวเองและห้ามถอนบิด แต่ตัด Dynamic Anti-Sniping และ Deposit Hold ออก) |
| **US-17** | **Resolution, Settlement & Ownership**<br>*(ตัดสินผู้ชนะ, ชำระเงิน 48 ชม., โอนเข้า Binder)* | 💡 **GOOD TO HAVE** | 6 ข้อ | **Sprint 2 (Priority 2)** | 🟢 **ครบ 100%** | มี Daemon ตัดสินผู้ชนะ, เคลียร์ Reserve Not Met, โอนการ์ดเข้า Binder อัตโนมัติ, Second-Chance Offer, และระบบลงโทษ Defaulting Bidder (`DefaultCasesPage.tsx`) |
| **US-19** | **Auction Administration & Dispute Handling**<br>*(มอนิเตอร์สด, สั่งระงับ/ยกเลิกฉุกเฉิน, ตรวจสอบหลักฐาน)* | 💡 **GOOD TO HAVE** | 4 ข้อ | **Sprint 2 (Priority 2)** | 🟢 **ครบ 100%** | • Live Monitor Console (`AdminAuctionMonitorPage.tsx`)<br>• Emergency Controls & Audit (`V22`, `V23`)<br>• Dispute Resolution Center (`AdminAuctionDisputesPage.tsx`, `ParticipantDisputesPage.tsx`, `AuctionDisputeService.java`, `V27`)<br>• Cancellation & Security Audit Trail (`AdminAuditLogsController.java`) |
| `US-21` | *Middleman Escrow Fee & Monthly Dashboard* | ⏸️ *DEFERRED (ข้ามไปก่อน)* | 2 ข้อ | รวมอยู่ใน US-18 แล้ว | 🟢 **พัฒนาครบแล้ว (100%)** | **มีครบตามสเปก:** หัก Platform Fee ในคำสั่งซื้อทั่วไป (`GET /api/platform/fee-policy`), ตาราง `platform_fee_policy` (V21), หน้า Checkout แสดงค่าธรรมเนียม และ Seller Orders มี Monthly Dashboard พร้อมกราฟ 12 เดือน และ Export CSV |
| `US-22` | *Collection Privacy & Showcase Viewer* | ⏸️ *DEFERRED (ข้ามไปก่อน)* | 2 ข้อ | Phase 1 มี US-10-6 แล้ว | 🟢 **พัฒนาครบแล้ว (100%)** | **มีครบตามสเปก:** สวิตช์ Toggle Public vs Private ใน `/my-collection` (`/collection`), บล็อก 403 Forbidden สำหรับอัลบั้ม Private, ปุ่มแชร์ URL, ตัวกรองชุดการ์ด, Secret Rare/Badges และ Card Comparison Helper (`/api/public/collections/{userId}/compare`) |
| `US-23` | *Product Categories & Advanced Filtering* | ⚪ *OUT OF SCOPE (ตัดออก)* | 1 ข้อ | ใช้ตัวกรองเดิม US-02-1 | ⚪ **ตัดออกจาก Scope (De-scoped)** | **มติกลุ่มไม่พัฒนาต่อ:** ยืนยันรองรับเฉพาะแคตตาล็อกการ์ดเดี่ยว (Single Cards) ตามเดิม และตัดการขยายหมวด Booster Pack, Box, Accessories ออกเนื่องจากข้อจำกัดด้านเวลา |
| `US-25` | *Order History & Reorder, PDF Summary Export* | ⏸️ *DEFERRED (ข้ามไปก่อน)* | 2 ข้อ | ยกยอดหลังส่งมอบหลัก | 🟢 **พัฒนาครบแล้ว (100%)** | **มีครบตามสเปก:** `1-Click Reorder` (`POST /api/orders/{id}/reorder`), `Download PDF Invoice` (`GET /api/orders/{id}/invoice-pdf`), และ `OrderDetailPage.tsx` |
| `US-26` | *Out of Stock Alert & Smart Restock Prediction* | ⚪ *OUT OF SCOPE (ตัดออก)* | 2 ข้อ | ซับซ้อนเกินกรอบเวลา | ⚪ **ตัดออกจาก Scope (De-scoped)** | **มติกลุ่มไม่พัฒนาต่อ:** ยืนยันตัดระบบแจ้งเตือนสินค้ากลับมาและ AI Restock Prediction ออกอย่างเป็นทางการ เนื่องจากข้อจำกัดด้านเวลาและความซับซ้อนอยู่นอกขอบเขต |
| `US-28` | *Tolerant Search (Typo) & Multilingual Search* | ⏸️ *DEFERRED (ข้ามไปก่อน)* | 2 ข้อ | โบนัสเสริม ยกยอดไว้ก่อน | 🟢 **พัฒนาครบแล้ว (100%)** | **มีครบทั้งสองข้อย่อย:**<br>• `US-28-1`: Typo-Tolerant Fuzzy Search (Levenshtein Distance <= 2, แนะนำ Did-you-mean ใน CardDiscoveryPage และ API `/api/cards/search`)<br>• `US-28-2`: ค้นหาภาษาไทยผ่าน `card_search_names` (V19) + Hybrid Search (ไทย + เลขการ์ด) |
| **US-29** | **Multi-Channel Email & In-App Alerts**<br>*(ระบบแจ้งเตือน 16 เหตุการณ์สำคัญ)* | 🚀 **RECOMMENDED** | 3 ข้อ | **Sprint 2 (Priority 1)** | 🟢 **Backend Outbox & Frontend พร้อมทำงาน** | มีโครงสร้าง Transactional Outbox Worker (`NotificationEmailDeliveryWorker.java`, `NotificationEmailService.java`, V25/V28) เชื่อมต่ออีเมล 12 เหตุการณ์, รองรับแนบ PDF ใบเสร็จ, เลขพัสดุ Tracking V26, หน้ายืนยันออเดอร์ (`OrderVerificationPage.tsx`) และ Reset Password (V29) |

---

## 4. ตารางตรวจสอบเจาะลึกกลุ่ม Deferred เปรียบเทียบ Phase 1 vs Phase 2 Requirements

> เพื่อตอบคำถามอย่างโปร่งใสว่า **"ของเดิมใน Phase 1 ครบตาม Requirement ที่เขียนใน Phase 2 หรือไม่"** ตารางนี้แสดงช่องว่าง (Gap Analysis) ชัดเจนข้อต่อข้อ:

| รหัส US | สิ่งที่ Phase 2 ระบุไว้ใน Acceptance Criteria | สิ่งที่มีอยู่จริงจาก Phase 1 ในปัจจุบัน | สถานะตามสเปก Phase 2 | ช่องว่างที่ยังขาดอยู่จริง (Missing Gaps) |
| :---: | :--- | :--- | :---: | :--- |
| **US-21-1** | หักค่าตัวกลางจากทุกออเดอร์ปกติ (`/api/platform/fee-policy`), แสดงในหน้า Checkout และสรุปบัญชีกลาง | พัฒนาใน Phase 2 เรียบร้อย (`V21__platform_fee_policy_and_direct_sale_fee.sql`, `PlatformFeeController.java`, `PlatformFeeService.java`, `platformFee.ts`, `CheckoutPage.tsx`) | 🟢 **มีตามสเปก** | หักค่าตัวกลาง 5% (ขั้นต่ำ ฿20) จากยอด Direct-Sale ในหน้า Checkout และคำนวณเข้าบัญชีกลาง |
| **US-21-2** | เมนู Seller Dashboard มีแท็บดูยอดขายรายเดือน พร้อม Dropdown เลือกเดือน/ปี, กราฟ 12 เดือน และปุ่ม Export CSV | พัฒนาใน Phase 2 เรียบร้อย (`SellerOrderService.java`, `SellerOrdersPage.tsx`, API `/api/seller/orders/monthly-dashboard`) | 🟢 **มีตามสเปก** | มี Dropdown เลือกเดือน/ปี, สรุป KPI ยอดขาย/ค่าธรรมเนียม/กำไรสุทธิ, กราฟแท่งรายรับ 12 เดือน และปุ่ม Export CSV |
| **US-22-1** | ปุ่มสวิตช์ Toggle Public vs. Private ใน `/my-collection`, ถ้า Private ต้องซ่อนจาก Leaderboard และบล็อก URL สาธารณะ (HTTP 403) | พัฒนาครบถ้วนใน Phase 2 (`V14__add_collection_privacy_to_users.sql`, `CollectionController.java`, `MyCollectionPage.tsx`) | 🟢 **มีตามสเปก** | มีสวิตช์สลับสถานะในหน้า My Collection, บันทึกฟิลด์ `collection_privacy` และบล็อกผู้เยี่ยมชมด้วยหน้าจอ Private (403) |
| **US-22-2** | หน้าชมคอลเลกชันคนอื่น พร้อมฟังก์ชัน **Card Comparison Helper** (ป้ายบอกว่าคุณมีแล้วกี่ใบ/ยังไม่มี) และปุ่มแชร์ลิงก์ | พัฒนาครบถ้วนใน Phase 2 (`PublicCollectionController.java`, `PublicCollectionService.java`, `PublicCollectionPage.tsx`, `CollectionCard.tsx`) | 🟢 **มีตามสเปก** | มีหน้า Showcase `/collections/:userId`, กรองชื่อ/ชุดการ์ด/ความหายาก, แสดง Secret Rare/Badges, ปุ่มแชร์ URL และป้ายเปรียบเทียบสด Card Comparison Helper |
| **US-23-1** | สถาปัตยกรรม 4 หมวดหมู่ (Single Cards, Booster Packs, Booster Boxes, Accessories) พร้อม Dropdown บน Navbar และตัวกรอง Dynamic | Phase 1 เป็นแคตตาล็อกการ์ดเดี่ยว (Single Cards) เท่านั้น มีตัวกรองสภาพและราคา | ⚪ **ตัดออกจาก Scope (Out of Scope)** | **มติกลุ่มไม่พัฒนาต่อ:** ยึดการซื้อขายเฉพาะการ์ดเดี่ยว (Single Cards) ตามเดิม และตัดการขยายหมวดสินค้าอื่นเนื่องจากข้อจำกัดด้านเวลาและอยู่นอกขอบเขตหลัก |
| **US-25-1** | ปุ่ม **"1-Click Reorder"** ในหน้ารายละเอียดออเดอร์ ดึงสินค้าเดิมเข้าตะกร้าพร้อมตรวจสอบสต๊อกปัจจุบัน | พัฒนาใน Phase 2 เรียบร้อย (`CartService.java`, `OrderDetailPage.tsx`) | 🟢 **มีตามสเปก** | รองรับการตรวจสอบสต๊อกคงเหลือและดึงการ์ดเดิมเข้าตะกร้าพร้อมสั่งซื้อใหม่ |
| **US-25-2** | ปุ่ม **"Download PDF Invoice"** สร้างเอกสาร PDF ใบเสร็จพร้อม QR Code สแกนตรวจสอบสถานะออเดอร์ | พัฒนาใน Phase 2 เรียบร้อย (`InvoicePdfService.java`, `BuyerOrderController.java`) | 🟢 **มีตามสเปก** | รองรับการดาวน์โหลดไฟล์ PDF ใบเสร็จสั่งซื้อที่มี QR Code ผ่าน API |
| **US-26-1** | ระบบแจ้งเตือนสต๊อกหมด (ผู้ขาย) และปุ่ม **"Notify Me When Available"** ให้ผู้ซื้อกดติดตามการ์ดที่หมดสต๊อก (ทั้ง In-App & Email) | Phase 1 แสดงเพียงสถานะ Out of Stock บนการ์ดที่จำนวนเหลือ 0 | ⚪ **ตัดออกจาก Scope (Out of Scope)** | **มติกลุ่มไม่พัฒนาต่อ:** ตัดระบบแจ้งเตือนสินค้ากลับมาทั้ง In-App และ Email (Back-in-stock Subscription) ออกเนื่องจากข้อจำกัดด้านเวลาและอยู่นอกขอบเขตหลัก |
| **US-26-2** | AI / Smart Restock Prediction คำนวณความเร็วในการขาย (Sales Velocity) ทำนายวันหมดสต๊อกล่วงหน้า | Phase 1 ไม่มีระบบวิเคราะห์แนวโน้ม | ⚪ **ตัดออกจาก Scope (Out of Scope)** | **มติกลุ่มไม่พัฒนาต่อ:** ตัดการสร้างโมเดลคำนวณทำนายสต๊อกออกเนื่องจากอยู่นอกขอบเขตหลักและข้อจำกัดเวลา |
| **US-28-1** | Typo-Tolerant Search ค้นหาคำสะกดผิด เช่น `"pokamon"` แล้วแสดงผลของ `"pokemon"` พร้อมข้อความแนะนำ | พัฒนาครบถ้วนใน Phase 2 (`CardFuzzySearchService.java`, `CardSearchPage.java`, `CardController.java`, `ProductService.java`, `CardDiscoveryPage.tsx`) | 🟢 **มีตามสเปก** | ค้นหาคำสะกดผิด (Edit Distance <= 2) เช่น `"pokamon"`, `"chairzard"`, `"pikashu"`, ส่ง `didYouMean` และแสดง Suggestion Banner ในหน้าผลการค้นหา พร้อมปุ่มค้นหาคำเดิม |
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
| **US-27-1** | Automated Weekly Stock & Profit Platform Governance Report | 🟢 **Frontend ครบ / Backend พร้อม Merge** | • Frontend: `AdminWeeklyReportsPage.tsx`, `weeklyReports.ts`, `AdminWeeklyReportsPage.test.tsx`, Cypress E2E `07_weekly_reports.cy.ts` (สรุป Stock Added/Removed, Sold Units, Inventory Value, Top Revenue/Profit, Stagnant Inventory > 60 วัน, Export CSV)<br>• Backend: พร้อมสมบูรณ์ใน `fix/weekly-admin-reports` (`WeeklyReportScheduler.java`, `AdminWeeklyReportController.java`, `WeeklyReportService.java`, `WeeklyReportCsv.java`) |

---

### 5.3 กลุ่ม Good to Have: วงจรประมูลสดและการกำกับดูแล (US-14, US-15, US-17, US-19 — หมายเหตุ: US-16 ถูกตัดออกจาก Scope)

| รหัส US | ชื่อฟีเจอร์ (Feature Title) | สถานะตามสเปก Phase 2 | รายละเอียดการ Implement ในระบบ |
| :--- | :--- | :---: | :--- |
| **US-14-1** | Browse Auctions Hub with Multi-Filter & Ending Soon | 🟢 **ครบถ้วน** | `BuyerAuctionsPage.tsx` แท็บ Ending Soon, Hot Bids, Buy-It-Now, No Reserve และตัวกรอง |
| **US-14-2** | Live Auction Room with Real-Time WebSocket Ticker | 🟢 **ครบถ้วน** | `BuyerAuctionDetailPage.tsx` เชื่อมต่อ WebSocket `/auctions/{id}/live`, นับถอยหลังซิงก์ Server UTC |
| **US-14-3** | Transparent Public Bid History (Masked Identities) | 🟢 **ครบถ้วน** | `maskIdentity` แสดงชื่อนิรนาม `p***a` บนกระดานประมูล |
| **US-14-4** | Auction Watchlist & Ending Countdown Alert | 🟢 **ครบถ้วน** | `AuctionWatchlistService.java`, ปุ่มบันทึก Watchlist และแจ้งเตือนก่อนปิดประมูล |
| **US-14-5** | High-Value & Graded Card Verification Badge Display | 🟢 **ครบถ้วน** | แสดง Badge สถาบันเกรดพร้อมลิงก์ตรวจสอบเลขใบรับรอง (`buildCertificationUrl`) |
| **US-15-1** | Manual Direct Bidding with Real-Time Validation | 🟢 **ครบถ้วน** | `placeManualBid` ใน `AuctionBidService.java`, บันไดราคา Dynamic Increment Ladder |
| **US-15-2** | Automated Proxy Bidding Engine (Max Bid) | 🟢 **ครบถ้วน** | `placeProxyBid` ใน `AuctionBidService.java`, เเคาะสู้แทนอัตโนมัติตามเพดาน Max Bid |
| **US-15-3** | Instant Buy-It-Now Purchase Flow | 🟢 **ครบถ้วน** | `executeBuyout`, ปิดห้องประมูลและสร้าง Order ทันที (`BUYOUT_COMPLETED`) |
| **US-15-4** | Instant Outbid In-App & Push Notification | 🟢 **ครบถ้วน** | `notifyOutbid`, ส่ง In-App Notification แจ้งเตือนผู้ที่โดนเคาะแซงทันที |
| **US-15-5** | Bid Confirmation Modal & Increment Ladder Helper | 🟢 **ครบถ้วน** | Modal ยืนยันการเคาะราคาและปุ่มลัดสเต็ป (+฿50, +฿100, +฿500) |
| **US-16-1** | Anti-Shill Bidding & Self-Bid Restrictions | ⚪ **ตัดออกจาก Scope** | *(มีตรรกะพื้นฐานเดิม: ป้องกันผู้ขายเคาะการ์ดตนเอง)* มติกลุ่มตัด US-16 ออกจาก Scope การประเมินเนื่องจากข้อจำกัดด้านเวลา |
| **US-16-2** | Dynamic Anti-Sniping Engine (3-Minute Soft Close) | ⚪ **ตัดออกจาก Scope** | มติกลุ่มไม่พัฒนาต่อเนื่องจากข้อจำกัดด้านเวลาและอยู่นอกขอบเขตหลัก (คงเหลือเฉพาะโครงสร้างสถานะ `EXTENDED` เดิม) |
| **US-16-3** | Bidder Eligibility & Deposit Credit Hold | ⚪ **ตัดออกจาก Scope** | มติกลุ่มไม่พัฒนาต่อเนื่องจากข้อจำกัดด้านเวลาและอยู่นอกขอบเขตหลัก |
| **US-16-4** | Strict Bid Retraction Policy Enforcement | ⚪ **ตัดออกจาก Scope** | *(มีตรรกะพื้นฐานเดิม: ห้ามกดยกเลิกบิด)* มติกลุ่มตัด US-16 ออกจาก Scope การประเมินเนื่องจากข้อจำกัดด้านเวลา |
| **US-17-1** | Automated Closing & Winner Determination Service | 🟢 **ครบถ้วน** | `AuctionLifecycle.java` และ `AuctionSettlementService.java` ตัดสินผู้ชนะเมื่อหมดเวลา |
| **US-17-2** | Settlement for Reserve-Not-Met & Unsold Auctions | 🟢 **ครบถ้วน** | ปิดสถานะ `RESERVE_NOT_MET` / `UNSOLD` และปลดล็อกการ์ดคืนสต๊อกผู้ขายอัตโนมัติ |
| **US-17-3** | Winner Checkout & Payment Gateway Window | 🟢 **ครบถ้วน** | สร้าง Order เชื่อมต่อ Flow ชำระเงิน |
| **US-17-4** | Automated Card Ownership Transfer into Personal Binder | 🟢 **ครบถ้วน** | `transferAuctionCardToPersonalBinder` โอนการ์ดเข้าอัลบั้มสะสมทันทีเมื่อออเดอร์เสร็จสิ้น |
| **US-17-5** | Second-Chance Offer for Runner-up Bidders | 🟢 **ครบถ้วน** | `sendSecondChanceOffer`, `respondSecondChanceOffer`, ตาราง `auction_second_chance_offers` |
| **US-17-6** | Defaulting Bidder Penalty & Cancelled Order Sync | 🟢 **ครบถ้วน** | `AuctionDefaultCaseService.java`, `DefaultCasesPage.tsx`, `/api/admin/auctions/default-cases` แบนผู้ใช้เบี้ยวประมูล และซิงก์ยกเลิกออเดอร์ |
| **US-19-1** | Platform Admin Live Auction Monitoring Console | 🟢 **ครบถ้วน** | `AdminAuctionMonitorPage.tsx`, `AdminAuctionController.java`, `AdminAuctionService.java`, Flyway V22 (`V22__auction_emergency_controls.sql`) แสดงกระดานมอนิเตอร์ห้องประมูลสด พร้อมสถานะ Bids, Active Lots, และคำสั่ง Pause/Resume/Cancel ฉุกเฉิน |
| **US-19-2** | Emergency Auction Pause & Force-Cancellation Review | 🟢 **ครบถ้วน** | `AdminAuctionCancellationsPage.tsx`, `AdminAuctionCancellationController.java`, ตรวจสอบภาพถ่ายหลักฐานผู้ขายและอนุมัติ/ปฏิเสธคำขอยกเลิก |
| **US-19-3** | Auction Dispute Resolution Center (Counterfeit/Damage) | 🟢 **ครบถ้วน** | `AdminAuctionDisputesPage.tsx`, `ParticipantDisputesPage.tsx`, `OpenAuctionDispute.tsx`, `AuctionDisputeService.java`, `AuctionDisputeController.java`, Flyway V27 (`V27__auction_dispute_notification_types.sql`) เมนู Dispute Resolution Center แยกเฉพาะ รองรับการเปิดเคสพิพาท แนบหลักฐานภาพถ่าย และการตัดสินชี้ขาด |
| **US-19-4** | Immutable Security Audit Trail for Auction Actions | 🟢 **ครบถ้วน** | `AdminAuditLogsController.java`, `AuditLog.java`, ตาราง `audit_logs` บันทึกประวัติ Action, Timestamp, IP Address, Admin ID โดยห้ามลบ/แก้ไข |

---

### 5.4 กลุ่ม Deferred / Out of Scope: การตรวจเช็กเทียบสเปก Phase 2 (US-21 ถึง US-28)

| รหัส US | ชื่อฟีเจอร์ตามสเปก Phase 2 | ผลการตรวจสอบในระบบ | สรุปสถานะตามสเปก Phase 2 |
| :---: | :--- | :--- | :---: |
| **US-21-1** | Platform Fee ในทุกออเดอร์ปกติ | `GET /api/platform/fee-policy`, `platform_fee_policy` (V21), แสดงค่าธรรมเนียมใน Checkout | 🟢 **ครบถ้วน** |
| **US-21-2** | Monthly Sales Dashboard & CSV Export | `SellerOrdersPage.tsx` เพิ่ม Monthly Dashboard, เลือกเดือน/ปี, กราฟ 12 เดือน, ปุ่ม Export CSV | 🟢 **ครบถ้วน** |
| **US-22-1** | Collection Privacy Toggle (Public vs Private) | `GET/PUT/PATCH /api/collection/privacy` (`/api/user/collection/privacy`), `MyCollectionPage.tsx`, บล็อก 403 Forbidden เมื่อ Private | 🟢 **ครบถ้วน** |
| **US-22-2** | Community Showcase + Comparison Helper | หน้า `/collections/:userId`, สถิติ Secret Rare/Badges, กรองชุดการ์ด, ปุ่มแชร์ URL, และ Card Comparison Helper (`GET /api/public/collections/{userId}/compare`) | 🟢 **ครบถ้วน** |
| **US-23-1** | Categories (Booster Pack, Box, Accessories) | มติกลุ่มยืนยันไม่ทำต่อเนื่องจากข้อจำกัดด้านเวลา ยึดตามแคตตาล็อกการ์ดเดี่ยว (Single Cards) ใน Phase 1 | ⚪ **ตัดออกจาก Scope** |
| **US-25-1** | 1-Click Fast Reorder Flow | `POST /api/orders/{id}/reorder`, `CartService.java`, `OrderDetailPage.tsx` | 🟢 **ครบถ้วน** |
| **US-25-2** | Print Order Summary as PDF | `GET /api/orders/{id}/invoice-pdf`, `InvoicePdfService.java` รองรับ QR Code และดาวน์โหลด PDF | 🟢 **ครบถ้วน** |
| **US-26-1** | Out of Stock & Back-in-Stock Alert (In-App & Email) | มติกลุ่มยืนยันไม่ทำต่อเนื่องจากข้อจำกัดด้านเวลาและอยู่นอกขอบเขตหลัก | ⚪ **ตัดออกจาก Scope** |
| **US-26-2** | Smart Restock Prediction based on Trends | มติกลุ่มยืนยันไม่ทำต่อเนื่องจากข้อจำกัดด้านเวลาและอยู่นอกขอบเขตหลัก | ⚪ **ตัดออกจาก Scope** |
| **US-28-1** | Typo-Tolerant Search (Fuzzy Matching) | `CardFuzzySearchService.java`, `CardSearchPage.java`, `CardController.java`, `CardDiscoveryPage.tsx` | 🟢 **ครบถ้วน** |
| **US-28-2** | Multilingual Search (Thai Card Search) | มีตาราง `card_search_names` (V19) ค้นหาภาษาไทยได้จริง | 🟢 **ครบถ้วน** |

---

### 5.5 หมวด US-29: ระบบการแจ้งเตือนหลายช่องทางและอีเมลอัตโนมัติ (Multi-Channel In-App & Email Notification System)

| ที่ | เหตุการณ์ (Event) | ผู้รับ (Recipient) | ในเว็บตอนนี้ | แผนในเว็บ | แผนอีเมล | สถานะปัจจุบัน |
| :---: | :--- | :--- | :--- | :--- | :--- | :---: |
| **1** | ผู้ซื้อสั่งซื้อ/จองสำเร็จ | ผู้ซื้อ (Buyer) | มีใบยืนยันคำสั่งซื้อ (`OrderConfirmationModal`, `OrderDetailPage`) | ปรับปรุงหน้ายืนยันคำสั่งซื้อ | **ส่ง** (`ORDER_PLACED_BUYER` / `ORDER_RESERVED`) | 🟢 **พัฒนาแล้ว** (In-App + Email Outbox) |
| **2** | มีคำสั่งซื้อใหม่ | ผู้ขายแต่ละรายในออเดอร์ (Sellers) | มี In-App Notification และลิงก์ไปจัดการออเดอร์ `/workspace/orders` | ใช้ต่อและลิงก์ไปออเดอร์ | **ส่ง** (`ORDER_RESERVED`) | 🟢 **พัฒนาแล้ว** (In-App + Email Outbox) |
| **3** | ผู้ขายยืนยันคำสั่งซื้อ | ผู้ซื้อ (Buyer) | มีการปรับเปลี่ยนสถานะคำสั่งซื้อในระบบ | อัปเดตสถานะในระบบ | **ยังไม่ส่ง** | 🟢 **มีในระบบแล้ว** (In-App Status Update) |
| **4** | ผู้ซื้อยกเลิกคำสั่งซื้อ | ผู้ขาย (Seller) | มีการแจ้งเตือนในระบบ | เพิ่มการแจ้งเตือนในระบบ | **ส่ง** (`ORDER_CANCELLED_SELLER`) | 🟢 **พัฒนาแล้ว** (In-App + Email Outbox) |
| **5** | ผู้ขายยกเลิกคำสั่งซื้อ | ผู้ซื้อ (Buyer) | มีการแจ้งเตือนพร้อมระบุเหตุผล | เพิ่มการแจ้งเตือน พร้อมระบุเหตุผล | **ส่ง** (`ORDER_CANCELLED_BUYER`) | 🟢 **พัฒนาแล้ว** (In-App + Email Outbox) |
| **6** | ผู้ขายทำเครื่องหมายว่าส่งของแล้ว | ผู้ซื้อ (Buyer) | มีข้อมูลจัดส่ง เลขพัสดุ และชื่อขนส่ง (`tracking_number`, `shipping_carrier` V26) + หน้า `OrderVerificationPage.tsx` | ข้อมูลจัดส่งพร้อมเลขพัสดุและ QR Code | **ส่ง พร้อมเลขพัสดุและไฟล์แนบ PDF** (`ORDER_SENT_BUYER`, V28) | 🟢 **พัฒนาแล้ว** (In-App Tracking + Email Outbox พร้อม PDF) |
| **7** | ผู้ซื้อยืนยันว่าได้รับของ | ผู้ขาย (Seller) | มีการปรับสถานะคำสั่งซื้อเป็นเสร็จสิ้น | อัปเดตสถานะในระบบ | **ยังไม่ส่ง** | 🟢 **มีในระบบแล้ว** (In-App Status Update) |
| **8** | แอดมินตัดสินกรณีจัดส่งของออเดอร์ประมูล | ผู้ซื้อและผู้ขายที่เกี่ยวข้อง | มีผลตัดสินในหน้า Dispute Resolution Center (`AdminAuctionDisputesPage.tsx`, `ParticipantDisputesPage.tsx`) | เพิ่มผลตัดสินในเส้นทางออเดอร์ | **ส่ง** (`AUCTION_DISPUTE_DECIDED`, V27) | 🟢 **พัฒนาแล้ว** (Dispute Center + Email Outbox) |
| **9** | สมัครเป็นผู้ขาย | แอดมิน (Platform Admin) | มีคำขอใน Admin Verification Queue | ใช้ต่อ | **ยังไม่ส่ง** | 🟢 **มีในระบบแล้ว** (Admin Verification Queue) |
| **10** | อนุมัติ/ปฏิเสธผู้ขาย | ผู้สมัคร (Applicant) | มี In-App แจ้งเตือนสถานะการอนุมัติ | ใช้ต่อ | **ส่งผลการพิจารณา** (`SELLER_APPLICATION_APPROVED`, `REJECTED`) | 🟢 **พัฒนาแล้ว** (In-App + Email Outbox) |
| **11** | ขอเลิกประมูล/แอดมินตัดสิน | แอดมิน/ผู้ขาย | มีในระบบพิจารณาคำขอ (`AdminAuctionCancellationsPage.tsx`) | ใช้ต่อ | **ส่งผลตัดสินให้ผู้ขาย** (`AUCTION_CANCELLATION_DECIDED`) | 🟢 **พัฒนาแล้ว** (In-App + Email Outbox) |
| **12** | ถูกเสนอราคาสูงกว่า (Outbid) | ผู้ประมูลเดิม | มี Real-time WebSocket + In-App แจ้งเตือน | ใช้ต่อ | **ส่ง หากยังมีเวลาเสนอราคา** (`AUCTION_OUTBID`) | 🟢 **พัฒนาแล้ว** (In-App WebSocket + Email Outbox) |
| **13** | ชนะการประมูล (Auction Won) | ผู้ชนะ (Winner) | มี In-App แจ้งเตือนพร้อมปุ่มไปชำระเงิน | ใช้ต่อ | **ส่ง** (`AUCTION_WON`) | 🟢 **พัฒนาแล้ว** (In-App + Email Outbox) |
| **14** | ประมูลจบ (Auction Ended) | ผู้ขาย (Seller) | มี In-App แจ้งเตือนผลการประมูล | ใช้ต่อ | **ส่งเมื่อมีผู้ชนะและต้องดำเนินการ** (`AUCTION_ENDED_SELLER`) | 🟢 **พัฒนาแล้ว** (In-App + Email Outbox) |
| **15** | รายการที่ติดตามใกล้จบ | ผู้ติดตาม (Watchers) | มี In-App Watchlist Alert เตือนก่อนปิดประมูล | ใช้ต่อ | **ยังไม่ส่ง** | 🟢 **มีในระบบแล้ว** (In-App Watchlist Service) |
| **16** | ผู้ชนะไม่ดำเนินการ / ได้สิทธิ์ซื้อเป็นลำดับถัดไป | ผู้เกี่ยวข้อง / ผู้ได้รับสิทธิ์ | มี In-App แจ้งเตือนข้อเสนอสำรอง (`DefaultCasesPage.tsx`) | ใช้ต่อ | **ส่ง เพราะมีเวลาจำกัด** (`AUCTION_DEFAULTED_WARNING`, `AUCTION_SECOND_CHANCE`) | 🟢 **พัฒนาแล้ว** (In-App + Email Outbox) |

---

## 6. สรุปข้อบกพร่องและสิ่งที่ต้องพัฒนาเพิ่มตามสเปก Phase 2 (Deficit Analysis & Action Plan)

เมื่อยึดข้อกำหนดของ Phase 2 เป็นเกณฑ์หลัก รายการฟีเจอร์ที่ระบบของเรายังขาดและสิ่งที่ต้องดำเนินการเพิ่มเติม มีดังนี้:

### 🔴 ระดับสิ่งที่ยังค้างอยู่จริงใน Scope หลักของ Phase 2:
1. **US-24-2 (Admin Promo Campaign Manager UI):**  
   - มีฐานข้อมูล `vouchers` (Flyway V13) และ API ตรวจสอบโค้ดแล้ว แต่**ยังขาดหน้าเว็บ Admin UI สำหรับสร้าง แก้ไข และปิดการใช้งานแคมเปญคูปอง**
2. **US-27-1 Backend Main Integration:**  
   - โค้ด Backend สรุปยอดอัตโนมัติ (`WeeklyReportScheduler.java`), API (`AdminWeeklyReportController.java`) และ Export CSV (`WeeklyReportCsv.java`) พัฒนาเสร็จสมบูรณ์แล้วใน Branch `fix/weekly-admin-reports` **รอการ Merge เข้าสู่ Branch `main` ของ Backend** (Frontend บน `main` มีหน้า `AdminWeeklyReportsPage.tsx` และ Cypress E2E รองรับเรียบร้อยแล้ว)
3. **US-29 Production Mail Relay Deployment:**  
   - ระบบ Transactional Outbox Worker (`NotificationEmailDeliveryWorker.java`) และ Template อีเมล 12 เหตุการณ์พัฒนาและผ่านการทดสอบแล้ว เหลือเพียงการตั้งค่า Environment Variable สำหรับ SMTP Relay จริง (`SPRING_MAIL_HOST`, `SPRING_MAIL_USERNAME`, `SPRING_MAIL_PASSWORD`) บนเครื่อง Server ปลายทาง

### 🟢 รายการที่พัฒนาเสร็จสมบูรณ์เพิ่มเติมแล้ว (Recently Completed):
1. **US-19 (Auction Administration & Dispute Handling):** ✅ **ครบถ้วน 100%** (มีทั้งกระดาน Live Monitor `AdminAuctionMonitorPage.tsx`, ศูนย์จัดการข้อพิพาท `AdminAuctionDisputesPage.tsx`, และ Security Audit Trail ครบครัน)
2. **US-28-1 & US-28-2 (Typo Tolerance & Thai Search):** ✅ **ครบถ้วน 100%** (ค้นหาคำสะกดผิด Levenshtein Distance <= 2, แนะนำคำค้น, และค้นหาการ์ดภาษาไทย)
3. **US-21 (Platform Fee & Monthly Dashboard):** ✅ **ครบถ้วน 100%** (หักค่าตัวกลางคำสั่งซื้อทั่วไป และแดชบอร์ดรายรับ 12 เดือนของผู้ขาย)
4. **US-22 (Collection Privacy & Showcase):** ✅ **ครบถ้วน 100%** (สวิตช์ Toggle Public/Private, บล็อก 403, และ Card Comparison Helper)
5. **US-25 (1-Click Reorder & PDF Invoice):** ✅ **ครบถ้วน 100%** (สั่งซื้อซ้ำใน 1 คลิก และดาวน์โหลดใบเสร็จ PDF พร้อม QR Code)

### ⚪ รายการที่ตัดออกจาก Scope ตามมติกลุ่มอย่างเป็นทางการ (De-scoped Features):
1. **US-16 (Fair-Play & Anti-Fraud Controls):**  
   - ตัดการพัฒนา Dynamic Anti-Sniping อัตโนมัติ และ Deposit Credit Hold ออกจากขอบเขตประเมินเนื่องจากข้อจำกัดด้านเวลา (คงไว้เฉพาะกฎพื้นฐานเดิมในระบบ เช่น ห้ามเคาะการ์ดตนเอง และห้ามกดยกเลิกบิด)
2. **US-23 (Product Categories & Advanced Filtering):**  
   - ตัดการขยายหมวดสินค้า Booster Pack, Booster Box และ Accessories ออกจากขอบเขตประเมิน โดยยืนยันให้ระบบมุ่งเน้นการซื้อขายเฉพาะการ์ดเดี่ยว (Single Cards) ตามสเปกหลักของแพลตฟอร์ม
3. **US-26 (Out of Stock Alert & Smart Restock Prediction):**  
   - ตัดระบบสมัครรับแจ้งเตือนสินค้ากลับมา (Back-in-stock Subscription ทั้ง In-App และ Email) และระบบ AI/สถิติพยากรณ์การเติมสต๊อกสินค้าออก เนื่องจากข้อจำกัดด้านเวลาและความซับซ้อนอยู่นอกขอบเขต

---

## 7. สรุปสถานะการทดสอบระบบของ Phase 2 (Automated Testing & Quality Gates)

เพื่อให้การส่งมอบโครงงานมีความน่าเชื่อถือและผ่านเกณฑ์การประเมินคุณภาพซอฟต์แวร์ ระบบได้รับการออกแบบและสร้างชุดทดสอบอัตโนมัติสำหรับฟีเจอร์ Phase 2 ดังนี้:

### 7.1 Cypress End-to-End (E2E) Tests ฝั่ง Frontend
| ชุดทดสอบ (Spec File) | ขอบเขต User Story ที่ครอบคลุม | สิ่งที่ทดสอบจริง | สถานะ |
| :--- | :--- | :--- | :--- | :---: |
| `07_weekly_reports.cy.ts` | **US-27:** รายงานสินค้าคงคลังและผลกำไรประจำสัปดาห์ | ตรวจสอบหน้าแดชบอร์ดสรุปรายสัปดาห์, การแสดงผลสต๊อกคงเหลือ, รายการ Stagnant Inventory > 60 วัน, การ์ด Top Performers และการดาวน์โหลดไฟล์ CSV | 🟢 ผ่าน 100% |
| `15_live_auction_journey.cy.ts` | **US-13:** สร้าง/ตั้งค่าประมูล | สร้างห้องประมูลจากคลังสินค้า, ล็อกสต็อกการ์ด, เผยแพร่ (Publish) และกดยกเลิกคืนสต็อก | 🟢 พร้อมใช้งาน |
| `18_live_auction_settlement.cy.ts` | **US-13, 14, 15, 17, 18:** วงจรประมูลสด | เชื่อมต่อ WebSocket สด, เสนอราคา, Watchlist, ซื้อทันที (Buy-It-Now), ตัดสินผู้ชนะ และสร้าง Order อัตโนมัติ | 🟢 พร้อมใช้งาน |
| `design/07_auction_default_cases_http.cy.ts` | **US-17-6:** ผู้ชนะเบี้ยวประมูล | ตรวจสอบเคสเบี้ยวประมูล (Default Cases) ฝั่งผู้ขาย และการอนุมัติ/ปฏิเสธ/ย้อนคำตัดสินของแอดมิน | 🟢 ผ่าน 100% |
| `design/06_auction_management_http.cy.ts` | **US-13 & US-19:** กำกับดูแลประมูล | การบันทึกฉบับร่างห้องประมูล (Draft Idempotency) และคำขอยกเลิกฉุกเฉิน | 🟢 ผ่าน 100% |
| `17_actual_card_photos.cy.ts`<br>`design/05_actual_card_photos_http.cy.ts` | **US-20:** รูปถ่ายจริงหลายมุม | ตรวจสอบนโยบายบังคับแนบรูปถ่ายการ์ดจริงหน้า-หลัง (Mandatory Card Photos Policy) และแว่นขยาย | 🟢 ผ่าน 100% |
| `10_collection_and_leaderboard.cy.ts` | **US-22:** คอลเลกชัน & ความเป็นส่วนตัว | การเข้าถึง Binder Collection และการเปิด/ปิดสิทธิ์แสดงผล (Public vs Private) | 🟢 ผ่าน 100% |

> *หมายเหตุ: สำหรับ `15_live_auction_journey.cy.ts` และ `18_live_auction_settlement.cy.ts` มีการกำหนด Flag `AUCTION_LIVE_E2E=true` สำหรับการรัน Live End-to-End กับเซิร์ฟเวอร์และฐานข้อมูลจริง*

### 7.2 Backend Integration & Concurrency Tests ฝั่ง Spring Boot
| ชุดทดสอบ (Test Class) | ขอบเขตการทดสอบ | สิ่งที่ทดสอบจริง | สถานะ |
| :--- | :--- | :--- | :---: |
| `AuctionConcurrencyPostgresTests.java` | **US-15:** Concurrency เคาะราคา | ทดสอบ Race Condition และ Pessimistic Locking เมื่อมีผู้เสนอราคาพร้อมกันในระดับ PostgreSQL | 🟢 ผ่าน |
| `BuyerAuctionIntegrationTests.java` | **US-14, 15, 18:** ระบบประมูลผู้ซื้อ | ทดสอบ Lifecycle ประมูลสด, WebSocket, Proxy Bid, Buy-it-now และหักค่าธรรมเนียม Platform Fee | 🟢 ผ่าน |
| `AdminAuctionDisputeIntegrationTests.java`<br>`AuctionDisputeServiceTest.java` | **US-19:** ข้อพิพาทประมูล & Dispute Center | ทดสอบกระบวนการเปิดเคสพิพาท, การแนบหลักฐานภาพถ่าย, การตัดสินของแอดมิน และการอัปเดตสถานะ | 🟢 ผ่าน |
| `AdminAuctionServiceTest.java` | **US-19:** มอนิเตอร์ & ระงับฉุกเฉิน | ทดสอบคำสั่ง Pause, Resume, และ Force Cancel ห้องประมูลฉุกเฉินจากฝั่ง Admin Console | 🟢 ผ่าน |
| `BuyerOrderControllerIntegrationTests.java` | **US-25:** สั่งซื้อซ้ำ & ดาวน์โหลด PDF | ทดสอบ `POST /api/orders/{id}/reorder` (สต็อกขาด, ดึงเข้าตะกร้า) และ `GET /api/orders/{id}/invoice-pdf` (สิทธิ์เจ้าของ) | 🟢 ผ่าน |
| `InvoicePdfServiceTest.java` | **US-25:** การสร้างไฟล์ PDF | ทดสอบความสมบูรณ์ของโครงสร้างไฟล์ PDF (%PDF Header, QR Code, Verification Layout) | 🟢 ผ่าน |
| `VoucherServiceTest.java` & `CheckoutControllerIntegrationTests.java` | **US-24:** โค้ดส่วนลดโปรโมชัน | ทดสอบการคำนวณและหักส่วนลดโค้ดโปรโมชันในขั้นตอนชำระเงิน และบันทึกประวัติการใช้งาน | 🟢 ผ่าน |
| `PlatformFeeServiceTest.java` & `SellerOrderServiceUnitTest.java` | **US-21:** ค่าตัวกลาง & แดชบอร์ดรายเดือน | ทดสอบกฎการคำนวณ Platform Fee 5% และการสรุปยอดขายรายเดือน 12 เดือนพร้อม Export | 🟢 ผ่าน |
| `NotificationEmailDeliveryWorkerTest.java`<br>`NotificationEmailServiceTest.java` | **US-29:** ระบบส่งอีเมล Outbox | ทดสอบการดึงคิวอีเมล Outbox, การส่งซ้ำแบบ Exponential Backoff, Dead-letter handling และการแนบ PDF | 🟢 ผ่าน |
| `WeeklyReportPostgresTests.java`<br>`WeeklyReportServiceTests.java` | **US-27:** การคำนวณรายงานและ CSV Export | ทดสอบการประมวลผลสรุปยอดขาย, ต้นทุน, กำไร, Stagnant Inventory เกิน 60 วัน และการสร้างไฟล์ CSV | 🟢 ผ่าน (บน branch) |

---
> 📌 *เอกสารฉบับนี้จัดทำขึ้นและปรับปรุงตามมติของกลุ่ม โดยยึดตามข้อกำหนด User Stories Phase 2 อย่างเคร่งครัด เพื่อใช้เป็นเกณฑ์ตัดสินความสมบูรณ์ของโครงงานก่อนการประเมินผล*
