# 📊 Mythix TCG Platform — Phase 2 Feature Implementation & Process Checklist
> **เอกสารตรวจสอบสถานะและกระบวนการพัฒนาฟีเจอร์ประจำ Phase 2 (Implementation & Verification Checklist)**  
> **อ้างอิงจาก:** `final_user_story_phase_2.md` (Final Scope Agreement)  
> **Repository:** `User-FlowANDFigma-Progress`  
> **Directory:** `/User Story & Flow/check-process-phase2.md`  
> **Target Branch:** `main`  
> **วันจัดทำ:** พฤศจิกายน 2026  

---

## 📑 สารบัญ (Table of Contents)
1. [บทสรุปภาพรวมสถานะการพัฒนา (Executive Summary)](#1-บทสรุปภาพรวมสถานะการพัฒนา-executive-summary)
2. [ตารางสรุปตามหมวดหมู่หลัก (Master Priority Matrix with Implementation Status)](#2-ตารางสรุปตามหมวดหมู่หลัก-master-priority-matrix-with-implementation-status)
3. [ตารางตรวจสอบรายฟีเจอร์อย่างละเอียด (Detailed User Stories Feature Checklist)](#3-ตารางตรวจสอบรายฟีเจอร์อย่างละเอียด-detailed-user-stories-feature-checklist)
   - [3.1 กลุ่ม Must-Have: แกนหลักระบบประมูล (US-13, US-18)](#31-กลุ่ม-must-have-แกนหลักระบบประมูล-us-13-us-18)
   - [3.2 กลุ่ม Recommended to Develop: ฟีเจอร์ยกระดับตามคำแนะนำอาจารย์ (US-20, US-24, US-27)](#32-กลุ่ม-recommended-to-develop-ฟีเจอร์ยกระดับตามคำแนะนำอาจารย์-us-20-us-24-us-27)
   - [3.3 กลุ่ม Good to Have: วงจรประมูลสดและการส่งมอบ (US-14, US-15, US-16, US-17)](#33-กลุ่ม-good-to-have-วงจรประมูลสดและการส่งมอบ-us-14-us-15-us-16-us-17)
   - [3.4 กลุ่ม Deferred / Out of Scope: ฟีเจอร์ที่ข้ามหรือมีของเดิมรองรับ (US-21, US-22, US-23, US-25, US-26, US-28)](#34-กลุ่ม-deferred--out-of-scope-ฟีเจอร์ที่ข้ามหรือมีของเดิมรองรับ-us-21-us-22-us-23-us-25-us-26-us-28)
4. [สรุปฟีเจอร์ที่ยังคงค้างและข้อเสนอแนะในการพัฒนาต่อ (Pending Items & Recommendations)](#4-สรุปฟีเจอร์ที่ยังคงค้างและข้อเสนอแนะในการพัฒนาต่อ-pending-items--recommendations)

---

## 1. บทสรุปภาพรวมสถานะการพัฒนา (Executive Summary)

จากการตรวจสอบซอร์สโค้ดล่าสุดบน Branch `main` ของทั้งฝั่ง **Backend (`tcg-store-backend`)** และ **Frontend (`tcg-store-frontend`)** เปรียบเทียบกับเอกสารข้อตกลงขอบเขตสุดท้าย `final_user_story_phase_2.md` พบสถานะความคืบหน้าของฟีเจอร์ในระบบดังนี้:

* **กลุ่ม Must-Have (US-13, US-18):** พัฒนาเสร็จสมบูรณ์ทั้ง Frontend และ Backend **100% (8/8 ข้อ)**  
  รองรับทั้งการสร้างและจัดการประมูล, Reserve Price, Buy-It-Now, แดชบอร์ดผู้ขาย, การคำนวณหักค่าธรรมเนียมแพลตฟอร์มอัตโนมัติ, สถิติกำไรผู้ขาย และพอร์ตการประมูลของผู้ซื้อ
* **กลุ่ม Recommended to Develop (US-20, US-24, US-27):** ดำเนินการแล้ว **60% (3/5 ข้อ)**  
  - `US-20` (Image Upload Policy Gate & Zoom Magnifier): **เสร็จสมบูรณ์ 100%**
  - `US-24` (Voucher / Promo Code at Checkout): **เสร็จสมบูรณ์ฝั่ง Buyer & Checkout** ขาดเฉพาะหน้า Admin Campaign Manager UI (`US-24-2`)
  - `US-27` (Weekly Stock & Profit Admin Report): **ยังไม่ได้พัฒนา (Pending Implementation)**
* **กลุ่ม Good-to-Have (US-14, US-15, US-16, US-17):** ดำเนินการแล้วส่วนใหญ่ **85% (17/20 ข้อ)**  
  ระบบห้องประมูลสด WebSocket, กลไกเคาะราคา Manual/Proxy Bids, การป้องกันบิดการ์ดตัวเอง, ระบบตัดสินผู้ชนะอัตโนมัติ และการโอนการ์ดเข้า Personal Binder ทำงานได้จริง
* **ฟีเจอร์โบนัสเพิ่มเติมที่พัฒนาเกิน Scope:**  
  - `US-28-2` (Multilingual Thai Card Search): รองรับการค้นหาการ์ดด้วยชื่อภาษาไทยผ่านฐานข้อมูลแคตตาล็อก `card_search_names` แล้ว

---

## 2. ตารางสรุปตามหมวดหมู่หลัก (Master Priority Matrix with Implementation Status)

> ตารางด้านล่างนำโครงสร้างดั้งเดิมจาก **หัวข้อที่ 2 ของ `final_user_story_phase_2.md`** มาเพิ่มคอลัมน์ **"มีในระบบหรือยัง"** และ **"รายละเอียดและหลักฐานในระบบ"** เพื่อให้เห็นความพร้อมในการประเมินผล:

| รหัสหมวด | ชื่อหมวดหมู่ (Module Title) | สถานะความสำคัญตามคำแนะนำอาจารย์ | จำนวน US ย่อย | เป้าหมายการส่งมอบ | มีในระบบหรือยัง (Status in System) | รายละเอียดและหลักฐานการพัฒนาในระบบ (Implementation Details & Evidence) |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| **US-13** | **Auction Listing & Setup**<br>*(สร้าง/ตั้งค่าประมูล, Reserve, Buy-It-Now)* | ⭐ **MUST HAVE** | 5 ข้อ | **Sprint 1 (Priority 1)** | 🟢 **มีครบแล้ว (100%)** | • `POST /api/seller/auctions`<br>• `AuctionWizardPage.tsx`<br>• `AuctionDetailsPage.tsx`<br>• `MyAuctionsPage.tsx` |
| **US-18** | **Auction Analytics & Financials**<br>*(คำนวณค่าธรรมเนียม, สถิติกำไรผู้ขาย/ผู้ซื้อ)* | ⭐ **MUST HAVE** | 3 ข้อ | **Sprint 1 (Priority 1)** | 🟢 **มีครบแล้ว (100%)** | • `AuctionAnalyticsPage.tsx`<br>• `AuctionPortfolioPage.tsx`<br>• `AuctionCommissionPage.tsx`<br>• `AuctionCommissionService.java` |
| **US-20** | **Card Image Upload Policy & Criteria Gate**<br>*(เกณฑ์บังคับรูปจริง vs ตัวเลือกเสริม + แว่นขยาย)* | 🚀 **RECOMMENDED** | 2 ข้อ | **Sprint 1 (Priority 1)** | 🟢 **มีครบแล้ว (100%)** | • `imagePolicy.ts` & `ListingPhotoEditor.tsx`<br>• `ListingImagePolicy.java`<br>• `CardPhotoMagnifierViewer.tsx` (ซูม 2.5x) |
| **US-24** | **Promotions & Discount Codes Engine**<br>*(ระบบคูปองและโค้ดส่วนลด Checkout)* | 🚀 **RECOMMENDED** | 2 ข้อ | **Sprint 2 (Priority 1)** | 🟡 **มีบางส่วน (70%)** | • มี Voucher Center, Wallet, Validation & Checkout (`/api/vouchers/validate`, `CheckoutVoucherModal.tsx`)<br>• *ขาดหน้า Admin Promo Campaign UI* |
| **US-27** | **Weekly Stock & Profit Admin Report**<br>*(รายงานสินค้าคงคลังและผลกำไรประจำสัปดาห์)* | 🚀 **RECOMMENDED** | 1 ข้อ | **Sprint 2 (Priority 1)** | 🔴 **ยังไม่มี (0%)** | • ปัจจุบัน Admin มี Dashboard รวม (`AdminDashboardPage.tsx`)<br>• *ยังไม่มี Scheduled Weekly Cron และรายงานสรุปค้างสต๊อก 60 วัน* |
| **US-14** | **Auction Discovery & Live Arena**<br>*(หน้ารวมประมูล, WebSocket Room, Watchlist)* | 💡 **GOOD TO HAVE** | 5 ข้อ | **Sprint 2 (Priority 2)** | 🟢 **มีครบแล้ว (100%)** | • `BuyerAuctionsPage.tsx`<br>• `BuyerAuctionDetailPage.tsx` (WebSocket `/auctions/{id}/live`)<br>• Masked Bid History (`p***a`)<br>• Watchlist Notification |
| **US-15** | **Bidding Engine & Proxy Bids**<br>*(เคาะสด, บิดอัตโนมัติ Max Bid, แจ้งเตือน Outbid)* | 💡 **GOOD TO HAVE** | 5 ข้อ | **Sprint 2 (Priority 2)** | 🟢 **มีครบแล้ว (100%)** | • `placeManualBid` & `placeProxyBid` (`AuctionBidService.java`)<br>• Dynamic Increment Ladder<br>• Outbid Notification |
| **US-16** | **Fair-Play & Anti-Fraud Controls**<br>*(Dynamic Anti-Sniping 3 นาที, ป้องกันปั่นราคา)* | 💡 **GOOD TO HAVE** | 4 ข้อ | **Sprint 2 (Priority 2)** | 🟡 **มีบางส่วน (75%)** | • มี Anti-Shill ป้องกันผู้ขายเคาะการ์ดตัวเอง<br>• นโยบายห้ามยกเลิกบิด<br>• *Anti-Sniping ขยายเวลาอัตโนมัติรองรับใน State แต่ยังไม่เปิด Trigger* |
| **US-17** | **Resolution, Settlement & Ownership**<br>*(ตัดสินผู้ชนะ, ชำระเงิน 48 ชม., โอนเข้า Binder)* | 💡 **GOOD TO HAVE** | 6 ข้อ | **Sprint 2 (Priority 2)** | 🟢 **มีเกือบครบ (90%)** | • `AuctionSettlementService.java`<br>• Scheduled Auto-Close Daemon<br>• โอนการ์ดเข้า Personal Binder อัตโนมัติ<br>• Second-Chance Offer รองรับในระบบ |
| `US-21` | *Middleman Escrow Fee & Monthly Dashboard* | ⏸️ *DEFERRED (ข้ามไปก่อน)* | — | รวมอยู่ใน US-18 แล้ว | 🟢 **รวมใน US-18 แล้ว** | คิดค่าธรรมเนียมในกระบวนการ Settlement และรายงานใน `AuctionCommissionPage.tsx` |
| `US-22` | *Collection Privacy & Showcase Viewer* | ⏸️ *DEFERRED (ข้ามไปก่อน)* | — | Phase 1 มี US-10-6 แล้ว | 🟢 **มีใน Phase 1 แล้ว** | `PublicCollectionsExplorePage.tsx` & `PublicCollectionPage.tsx` (`/collections/:userId`) |
| `US-23` | *Product Categories & Advanced Filtering* | ⏸️ *DEFERRED (ข้ามไปก่อน)* | — | ใช้ตัวกรองเดิม US-02-1 | 🟢 **มีใน Phase 1 แล้ว** | Multi-Filter กรอง Set, Game, Rarity, Condition ใน `CardDiscoveryPage.tsx` |
| `US-25` | *Order History & Reorder, PDF Summary Export* | ⏸️ *DEFERRED (ข้ามไปก่อน)* | — | ยกยอดหลังส่งมอบหลัก | 🟡 **มีเฉพาะประวัติออเดอร์** | มีดูประวัติคำสั่งซื้อ (`/profile/orders`) แต่ปุ่ม Reorder 1-Click และพิมพ์ PDF ยกยอด |
| `US-26` | *Out of Stock Alert & Smart Restock Prediction* | ⏸️ *DEFERRED (ข้ามไปก่อน)* | — | ซับซ้อนเกินกรอบเวลา | ⏸️ **ยกยอดตาม Scope** | ข้ามตามคำแนะนำอาจารย์ |
| `US-28` | *Tolerant Search (Typo) & Multilingual Search* | ⏸️ *DEFERRED (ข้ามไปก่อน)* | — | โบนัสเสริม ยกยอดไว้ก่อน | 🟢 **พัฒนาเพิ่มแล้ว (TH Search)** | ตาราง `card_search_names` (Migration V19) + คำค้นหาภาษาไทยกว่า 2,000 รายการ รองรับการค้นหาการ์ดภาษาไทย |

---

## 3. ตารางตรวจสอบรายฟีเจอร์อย่างละเอียด (Detailed User Stories Feature Checklist)

### 3.1 กลุ่ม Must-Have: แกนหลักระบบประมูล (US-13, US-18)

| รหัส US | ชื่อฟีเจอร์ (Feature Title) | สถานะในระบบ | รายละเอียดการ Implement ใน Frontend / Backend |
| :--- | :--- | :---: | :--- |
| **US-13-1** | Create Card Auction Listing from Catalog/Collection | ✅ **มีแล้ว** | • **Frontend:** `AuctionWizardPage.tsx`, `AuctionWizardSections.tsx`, `CatalogCardPicker.tsx`<br>• **Backend:** `SellerAuctionController.java`, `AuctionService.java` (`POST /api/seller/auctions`)<br>• ตรวจสอบ `seller_status = 'APPROVED'`, ดึงข้อมูลต้นแบบ, ระบุสภาพการ์ด และล็อกสต๊อก `auction_locked` |
| **US-13-2** | Configure Hidden Reserve Price & Buy-It-Now Option | ✅ **มีแล้ว** | • **Frontend:** ฟิลด์ตั้ง Reserve Price และ Buy-It-Now ใน `AuctionWizardSections.tsx`<br>• **Backend:** `Auction.java` ฟิลด์ `reservePrice`, `buyItNowPrice`, `isReserveMet` ซ่อนตัวเลขจากผู้ซื้อ |
| **US-13-3** | Schedule Auction Start Time & Duration | ✅ **มีแล้ว** | • **Frontend:** ตัวเลือกเปิดทันที หรือกำหนดเวลาล่วงหน้า >= 15 นาที, เลือกระยะเวลา (24h, 3d, 5d, 7d)<br>• **Backend:** `AuctionService.java` (`POST /api/seller/auctions/schedule`), คำนวณ `end_time` เป็น UTC |
| **US-13-4** | Seller Auction Dashboard & Draft Management | ✅ **มีแล้ว** | • **Frontend:** `MyAuctionsPage.tsx`, `AuctionDetailsPage.tsx` มีแท็บสถานะ Drafts, Scheduled, Active, Ended, Completed<br>• **Backend:** `GET /api/seller/auctions`, รองรับการแก้ไขและลบ Draft ก่อนเปิดจริง |
| **US-13-5** | Seller Auction Early Cancellation Rules | ✅ **มีแล้ว** | • **Frontend:** `AuctionCancellation.tsx`, Modal แนบหลักฐานยกเลิกประมูล<br>• **Backend:** `AuctionCancellationService.java` (ยกเลิกได้ทันทีถ้า 0 Bids, หากมีผู้เคาะแล้วต้องส่งคำขอพร้อมหลักฐานให้แอดมิน) |
| **US-18-1** | Seller Auction Revenue, Cost & Net Margin Analytics | ✅ **มีแล้ว** | • **Frontend:** `AuctionAnalyticsPage.tsx` แสดง Gross Auction Volume, Total Cost, Net Profit, Margin %, กราฟ Start vs Realized Price<br>• **Backend:** `AuctionAnalyticsService.java` (`GET /api/seller/auctions/analytics`) |
| **US-18-2** | Platform Auction Fee & Commission Auto-Deduction | ✅ **มีแล้ว** | • **Frontend:** `AuctionCommissionPage.tsx` ตั้งค่านโยบายค่าธรรมเนียม, `AuctionDetailsPage.tsx` แสดง Settlement Summary<br>• **Backend:** `AuctionCommissionService.java`, `AdminAuctionCommissionController.java`, หักเงินค่าธรรมเนียมอัตโนมัติ |
| **US-18-3** | Buyer Personal Auction Portfolio & Win-Rate Stats | ✅ **มีแล้ว** | • **Frontend:** `AuctionPortfolioPage.tsx` แสดง Bids Placed, Auctions Won, Win Rate %, Total Invested Volume<br>• **Backend:** `AuctionAnalyticsService.java` (`GET /api/user/auction-portfolio`) |

---

### 3.2 กลุ่ม Recommended to Develop: ฟีเจอร์ยกระดับตามคำแนะนำอาจารย์ (US-20, US-24, US-27)

| รหัส US | ชื่อฟีเจอร์ (Feature Title) | สถานะในระบบ | รายละเอียดการ Implement ใน Frontend / Backend |
| :--- | :--- | :---: | :--- |
| **US-20-1** | Mandatory vs. Optional Real Card Image Upload Gate | ✅ **มีแล้ว** | • **Frontend:** `imagePolicy.ts`, `useListingImageRules.ts`, `ListingPhotoEditor.tsx` ประเมินเกณฑ์แบบเรียลไทม์ (ราคา >= ฿500, การ์ดเกรด, สภาพตำหนิ, Rarity พิเศษ บังคับแนบรูปจริง >= 2 รูป ไม่อนุญาตให้กด Submit หากไม่ครบ)<br>• **Backend:** `ListingImagePolicy.java`, `SellerProductController.java` (`POST /api/seller/products/validate-listing-rules`) |
| **US-20-2** | High-Resolution Card Gallery with Zoom Magnifier | ✅ **มีแล้ว** | • **Frontend:** `CardPhotoMagnifierViewer.tsx`, `CardDetailPage.tsx` มีแท็บสลับ "Official Art" กับ "Actual Photos" พร้อมเอฟเฟกต์ Hover Zoom Magnifier ขยาย 2.5x ส่องตำหนิการ์ด |
| **US-24-1** | Promo Code / Voucher Application & Validation at Checkout | ✅ **มีแล้ว** | • **Frontend:** `CheckoutVoucherModal.tsx`, `VoucherTicket.tsx`, `VoucherCenterPage.tsx`, `MyVouchersPage.tsx`<br>• **Backend:** `VoucherController.java` (`POST /api/vouchers/validate`, `/claim`, `/my-vouchers`), `BuyerOrderService.java` หักส่วนลดจากยอด Subtotal และบันทึกประวัติ Voucher |
| **US-24-2** | Admin Promo Campaign Management | 🟡 **มีบางส่วน** | • **Backend:** ฐานข้อมูลมีตาราง `vouchers` (Flyway V13) และ Initial Seeds (WELCOME10, MYTHIX50, FLASH100, POKEMON15)<br>• *สิ่งที่ยังขาด:* ยังไม่มีหน้า UI สำหรับแอดมินสร้าง/แก้ไขโค้ดใหม่ (`/admin/promotions`) และ Controller เฉพาะ |
| **US-27-1** | Automated Weekly Stock & Profit Platform Governance Report | 🔴 **ยังไม่มี** | • **สถานะปัจจุบัน:** แอดมินมี `AdminDashboardPage.tsx` แสดงยอดรวมการ์ดและออเดอร์ทั่วไป<br>• *สิ่งที่ยังขาด:* Scheduled Cron Job สรุปยอดทุกคืนวันอาทิตย์ (23:59 UTC), การวิเคราะห์สินค้าค้างสต๊อกเกิน 60 วัน (Stagnant Inventory), และปุ่มดาวน์โหลดรายงาน CSV/PDF |

---

### 3.3 กลุ่ม Good to Have: วงจรประมูลสดและการส่งมอบ (US-14, US-15, US-16, US-17)

| รหัส US | ชื่อฟีเจอร์ (Feature Title) | สถานะในระบบ | รายละเอียดการ Implement ใน Frontend / Backend |
| :--- | :--- | :---: | :--- |
| **US-14-1** | Browse Auctions Hub with Multi-Filter & Ending Soon | ✅ **มีแล้ว** | • `BuyerAuctionsPage.tsx` มีแท็บ Ending Soon, Hot Bids, Buy-It-Now, No Reserve, กรอง Condition และสถิติ |
| **US-14-2** | Live Auction Room with Real-Time WebSocket Ticker | ✅ **มีแล้ว** | • `BuyerAuctionDetailPage.tsx` เชื่อมต่อ WebSocket `/auctions/{id}/live`, แสดงเวลานับถอยหลังซิงก์ Server Time |
| **US-14-3** | Transparent Public Bid History (Masked Identities) | ✅ **มีแล้ว** | • `AuctionBidService.java` ฟังก์ชัน `maskIdentity` แสดงชื่อ `p***a` หรือ `You` บนกระดานประมูล |
| **US-14-4** | Auction Watchlist & Ending Countdown Alert | ✅ **มีแล้ว** | • `AuctionWatchlistService.java`, ปุ่มกดบันทึกการ์ดลง Watchlist และระบบแจ้งเตือนก่อนปิดประมูล |
| **US-14-5** | High-Value & Graded Card Verification Badge Display | ✅ **มีแล้ว** | • ป้ายแสดงข้อมูลสถาบันเกรด (PSA, BGS, CGC) พร้อมปุ่มคลิกตรวจสอบเลขใบรับรอง (`buildCertificationUrl`) |
| **US-15-1** | Manual Direct Bidding with Real-Time Validation | ✅ **มีแล้ว** | • `placeManualBid` ใน `AuctionBidService.java`, คำนวณขั้นบันไดราคาขั้นต่ำ (Dynamic Increment Ladder) |
| **US-15-2** | Automated Proxy Bidding Engine (Max Bid) | ✅ **มีแล้ว** | • `placeProxyBid` ใน `AuctionBidService.java`, ระบบเคาะสู้ให้อัตโนมัติทีละสเต็ปไม่เกินเพดาน Max Bid |
| **US-15-3** | Instant Buy-It-Now Purchase Flow | ✅ **มีแล้ว** | • `executeBuyout` ใน `AuctionBidService.java`, สั่งซื้อและตัดจบห้องประมูลทันที (`BUYOUT_COMPLETED`) |
| **US-15-4** | Instant Outbid In-App & Push Notification | ✅ **มีแล้ว** | • `notifyOutbid` ใน `AuctionBidService.java`, ส่ง Notification แจ้งเตือนผู้ที่ถูกเคาะราคาแซงทันที |
| **US-15-5** | Bid Confirmation Modal & Increment Ladder Helper | ✅ **มีแล้ว** | • Modal ยืนยันการเคาะราคาใน `BuyerAuctionDetailPage.tsx` พร้อมปุ่มลัดคำนวณขั้นต่ำ |
| **US-16-1** | Anti-Shill Bidding & Self-Bid Restrictions | ✅ **มีแล้ว** | • `AuctionBidService.java` ตรวจสอบและไม่อนุญาตให้ผู้ขายเคาะการ์ดของตนเอง (`You cannot bid on your own auction`) |
| **US-16-2** | Dynamic Anti-Sniping Engine (3-Minute Soft Close) | 🟡 **มีบางส่วน** | • สเตตแมชชีนมีสถานะ `EXTENDED` แต่ยังไม่ได้ผูก Logic ขยายเวลา +3 นาทีอัตโนมัติในคำสั่ง `placeManualBid` |
| **US-16-3** | Bidder Eligibility & Deposit Credit Hold | 🟡 **มีบางส่วน** | • ตรวจสอบสิทธิ์บัญชีผู้ใช้และสถานะการยืนยันตัวตน แต่ยังไม่ได้ล็อกเงินมัดจำเครดิต |
| **US-16-4** | Strict Bid Retraction Policy Enforcement | ✅ **มีแล้ว** | • ไม่มีฟังก์ชันให้ผู้ซื้อกดยกเลิกการเคาะราคาด้วยตนเองตามนโยบายคุ้มครองความยุติธรรม |
| **US-17-1** | Automated Closing & Winner Determination Service | ✅ **มีแล้ว** | • `AuctionLifecycle.java` และ `AuctionSettlementService.java` ตัดสินผู้ชนะเมื่อหมดเวลาและสร้างออเดอร์ |
| **US-17-2** | Settlement for Reserve-Not-Met & Unsold Auctions | ✅ **มีแล้ว** | • ปิดสถานะ `RESERVE_NOT_MET` / `UNSOLD_NO_BIDS` และปลดล็อกการ์ดคืนสต๊อกผู้ขายโดยอัตโนมัติ |
| **US-17-3** | Winner Checkout & Payment Gateway Window | ✅ **มีแล้ว** | • สร้าง Order คำสั่งซื้อรองรับสถานะการชำระเงินของระบบ Marketplace เดิม |
| **US-17-4** | Automated Card Ownership Transfer into Personal Binder | ✅ **มีแล้ว** | • `transferAuctionCardToPersonalBinder` ใน `AuctionSettlementService.java` โอนการ์ดเข้าอัลบั้มสะสมทันทีเมื่อส่งมอบสำเร็จ |
| **US-17-5** | Second-Chance Offer for Runner-up Bidders | ✅ **มีแล้ว** | • `sendSecondChanceOffer`, `respondSecondChanceOffer`, ตาราง `auction_second_chance_offers` |
| **US-17-6** | Defaulting Bidder Penalty & Cancelled Order Sync | ✅ **มีแล้ว** | • `closeCancelledOrder` ซิงก์คำสั่งซื้อที่ยกเลิก และคืนสิทธิ์การขายให้แก่ผู้ขาย |

---

### 3.4 กลุ่ม Deferred / Out of Scope: ฟีเจอร์ที่ข้ามหรือมีของเดิมรองรับ (US-21, US-22, US-23, US-25, US-26, US-28)

| รหัส US | ชื่อฟีเจอร์ (Feature Title) | สถานะ | หมายเหตุและผลการตรวจเช็กในโค้ดเบสปัจจุบัน |
| :---: | :--- | :---: | :--- |
| **US-21** | Middleman Escrow Fee & Monthly Dashboard | 🟢 **รวมใน US-18** | ระบบคิดค่าธรรมเนียมตัวกลางถูกนำไปผนวกอยู่ในระบบประมูล `US-18-2` เรียบร้อยแล้ว |
| **US-22** | Collection Privacy & Showcase Viewer | 🟢 **มีใน Phase 1** | มี Route `/collections/:userId` และหน้ารวม Showcase ตาม `US-10-6` รองรับอยู่แล้ว |
| **US-23** | Product Categories & Advanced Filtering | 🟢 **มีใน Phase 1** | ตัวกรองหลายมิติเดิมใน Phase 1 (`US-02-1`) กรองตามชุดการ์ด ความหายาก และสภาพการ์ดได้อย่างครบถ้วน |
| **US-25** | Order History & Reorder, PDF Summary Export | 🟡 **มีเฉพาะประวัติ** | มีหน้าประวัติคำสั่งซื้อ (`US-09-1`) แต่ส่วนการกดสั่งซ้ำ (1-Click Reorder) และส่งออก PDF ยกยอดไว้ก่อน |
| **US-26** | Out of Stock Alert & Smart Restock Prediction | ⏸️ **ยกยอด** | ซับซ้อนเกินกรอบเวลา ตัดออกจาก Scope การประเมินตามคำแนะนำอาจารย์ |
| **US-28** | Tolerant Search (Typo) & Multilingual Search | 🟢 **พัฒนาเพิ่ม (TH)** | มีการสร้างตาราง `card_search_names` (Flyway V19) นำเข้าคำศัพท์ภาษาไทยกว่า 2,000 รายการ รองรับการค้นหาการ์ดภาษาไทยข้ามภาษา |

---

## 4. สรุปฟีเจอร์ที่ยังคงค้างและข้อเสนอแนะในการพัฒนาต่อ (Pending Items & Recommendations)

เพื่อให้ระบบมีความสมบูรณ์ 100% ตามขอบเขตของ **Must-Have** และ **Recommended to Develop** ของ Phase 2 รายการงานที่ควรดำเนินการต่อใน Sprint ถัดไป มีดังนี้:

1. **US-27-1 (Weekly Stock & Profit Admin Report):**  
   - สร้าง Backend Service พร้อม Spring `@Scheduled(cron = "0 59 23 * * SUN")` เพื่อประมวลผลข้อมูลสต๊อก, มูลค่ารวม, และสินค้าค้างสต๊อกเกิน 60 วัน
   - เพิ่มหน้า UI ในเมนู Admin Console สำหรับเปิดดูและดาวน์โหลดรายงานสรุป
2. **US-24-2 (Admin Promo Campaign Management):**  
   - พัฒนาหน้า Admin UI (`/admin/promotions`) เพื่อให้แอดมินสามารถกดสร้างโค้ดส่วนลดใหม่ กำหนดวันหมดอายุ โควตาสิทธิ์การใช้งาน และเปิด/ปิดแคมเปญได้สะดวกผ่านหน้าจอ
3. **US-16-2 (Dynamic Anti-Sniping Trigger):**  
   - เสริม Logic ใน `placeManualBid` / `placeProxyBid` ของ `AuctionBidService.java` ให้ขยายเวลา `end_time` ออกไป +3 นาทีโดยอัตโนมัติ เมื่อมีผู้เคาะราคาในช่วง 3 นาทีสุดท้ายก่อนปิดประมูล

---
> 📌 *เอกสารฉบับนี้ถูกจัดทำขึ้นเพื่อใช้เป็น Checklist อย่างเป็นทางการสำหรับการติดตามผลงานและการนำเสนอความก้าวหน้าโครงงาน (Phase 2 Progress Defense)*
