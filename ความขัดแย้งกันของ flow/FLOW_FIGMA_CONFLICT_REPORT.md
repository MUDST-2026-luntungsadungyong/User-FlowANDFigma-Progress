# 📋 รวมร่าง GitHub Issues สำหรับแก้ไข "ความขัดแย้งกันของ Flow"
> **วิธีใช้งาน:** คุณสามารถ Copy เนื้อหาในแต่ละ Issue ด้านล่างนี้ (ตั้งแต่ Title, Labels จนถึง Acceptance Criteria) ไปกดสร้างใน **GitHub > Issues > New Issue** ได้ทันทีครับ!

---

## 📑 สารบัญ Issues ทั้งหมด (Issue Index)

| Issue # | หัวข้อ Issue (Title) | โมดูลที่เกี่ยวข้อง | Priority |
| :---: | :--- | :---: | :---: |
| **[Issue 1](#issue-1-flow-fix-us-04-เพิ่มขั้นตอนเลือกที่อยู่จัดส่งและวิธีชำระเงินใน-checkout-flow)** | `[FLOW-FIX: US-04] เพิ่มขั้นตอนเลือกที่อยู่จัดส่งและวิธีชำระเงินใน Checkout Flow` | Checkout Flow | 🔴 High |
| **[Issue 2](#issue-2-flow-fix-us-07-ปรับปรุงระบบ-fulfillment-เป็น-2-leg-logistics-และเพิ่มจุดตัดสิน-qc-passfail)** | `[FLOW-FIX: US-07] ปรับปรุงระบบ Fulfillment เป็น 2-Leg Logistics และเพิ่มจุดตัดสิน QC Pass/Fail` | Seller & Admin | 🔴 High |
| **[Issue 3](#issue-3-flow-fix-us-01-เพิ่มฟิลด์-email-ใน-sign-up-และสร้าง-sub-flow-กู้คืนรหัสผ่าน-forgot-password)** | `[FLOW-FIX: US-01] เพิ่มฟิลด์ Email ใน Sign Up และสร้าง Sub-flow กู้คืนรหัสผ่าน (Forgot Password)` | Auth | 🟡 Medium |
| **[Issue 4](#issue-4-flow-fix-us-05-1-ปรับระบบลงขายการ์ดให้ค้นหาจาก-master-catalog-และระบุ-condition-grading)** | `[FLOW-FIX: US-05-1] ปรับระบบลงขายการ์ดให้ค้นหาจาก Master Catalog และระบุ Condition Grading` | Seller Inventory | 🟡 Medium |
| **[Issue 5](#issue-5-flow-fix-us-0203-ปรับปรุงระบบค้นหาและตะกร้าให้รองรับ-multi-seller-และ-cart-drawer)** | `[FLOW-FIX: US-02/03] ปรับปรุงระบบค้นหาและตะกร้าให้รองรับ Multi-Seller และ Cart Drawer` | Shop & Cart | 🟡 Medium |
| **[Issue 6](#issue-6-flow-new-selleradmin-เพิ่ม-flow-ฟีเจอร์ที่ตกหล่น-wallet-bulk-csv-และ-dispute)** | `[FLOW-NEW: Seller/Admin] เพิ่ม Flow ฟีเจอร์ที่ตกหล่น (Wallet, Bulk CSV, และ Dispute)` | Seller & Admin | 🟢 Low/Feature |

---

---

### Issue 1: `[FLOW-FIX: US-04] เพิ่มขั้นตอนเลือกที่อยู่จัดส่งและวิธีชำระเงินใน Checkout Flow`

**Title:**
```
[FLOW-FIX: US-04] เพิ่มขั้นตอนเลือกที่อยู่จัดส่งและวิธีชำระเงินใน Checkout Flow ให้ตรงกับ Figma
```

**Labels:** `flow-discrepancy`, `checkout`, `escrow`, `priority-high`

**Description (Copy ข้อความด้านล่างนี้):**
```markdown
## 📌 ปัญหาที่พบ (Problem Description)
ใน User Flow เดิมของ US-04 (หน้า 13-14) เมื่อผู้ใช้กด "Checkout จากตะกร้า" ระบบจะกระโดดข้ามไปหน้าสรุปและสร้าง QR Code ทันที โดย**ไม่มีขั้นตอนให้เลือกที่อยู่จัดส่ง และไม่มีให้เลือกช่องทางชำระเงิน** ทำให้ขาดข้อมูลสำคัญในการสร้าง Order Payload

## 🎯 สิ่งที่ต้องแก้ไข / ผลลัพธ์ที่ต้องการ (Expected Behavior)
ปรับปรุง Swimlane User Flow ของ US-04 ให้มีขั้นตอนการทำงานครบ 4 ขั้นตาม Figma:
1. **Cart Review:** ตรวจสอบรายการการ์ดและยอดรวมในตะกร้า (`Checkout Flow/frame_1.svg`)
2. **Select Shipping Address:** เลือกที่อยู่จัดส่งจาก Address Book หรือเพิ่มที่อยู่ใหม่ (`Checkout Flow/frame_2.svg`)
3. **Select Delivery Option:** เลือกรูปแบบการจัดส่งเข้า QC Hub (`Checkout Flow/frame_3.svg`)
4. **Select Payment Method:** เลือกช่องทางชำระเงิน (PromptPay QR / บัตรเครดิต) พร้อมป้าย Escrow Protection (`Checkout Flow/frame_4.svg`)
5. **Payment & Order Confirmed:** แสดง Dynamic QR Code และล็อกเงินใน Escrow Vault (`Checkout Flow/frame_5, 6.svg`)

## 🖼️ หน้าจออ้างอิงจาก Figma
- `ExportBlock/SVG/Checkout Flow/frame_1.svg` ถึง `frame_6.svg`
- รายงานอ้างอิง: `Flow_devops/ExportBlock/ความขัดแย้งกันของ flow/FLOW_FIGMA_CONFLICT_REPORT.md` (ประเด็นที่ 1)

## 🛠️ ผลกระทบเชิงเทคนิค (Technical & API Impact)
- **API Endpoint:** `POST /api/v1/orders/checkout` ต้องรับ Payload:
  ```json
  {
    "cart_items": [{"listing_id": "uuid", "quantity": 1}],
    "shipping_address_id": "uuid",
    "shipping_method_id": "standard_hub",
    "payment_method": "PROMPTPAY"
  }
  ```

## 🏷️ Acceptance Criteria
- [ ] มีการอัปเดต Swimlane Diagram ของ US-04 ในโฟลเดอร์ `ExportBlock`
- [ ] มีขั้นตอนตรวจสอบกรณีที่ผู้ใช้ยังไม่มีที่อยู่จัดส่ง (Redirect ไปหน้าเพิ่มที่อยู่)
- [ ] มี Error Handling กรณี Payment Gateway หมดเวลา (Payment Timeout 10 นาที)
```

---

---

### Issue 2: `[FLOW-FIX: US-07] ปรับปรุงระบบ Fulfillment เป็น 2-Leg Logistics และเพิ่มจุดตัดสิน QC Pass/Fail`

**Title:**
```
[FLOW-FIX: US-07] ปรับปรุงระบบ Fulfillment เป็น 2-Leg Logistics และเพิ่มจุดตัดสิน QC Pass/Fail
```

**Labels:** `flow-discrepancy`, `logistics`, `qc-hub`, `escrow`, `priority-high`

**Description (Copy ข้อความด้านล่างนี้):**
```markdown
## 📌 ปัญหาที่พบ (Problem Description)
ใน User Flow เดิมของ US-07 (หน้า 20) ระบุว่าแอดมินกด "จัดส่ง" ➔ กรอกเลขพัสดุ ➔ สถานะเป็น "Fulfilled" จบในขั้นตอนเดียว ซึ่งขัดแย้งกับโมเดลธุรกิจของแพลตฟอร์มที่เป็น **2-Leg Shipping ผ่านศูนย์ตรวจสภาพการ์ด (QC Hub)** และขาดจุดตัดสินใจเรื่องการตรวจสภาพการ์ด

## 🎯 สิ่งที่ต้องแก้ไข / ผลลัพธ์ที่ต้องการ (Expected Behavior)
แยก Swimlane ของ US-07 ออกเป็น 2 บทบาทและ 2 จังหวะการจัดส่งที่ชัดเจน:
1. **Leg 1 (Seller Fulfillment):**
   - ร้านค้าดูออเดอร์ ➔ พิมพ์ใบปะหน้าส่งเข้า Hub (`seller/frame_6.svg`) ➔ กรอกเลข Tracking Leg 1 (`seller/frame_7.svg`)
2. **QC Hub Inspection & Decision (จุดตัดสินใจสำคัญ):**
   - เจ้าหน้าที่ Hub สแกนรับพัสดุ ➔ เปิดกล้องบันทึก Unboxing & ถ่ายรูป Macro 4K
   - **Decision: QC Pass or Fail? (`platform-admin/frame_4.svg`)**
     - **[ QC Pass ]:** ออกใบปะหน้า Leg 2 ➔ จัดส่งให้ผู้ซื้อ (`platform-admin/frame_5.svg`) ➔ ผู้ซื้อตรวจรับ ➔ ปล่อยเงิน Escrow ให้ผู้ขาย
     - **[ QC Mismatch / Fail ]:** ส่งรายงานตำหนิให้ผู้ซื้อเลือกว่าจะรับหรือ Refund ➔ ถ้ายกเลิก คืนเงินผู้ซื้อ 100% + ส่งการ์ดคืนร้านค้า

## 🖼️ หน้าจออ้างอิงจาก Figma
- `ExportBlock/SVG/seller/frame_5, 6, 7.svg` (ฝั่ง Seller Leg 1)
- `ExportBlock/SVG/platform-admin/frame_3, 4, 5.svg` (ฝั่ง QC Hub Leg 2 & Pass/Fail Modal)

## 🛠️ ผลกระทบเชิงเทคนิค (Technical & API Impact)
- **Order State Machine:** เพิ่มสถานะ `SELLER_SHIPPED_LEG1` ➔ `ARRIVED_AT_HUB` ➔ `QC_IN_PROGRESS` ➔ `QC_PASSED` / `QC_FAILED` ➔ `HUB_DISPATCHED_LEG2` ➔ `DELIVERED`

## 🏷️ Acceptance Criteria
- [ ] Swimlane Diagram แสดง 2 เส้นทางชัดเจนระหว่าง Seller Lane และ QC Hub Admin Lane
- [ ] มี Decision Diamond สำหรับกรณี QC Pass และ QC Fail ชัดเจน
- [ ] มีเส้นทาง Rollback / Refund เงิน Escrow เมื่อการ์ดไม่ผ่าน QC
```

---

---

### Issue 3: `[FLOW-FIX: US-01] เพิ่มฟิลด์ Email ใน Sign Up และสร้าง Sub-flow กู้คืนรหัสผ่าน (Forgot Password)`

**Title:**
```
[FLOW-FIX: US-01] เพิ่มฟิลด์ Email ใน Sign Up และสร้าง Sub-flow กู้คืนรหัสผ่าน (Forgot Password)
```

**Labels:** `flow-discrepancy`, `auth`, `security`, `priority-medium`

**Description (Copy ข้อความด้านล่างนี้):**
```markdown
## 📌 ปัญหาที่พบ (Problem Description)
1. ใน Flow US-01 หน้า 30 ระบุให้กรอกเฉพาะ `Username` และ `Password` แต่ใน Figma `auth/frame_2.svg` มีฟิลด์ `Email` ด้วย
2. ใน Flow เดิมไม่มีกระบวนการลืมรหัสผ่านและการตั้งรหัสผ่านใหม่ ทั้งที่มีหน้าจอ UI ครบใน Figma (`auth/frame_3` ถึง `frame_6`)

## 🎯 สิ่งที่ต้องแก้ไข / ผลลัพธ์ที่ต้องการ (Expected Behavior)
1. **Update Sign Up Flow:** เพิ่มฟิลด์ Email ในฟอร์มสมัครสมาชิก พร้อมขั้นตอนตรวจสอบ Email Regex Format และเช็ค Email ซ้ำใน DB
2. **Add Forgot Password Sub-flow:**
   - ผู้ใช้กด "Forgot password?" บนหน้า Login (`auth/frame_1.svg`)
   - กรอก Email เพื่อขอ Reset Link (`auth/frame_3.svg`)
   - ระบบส่งอีเมลพร้อม Secure Token (TTL 15 นาที) ➔ แสดงหน้า Email Sent (`auth/frame_4.svg`)
   - ผู้ใช้กดลิงก์จากอีเมล ➔ เข้าหน้าตั้งรหัสผ่านใหม่ (`auth/frame_5.svg`)
   - บันทึกรหัสผ่านใหม่สำเร็จ ➔ แสดง Success State พร้อมปุ่ม Back to Login (`auth/frame_6.svg`)

## 🖼️ หน้าจออ้างอิงจาก Figma
- `ExportBlock/SVG/auth/frame_1.svg` ถึง `frame_6.svg`

## 🏷️ Acceptance Criteria
- [ ] Swimlane US-01 มีฟิลด์ Username, Email, Password ครบถ้วน
- [ ] มี Sub-flow สำหรับ Forgot Password และ Reset Password ที่สมบูรณ์
- [ ] ระบุเงื่อนไข Token Expired / Invalid Token ไว้อย่างชัดเจน
```

---

---

### Issue 4: `[FLOW-FIX: US-05-1] ปรับระบบลงขายการ์ดให้ค้นหาจาก Master Catalog และระบุ Condition Grading`

**Title:**
```
[FLOW-FIX: US-05-1] ปรับระบบลงขายการ์ดให้ค้นหาจาก Master Catalog และระบุ Condition Grading
```

**Labels:** `flow-discrepancy`, `seller`, `inventory`, `priority-medium`

**Description (Copy ข้อความด้านล่างนี้):**
```markdown
## 📌 ปัญหาที่พบ (Problem Description)
ใน Flow US-05-1 (หน้า 27) ระบุให้ผู้ขายพิมพ์ชื่อการ์ดและชื่อเกมเองแบบอิสระ ซึ่งจะทำให้ข้อมูลชื่อการ์ดในระบบสะกดผิดเพี้ยน ไม่สามารถจัดกลุ่มการ์ดใบเดียวกันจากหลายร้านค้าได้ และขัดแย้งกับ Figma ที่ให้ค้นหาการ์ดมาตรฐานของระบบ

## 🎯 สิ่งที่ต้องแก้ไข / ผลลัพธ์ที่ต้องการ (Expected Behavior)
ปรับปรุงกระบวนการลงขายการ์ด (Add Product Flow) ให้ตรงกับ `seller/frame_3.svg`:
1. ผู้ขายพิมพ์ค้นหาชื่อการ์ดจาก **Master Card Database** (ดึงรูป Official, หมายเลขการ์ด, ชุด Booster อัตโนมัติ)
2. เลือกระดับ **สภาพการ์ด (Condition Grading):** `Mint (M)`, `Near Mint (NM)`, `Lightly Played (LP)`, `Moderately Played (MP)` หรือ `Graded (PSA/BGS)`
3. อัปโหลดรูปถ่ายสภาพจริงของการ์ด (Actual Photos: ด้านหน้า, ด้านหลัง, ซูมมุมตำหนิ)
4. ระบุราคาขาย และจำนวนสต็อก ➔ กดยืนยันลงขาย ➔ บันทึกลงตาราง `seller_listings`

## 🖼️ หน้าจออ้างอิงจาก Figma
- `ExportBlock/SVG/seller/frame_2, 3, 4.svg`

## 🏷️ Acceptance Criteria
- [ ] Swimlane ระบุขั้นตอนการ Query จาก Master Card DB ชัดเจน
- [ ] มีขั้นตอนบังคับเลือก Condition และอัปโหลดภาพถ่ายสภาพจริง
- [ ] มี Error Handling กรณีไม่พบการ์ดใน Master Catalog
```

---

---

### Issue 5: `[FLOW-FIX: US-02/03] ปรับปรุงระบบค้นหาและตะกร้าให้รองรับ Multi-Seller และ Cart Drawer`

**Title:**
```
[FLOW-FIX: US-02/03] ปรับปรุงระบบค้นหาและตะกร้าให้รองรับ Multi-Seller และ Cart Drawer
```

**Labels:** `flow-discrepancy`, `marketplace`, `cart`, `priority-medium`

**Description (Copy ข้อความด้านล่างนี้):**
```markdown
## 📌 ปัญหาที่พบ (Problem Description)
Flow US-02 และ US-03 มองว่าการ์ด 1 ใบมีสต็อกรวมก้อนเดียว และแจ้ง Error ทันทีบนหน้าสินค้า แต่ในความเป็นจริง (Figma) การ์ดใบเดียวกันมีหลายร้านค้าลงขาย (Multi-Seller Listing) ในราคาและสภาพที่ต่างกัน

## 🎯 สิ่งที่ต้องแก้ไข / ผลลัพธ์ที่ต้องการ (Expected Behavior)
1. **Card Detail Page (`Shop & Browse/frame_3.svg`):** แสดงรายการผู้ขายทุกคนที่ลงขายการ์ดใบนั้น (เรียงตามราคาต่ำสุด หรือสภาพที่เลือก)
2. **Add to Cart Action:** ผู้ซื้อเลือกซื้อจากร้านค้าที่ต้องการ ➔ กด "Add to Cart" ➔ ระบบเปิด **Cart Drawer (`Shop & Browse/frame_6.svg`)** สไลด์ออกมาจากขวา
3. **Cart Item Model:** รายการในตะกร้าจะต้องผูกกับ `listing_id` (เฉพาะเจาะจงร้านค้า) ไม่ใช่ผูกกับ `card_id` รวม

## 🖼️ หน้าจออ้างอิงจาก Figma
- `ExportBlock/SVG/Shop & Browse/frame_2, 3, 6.svg`

## 🏷️ Acceptance Criteria
- [ ] Flow ระบุขั้นตอนการเลือก Seller Listing ชัดเจน
- [ ] การเพิ่มสินค้าลงตะกร้าเปิด Cart Drawer โดยไม่ต้อง Refresh หน้าเว็บ
- [ ] ระบบตะกร้าจัดกลุ่มสินค้าแยกตามร้านค้า (Group by Seller)
```

---

---

### Issue 6: `[FLOW-NEW: Seller/Admin] เพิ่ม Flow ฟีเจอร์ที่ตกหล่น (Wallet, Bulk CSV, และ Dispute)`

**Title:**
```
[FLOW-NEW: Seller/Admin] เพิ่ม User Flow สำหรับฟีเจอร์ที่ตกหล่น (Seller Wallet, Bulk CSV Upload, และ Dispute Claims)
```

**Labels:** `feature`, `seller-center`, `admin`, `wallet`, `dispute`

**Description (Copy ข้อความด้านล่างนี้):**
```markdown
## 📌 ปัญหาที่พบ (Problem Description)
ใน Figma มีหน้าจอ UI ที่สำคัญและสมบูรณ์มาก แต่ยังไม่มี User Flow ในเอกสาร PDF เลย 3 ระบบหลัก:
1. **Seller Wallet & Payout:** การดูยอดเงินที่ถอนได้ และสั่งถอนเงินเข้าบัญชีธนาคาร (`seller/frame_9-11`)
2. **Bulk CSV Upload:** การนำเข้าสต็อกการ์ดจำนวนมากผ่านไฟล์ CSV (`seller/frame_8`)
3. **Dispute Resolution Center:** ศูนย์ตัดสินข้อพิพาทเมื่อการ์ดชำรุดหรือไม่ตรงปก (`platform-admin/frame_7`)

## 🎯 สิ่งที่ต้องทำ (Tasks & Deliverables)
จัดทำ Swimlane User Flow เพิ่มเติม 3 แผนผัง:
1. **US-Seller-Wallet:** Flow ร้านค้ากดถอนเงิน ➔ ตรวจสอบยอดเงินคงเหลือ ➔ เช็คความถูกต้องชื่อบัญชีกับ KYC ➔ สร้าง Transaction สั่งถอน
2. **US-Seller-Bulk:** Flow อัปโหลดไฟล์ CSV ➔ Validate โครงสร้างแถวข้อมูล ➔ บันทึกสต็อกแบบ Batch ➔ แสดงรายงานผลสำเร็จ/แถวที่ Error
3. **US-Admin-Dispute:** Flow ผู้ซื้อยื่นเคลม ➔ เจ้าหน้าที่ดูรูปถ่าย/วิดีโอ Unboxing ของ Hub ➔ Admin ตัดสินผล (Approve Refund หรือ Reject Dispute)

## 🖼️ หน้าจออ้างอิงจาก Figma
- `ExportBlock/SVG/seller/frame_8, 9, 10, 11.svg`
- `ExportBlock/SVG/platform-admin/frame_7.svg`
- รายงานอ้างอิง: `Flow_devops/ExportBlock/สิ่งที่ต้องแก้/System & Edge Case FlawsMD.md`

## 🏷️ Acceptance Criteria
- [ ] สร้าง Swimlane Diagram แยกสำหรับทั้ง 3 ฟีเจอร์
- [ ] มีการเชื่อมโยง State Machine ระหว่างระบบ Wallet และระบบ Escrow
```

---

*เอกสารฉบับนี้ถูกสร้างและบันทึกไว้ใน `Flow_devops/ExportBlock/ความขัดแย้งกันของ flow/GITHUB_ISSUES_FLOW_CONFLICTS.md` เรียบร้อยแล้วครับ*
