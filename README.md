# 🃏 TCG Trading Platform — Flow Architecture & Discrepancies Tracking

> 📌 **ศูนย์กลางการติดตามและแก้ไขข้อขัดแย้งของ User Flow, สถาปัตยกรรมระบบ Escrow และการเชื่อมโยงกับ Figma UI**  
> เอกสารฉบับนี้จัดทำขึ้นเพื่อให้ทีมพัฒนา (DevOps, Backend, Frontend, QA) ใช้เป็นคู่มือมาตรฐานในการเปิด Issue, พัฒนางาน และตรวจสอบ (Review) เพื่อปิดงานบน GitHub

---

## 📑 สารบัญ (Table of Contents)
1. [เกี่ยวกับ Repository นี้ (About This Repository)](#1-เกี่ยวกับ-repository-นี้)
2. [โครงสร้างไฟล์และโฟลเดอร์ (Project Structure)](#2-โครงสร้างไฟล์และโฟลเดอร์)
3. [คู่มือการเปิด GitHub Issue (How to Create Issues)](#3-คู่มือการเปิด-github-issue)
4. [ขั้นตอนการทำงานตาม Issue (Development Workflow)](#4-ขั้นตอนการทำงานตาม-issue)
5. [ขั้นตอนการ Review และปิด Issue (Pull Request & Issue Closing Workflow)](#5-ขั้นตอนการ-review-และปิด-issue)

---

## 1. เกี่ยวกับ Repository นี้

Repository นี้ทำหน้าที่เป็น **Single Source of Truth** รวบรวมข้อบกพร่อง, ข้อขัดแย้งระหว่าง User Flow เดิมกับ Figma UI และกรณีขอบเขต (Edge Cases) ของระบบ **TCG Escrow Marketplace** เพื่อให้ทีมสามารถแปลงปัญหาเหล่านี้เป็น **GitHub Issues & Tasks** ที่มีแบบแผนชัดเจน

### 🎯 ประเด็นหลักที่ต้องแก้ไขในระบบ:
1. **Checkout Flow (US-04):** การเพิ่มขั้นตอนเลือกที่อยู่จัดส่ง และเลือกช่องทางชำระเงิน
2. **Order Fulfillment & Logistics (US-07):** การปรับปรุงระบบจัดส่งเป็น 2 จังหวะ (**Leg 1:** Seller ➔ Hub, **Leg 2:** Hub ➔ Buyer) พร้อมขั้นตอนตรวจสภาพการ์ด (**QC Pass / Fail**)
3. **Authentication (US-01):** เพิ่มฟิลด์ `Email` ในฟอร์มสมัครสมาชิก และเพิ่มระบบกู้รหัสผ่าน (Forgot Password)
4. **Seller Inventory (US-05):** การลงขายการ์ดผ่าน Master Catalog และการประเมินเกรดสภาพการ์ด (Condition Grading)
5. **Multi-Seller Marketplace (US-02, US-03):** การรองรับการ์ดใบเดียวกันจากหลายร้านค้า และระบบ Cart Drawer
6. **SLA Timers & Escrow Safety:** การตัดรอบออเดอร์อัตโนมัติ (48h Seller Timeout, 72h Buyer Auto-Release) และการจัดการ Partial QC Fail

---

## 2. โครงสร้างไฟล์และโฟลเดอร์

```
📂 Flow_devops/ExportBlock/
 ├── 📄 README.md                                   # คู่มือการทำงานบน GitHub ฉบับนี้
 ├── 📄 UI_FRAMES_CATALOG.md                        # รายการสกัด UI ทั้ง 75 หน้าจอจาก Figma
 ├── 📁 ความขัดแย้งกันของ flow/
 │    ├── 📄 FLOW_FIGMA_CONFLICT_REPORT.md          # รายงานสรุป 6 จุดขัดแย้งหลักระหว่าง Flow กับ Figma
 │    ├── 📊 Flow_Conflicts_Comprehensive_Swimlane.svg # แผนผังเปรียบเทียบ Before vs After (Vector SVG)
 │    └── 🌐 Flow_Discrepancies_and_Fixes_Overview.html # แดชบอร์ด Interactive HTML สำหรับดูเปรียบเทียบ
 ├── 📁 สิ่งที่ต้องแก้/
 │    └── 📄 System & Edge Case FlawsMD.md          # ข้อกำหนดทางธุรกิจ, SLA Timers, Partial QC, และ Edge Cases
 └── 📁 SVG/                                        # โฟลเดอร์เก็บไฟล์ Figma SVG แยกตามโมดูล
      ├── 📁 auth/                                  # 7 Frames (Login, Register, Reset Password)
      ├── 📁 Shop & Browse/                         # 11 Frames (Marketplace, Search, Card Detail)
      ├── 📁 Checkout Flow/                         # 7 Frames (Cart, Address, Payment, Timeline)
      ├── 📁 Buyer Account & Storefront/            # 6 Frames (Store Profile, Reviews)
      ├── 📁 profile/                               # 4 Frames (My Profile, Address Book, Security)
      ├── 📁 seller/                                # 20 Frames (Inventory, Leg 1 Shipping, Wallet)
      └── 📁 platform-admin/                        # 18 Frames (QC Hub Console, Leg 2, Dispute)
```

---

## 3. คู่มือการเปิด GitHub Issue

เมื่อต้องการนำปัญหาจากเอกสาร `FLOW_FIGMA_CONFLICT_REPORT.md` หรือ `System & Edge Case FlawsMD.md` ไปเปิดเป็น Issue บน GitHub ให้ปฏิบัติตามมาตรฐานดังนี้:

### 🏷️ 3.1 รูปแบบการตั้งชื่อ Issue (Title Convention)
```
[FLOW-FIX: <UserStory-ID>] <คำอธิบายสั้นๆ ของปัญหา>
[SYSTEM-EDGE: <หมวดหมู่>] <คำอธิบายสั้นๆ ของปัญหา>
```
*ตัวอย่าง:*
- `[FLOW-FIX: US-04] เพิ่มขั้นตอนเลือกที่อยู่จัดส่งและวิธีชำระเงินใน Checkout Flow`
- `[FLOW-FIX: US-07] ปรับปรุง Fulfillment เป็น 2-Leg Shipping และเพิ่มจุดตัดสิน QC Pass/Fail`
- `[SYSTEM-EDGE: Escrow] เพิ่มระบบ SLA Timer ยกเลิกออเดอร์อัตโนมัติเมื่อ Seller ไม่ส่งของภายใน 48 ชม.`

---

### 📝 3.2 Template ในการกรอกเนื้อหา Issue (Issue Description Template)

ก๊อปปี้เทมเพลตด้านล่างนี้ไปวางในช่อง Description ของ Issue:

```markdown
## 📌 ปัญหาที่พบ (Problem Description)
<!-- อธิบายว่า Flow เดิมมีปัญหาอะไร หรือขัดแย้งกับ Figma อย่างไร -->
ใน Flow เดิมข้ามขั้นตอนการเลือกที่อยู่จัดส่ง ทำให้ไม่มีข้อมูล Address ส่งไปยัง API สร้างคำสั่งซื้อ

## 🎯 สิ่งที่ต้องแก้ไข / ผลลัพธ์ที่ต้องการ (Expected Behavior)
<!-- ระบุขั้นตอนการทำงานที่ถูกต้องตาม Figma หรือ Business Rules -->
- [ ] เพิ่มหน้าจอ/ขั้นตอนเลือกที่อยู่จัดส่งจาก Address Book หรือเพิ่มที่อยู่ใหม่
- [ ] เพิ่มขั้นตอนเลือกรูปแบบขนส่งเข้า QC Hub
- [ ] อัปเดต Payload ใน API `/api/v1/orders/checkout` ให้รับ `address_id` และ `shipping_method`

## 🖼️ เอกสารและหน้าจออ้างอิง (References)
- **Figma Screens:** `ExportBlock/SVG/Checkout Flow/frame_2.svg` และ `frame_3.svg`
- **เอกสารวิเคราะห์:** `Flow_devops/ExportBlock/ความขัดแย้งกันของ flow/FLOW_FIGMA_CONFLICT_REPORT.md` (หัวข้อที่ 1)

## 🏷️ Acceptance Criteria (เกณฑ์การตรวจรับงาน)
1. มีการวาด Swimlane User Flow ใหม่ที่ระบุขั้นตอน Address Selection ชัดเจน
2. API Contract ระบุ Request/Response ครบถ้วน
3. มีการจัดการ Error Case กรณีผู้ใช้ยังไม่มีที่อยู่จัดส่ง
```

---

### 🏷️ 3.3 การใส่ Labels ให้กับ Issue
- `flow-discrepancy`: ข้อขัดแย้งระหว่าง Flow กับ Figma
- `edge-case`: ปัญหาขอบเขตระบบ / Concurrency / Timers
- `escrow-system`: ระบบสัญญาคนกลางและการเงิน
- `backend` / `frontend` / `devops`: แผนกที่รับผิดชอบ

---

## 4. ขั้นตอนการทำงานตาม Issue (Development Workflow)

เมื่อสมาชิกในทีมรับ Issue ไปทำ ให้ปฏิบัติตามลำดับขั้นตอนดังนี้:

### 🌿 4.1 การสร้าง Git Branch
ให้แตก Branch ออกมาจาก `main` หรือ `dev` โดยตั้งชื่อตามรูปแบบ:
```bash
# รูปแบบ: <type>/<issue-number>-<short-description>
git checkout -b fix/12-flow-us04-checkout-address
# หรือ
git checkout -b feature/15-escrow-sla-timers
```

### 💬 4.2 การเขียน Commit Message (Conventional Commits)
ต้องระบุหมายเลข Issue ใน Commit เพื่อให้ GitHub ลิงก์ไปยัง Issue อัตโนมัติ:
```bash
git commit -m "fix(flow): add address selection step in US-04 swimlane (Refs #12)"
git commit -m "feat(escrow): implement 48h seller timeout background cron (Refs #15)"
```

---

## 5. ขั้นตอนการ Review และปิด Issue (Pull Request & Closing Workflow)

### 🚀 5.1 การเปิด Pull Request (PR)
เมื่อทำงานเสร็จแล้ว ให้เปิด Pull Request เพื่อขอ Merge เข้า `dev` หรือ `main`

#### 📝 PR Title:
```
Fix(Flow): แก้ไขขั้นตอน Checkout และเพิ่ม Address Selection (#12)
```

#### 📋 PR Description Template:
```markdown
## 📌 สรุปการแก้ไข (Summary of Changes)
- อัปเดต Swimlane Diagram ของ US-04 ให้มีขั้นตอนเลือกที่อยู่จัดส่งและวิธีชำระเงิน
- เพิ่ม Error Handling กรณีไม่พบที่อยู่จัดส่งในระบบ
- ปรับปรุง Data Contract ให้ตรงกับ Figma `Checkout Flow/frame_2.svg`

## 🔗 ลิงก์ Issue ที่เกี่ยวข้อง (Fixes / Closes)
<!-- การใส่คำว่า Closes #... จะทำให้ GitHub ปิด Issue นั้นอัตโนมัติเมื่อ PR นี้ถูก Merge -->
Closes #12

## 🧪 การทดสอบและการตรวจสอบ (Verification)
- [x] ตรวจสอบความถูกต้องกับไฟล์ SVG ใน Figma เรียบร้อย
- [x] ตรวจสอบเส้นทาง Decision Paths และ Error Loops ครบถ้วน

## 📷 ภาพประกอบ / แผนผัง (Screenshots / Diagrams)
<!-- แนบรูปภาพ Diagram หรือโค้ดที่แก้ไข -->
```

---

### 🔍 5.2 ขั้นตอนสำหรับ Reviewer (ผู้ตรวจสอบงาน)

ผู้ทำหน้าที่ Reviewer จะต้องตรวจสอบตามเกณฑ์ 4 ข้อก่อนกด **Approve**:

1. **ความสอดคล้องกับ Figma (Figma Alignment):** Flow ที่แก้ใหม่ตรงกับหน้าจอใน `ExportBlock/SVG/` หรือไม่
2. **ความสมบูรณ์ของ Logic (Decision Completeness):** มีเส้นทาง Yes/No ครบทุกเงื่อนไข ไม่มีเส้นทางตัน (Dead End)
3. **การจัดการข้อผิดพลาด (Error & Edge Case Handling):** มีการจัดการ Timeout, ปัญหาสต็อกไม่พอ, หรือการคืนเงินครบถ้วน
4. **ความปลอดภัยของระบบ Escrow (Security & State Consistency):** สถานะออเดอร์สอดคล้องกับ State Machine ใน `System & Edge Case FlawsMD.md`

---

### ✅ 5.3 การปิด Issue (Closing Issue)
* เมื่อ Reviewer กด **Approve** และทำการ **Squash and Merge** PR เข้าสู่ Branch หลัก:
* GitHub จะทำการ **ปิด Issue (#12) ให้โดยอัตโนมัติ (Auto-Closed)**
* หากเป็นการแก้งานเอกสารโดยไม่ต้องเปิด PR สามารถกดปุ่ม **"Close Issue"** พร้อมระบุข้อความอธิบาย เช่น:
  > *"Closed via commit `a1b2c3d` — อัปเดต Swimlane Diagram ในโฟลเดอร์ ExportBlock เรียบร้อยแล้ว"*

---

🎉 **ทีมงานทุกคนสามารถเริ่มนำประเด็นในโฟลเดอร์นี้ไปเปิด Issue และดำเนินงานตามขั้นตอนข้างต้นได้ทันทีครับ!**
