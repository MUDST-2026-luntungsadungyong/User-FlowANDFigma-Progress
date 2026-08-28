# 🃏 TCG Trading Platform — Comprehensive UI Frames & Architecture Catalog
> **แหล่งข้อมูลอ้างอิง:** Figma Design Export (`ExportBlock/SVG/`)  
> **สถานะการแปลงไฟล์:** สกัดและ Validate ไฟล์ SVG ทุกโฟลเดอร์เป็น 100% Valid XML เรียบร้อยแล้ว

---

## 📑 สรุปภาพรวมโครงสร้างทั้ง 7 โมดูล (Platform Overview)

| โฟลเดอร์ (Module) | จำนวน Frames | บทบาทผู้ใช้งานหลัก (Target Roles) | วัตถุประสงค์หลักของระบบ (Core Purpose) |
| :--- | :---: | :--- | :--- |
| **1. `auth/`** | **7 Frames** | Guest / All Users | ระบบเข้าสู่ระบบ, สมัครสมาชิก, รีเซ็ตรหัสผ่าน และยืนยันความปลอดภัย |
| **2. `Shop & Browse/`** | **11 Frames** | Guest & Customer (Buyer) | หน้าแรก Marketplace, แคตตาล็อกค้นหา/กรองการ์ด, หน้ารายละเอียดการ์ด และตะกร้าด่วน |
| **3. `Checkout Flow/`** | **7 Frames** | Customer (Buyer) | ระบบสั่งซื้อและชำระเงินแบบ Escrow Protection, เลือกที่อยู่, และติดตามสถานะขนส่ง |
| **4. `Buyer Account & Storefront/`** | **6 Frames** | Buyer & Public Viewers | หน้าร้านค้าสาธารณะของผู้ขาย (Storefront Profile, การ์ดที่ลงขาย, รีวิวและคะแนนร้าน) |
| **5. `profile/`** | **4 Frames** | Customer (Buyer) | จัดการข้อมูลโปรไฟล์ส่วนตัว, สมุดที่อยู่จัดส่ง (Address Book), และเบอร์โทรศัพท์ (US-08) |
| **6. `seller/`** | **20 Frames** | Seller (ร้านค้า) | แดชบอร์ดร้านค้า, จัดการสต็อกการ์ด (CRUD), ส่งของเข้า QC Hub (Leg 1), และกระเป๋าเงิน |
| **7. `platform-admin/`** | **18 Frames** | Super Admin & QC Hub Staff | แดชบอร์ดภาพรวมระบบ, ศูนย์ตรวจสภาพการ์ด (QC Hub), จัดส่ง Leg 2, คุม Escrow และ Dispute |

---

## 🔍 รายละเอียดเจาะลึกทุกหน้าจอในแต่ละโมดูล (Deep-dive Frame Catalog)

```
📂 ExportBlock/SVG/
 ├── 📁 auth/
 ├── 📁 Shop & Browse/
 ├── 📁 Checkout Flow/
 ├── 📁 Buyer Account & Storefront/
 ├── 📁 profile/
 ├── 📁 seller/
 └── 📁 platform-admin/
```

---

### 1. 📂 `auth/` — Authentication & Account Security System
*โมดูลจัดการบัญชีผู้ใช้งานและการเข้าถึงระบบ (รองรับ Guest, Customer, Seller, Admin)*

| ชื่อไฟล์ | ขนาด Frame | รายละเอียดและหน้าที่ของหน้าจอ (Functionality & UI Elements) |
| :--- | :---: | :--- |
| **`frame_1.svg`** | 1440×1024 | **Login Screen (เข้าสู่ระบบ):** ฟอร์มล็อกอินตรงกลาง (378×449px), ช่องกรอก Email/Username, Password, ปุ่ม "Log in", ลิงก์ Forgot Password และ Sign Up |
| **`frame_2.svg`** | 1440×900 | **Sign Up Screen (สมัครสมาชิก):** ฟอร์มลงทะเบียน (400×544px), ช่องกรอก Username, Email, Password, ปุ่ม "Create Account" |
| **`frame_3.svg`** | 1440×900 | **Forgot Password Screen (ขอรีเซ็ตรหัสผ่าน):** ฟอร์มระบุ Email เพื่อขอรับลิงก์รีเซ็ตรหัสผ่าน พร้อมปุ่ม "Send Reset Link" |
| **`frame_4.svg`** | 1440×900 | **Email Sent Verification (ยืนยันส่งอีเมล):** กล่องแจ้งเตือนการส่งลิงก์ยืนยันสำเร็จ พร้อมคำแนะนำให้ไปเช็ค Inbox |
| **`frame_5.svg`** | 1440×900 | **Reset Password Screen (ตั้งรหัสผ่านใหม่):** ฟอร์มกรอก New Password และ Confirm Password พร้อมปุ่ม "Reset Password" |
| **`frame_6.svg`** | 1440×900 | **Success State (ดำเนินการสำเร็จ):** หน้าแจ้งสถานะเสร็จสิ้น พร้อมปุ่ม Back to Login |
| **`frame_7.svg`** | 1440×900 | **Logout Modal Dialog:** Popup Backdrop สีดำคลุมทั้งจอ พร้อมกล่องยืนยันการออกจากระบบ (ปุ่ม Cancel และ Confirm Logout) |

---

### 2. 📂 `Shop & Browse/` — Marketplace Discovery & Product Details
*โมดูลการค้นหา เลือกดูการ์ด TCG และตรวจสอบรายละเอียดก่อนตัดสินใจซื้อ*

| ชื่อไฟล์ | ขนาด Frame | รายละเอียดและหน้าที่ของหน้าจอ (Functionality & UI Elements) |
| :--- | :---: | :--- |
| **`frame_1.svg`** | 1440×4110 | **Marketplace Landing Page (Home):** แบนเนอร์โปรโมชั่นใหญ่, การ์ดแนะนำ (Featured Cards), Top Sellers, หมวดหมู่เกมการ์ด (One Piece, Pokémon, MTG, Yu-Gi-Oh) |
| **`frame_2.svg`** | 1440×2144 | **Catalog Search & Multi-Filter View:** รายการการ์ดทั้งหมดพร้อมตัวกรอง (เกม, ความหายาก/Rarity, ช่วงราคา, สภาพการ์ด Mint/NM/LP, การ์ดพร้อมส่ง) |
| **`frame_3.svg`** | 1440×900 | **Card Detail Page (หน้ารายละเอียดการ์ด):** ภาพสแกนการ์ด High-Res, รายการผู้ขายที่ลงขายการ์ดใบนี้ (เปรียบเทียบราคา/สภาพ/คะแนนร้าน), ปุ่ม Add to Cart & Buy Now |
| **`frame_4.svg`** | 1508×770 | **Card Condition & Price Comparison View:** ตารางเปรียบเทียบสภาพการ์ด (Graded vs Raw Card) และกราฟประวัติราคาตลาด |
| **`frame_5.svg`** | 1440×900 | **Seller Listing Preview on Product Page:** การ์ดแสดงข้อมูลร้านค้าเจ้าของการ์ด, Rating ความน่าเชื่อถือ และระยะเวลาจัดส่งเฉลี่ยเข้า Hub |
| **`frame_6.svg`** | 1440×376 | **Cart Drawer / Quick Slide-over:** แถบสไลด์ดูตะกร้าสินค้าแบบด่วนจากขอบจอด้านขวาเมื่อกดเพิ่มการ์ดลงตะกร้า |
| **`frame_7.svg`** | 1440×900 | **Empty Search State:** หน้าจอเมื่อค้นหาการ์ดแล้วไม่พบผลลัพธ์ พร้อมแนะนำการ์ดใกล้เคียง |
| **`frame_8.svg`** | 1440×420 | **Card Zoom & Inspection Modal:** Popup ขยายดูรายละเอียดตำหนิและภาพถ่ายสภาพจริงของการ์ด |
| **`frame_9.svg`** | 1440×2172 | **TCG Game Category Page:** หน้าเฉพาะสำหรับแฟนเกมการ์ดแต่ละเรื่อง (เช่น รวมการ์ด One Piece แบ่งตามชุด Booster OP-01 ถึง OP-09) |
| **`frame_10.svg`** | 1440×376 | **Escrow Guarantee & Protection Banner:** ส่วนแสดงความมั่นใจเรื่องระบบคนกลาง Escrow และการรับประกันของแท้ 100% |
| **`frame_11.svg`** | 1440×376 | **Footer Navigation:** ลิงก์ข้อกำหนดการใช้งาน, นโยบายคืนเงิน, และศูนย์ช่วยเหลือ |

---

### 3. 📂 `Checkout Flow/` — Escrow Checkout & Order Processing
*โมดูลการสั่งซื้อ ชำระเงินเข้า Escrow และติดตามการจัดส่งแบบ 2 จังหวะ (2-Leg Shipping)*

| ชื่อไฟล์ | ขนาด Frame | รายละเอียดและหน้าที่ของหน้าจอ (Functionality & UI Elements) |
| :--- | :---: | :--- |
| **`frame_1.svg`** | 1440×784 | **Shopping Cart Review (หน้าตะกร้าสินค้า):** ตรวจสอบรายการการ์ด, ปรับจำนวน, ลบรายการที่ไม่ต้องการ, สรุปยอดเงินรวม และค่าจัดส่ง |
| **`frame_2.svg`** | 1440×784 | **Shipping Address Selection:** เลือกที่อยู่จัดส่งจากที่บันทึกไว้ หรือกดเพิ่มที่อยู่ใหม่ พร้อมตรวจสอบเบอร์โทรศัพท์ผู้รับ |
| **`frame_3.svg`** | 1440×800 | **Delivery Method Selection:** เลือกรูปแบบการจัดส่ง (Standard Hub Inspection vs Express Delivery) |
| **`frame_4.svg`** | 1440×800 | **Payment Method Selection (Escrow Hold):** เลือกช่องทางชำระเงิน (PromptPay QR, บัตรเครดิต/เดบิต, TrueMoney) พร้อมแจ้งชัดเจนว่าเงินจะถูกพักไว้ที่ Escrow |
| **`frame_5.svg`** | 1440×800 | **QR Code Payment Modal:** แสดง QR Code พร้อมเพย์แบบ Dynamic พร้อมเวลานับถอยหลัง (Timer) |
| **`frame_6.svg`** | 1440×900 | **Order Placed & Escrow Confirmation:** หน้าแจ้งผลสั่งซื้อสำเร็จ พร้อมแสดงรหัสคำสั่งซื้อ (Order ID) และเงินถูกล็อกไว้ใน Escrow Vault |
| **`frame_7.svg`** | 1440×800 | **2-Leg Fulfillment Timeline Tracker:** ติดตามสถานะคำสั่งซื้อแบบ 4 ขั้น: (1) ชำระแล้ว ➔ (2) ร้านส่งเข้า Hub ➔ (3) Hub ตรวจ QC ผ่าน ➔ (4) ส่งถึงผู้ซื้อ |

---

### 4. 📂 `Buyer Account & Storefront/` — Public Store Profiles
*โมดูลหน้าโปรไฟล์ร้านค้าสาธารณะที่ผู้ซื้อสามารถเข้าไปดูข้อมูลร้านค้าได้*

| ชื่อไฟล์ | ขนาด Frame | รายละเอียดและหน้าที่ของหน้าจอ (Functionality & UI Elements) |
| :--- | :---: | :--- |
| **`frame_1.svg`** | 1440×1000 | **Storefront Main Header & Banner:** ป้ายร้านค้า, โลโก้, ป้าย Verified Store, คะแนนดาวรวม, ยอดขายสำเร็จ และปุ่ม Follow |
| **`frame_2.svg`** | 1440×900 | **Storefront Card Catalog:** แท็บแสดงการ์ดทั้งหมดที่ร้านค้านี้ลงขายอยู่ พร้อมระบบค้นหาภายในร้าน |
| **`frame_3.svg`** | 1440×1500 | **Storefront Reviews & Feedback:** ประวัติรีวิวและคะแนนความพึงพอใจจากผู้ซื้อที่ได้รับสินค้าจริง |
| **`frame_4.svg`** | 1440×160 | **Storefront Tab Navigation:** แถบสลับหน้า (Home / All Cards / Reviews / About Store) |
| **`frame_5.svg`** | 1440×376 | **Store Policies & Shipping Guarantee:** ข้อมูลนโยบายการจัดส่งเข้า QC Hub และเวลาเฉลี่ยในการ Drop-off พัสดุ |
| **`frame_6.svg`** | 1440×376 | **Store Contact & FAQ Section:** ช่องทางติดต่อสอบถามและคำถามที่พบบ่อยของร้านค้า |

---

### 5. 📂 `profile/` — Customer Profile & Settings (US-08)
*โมดูลจัดการข้อมูลผู้ซื้อ สมุดที่อยู่ และการตั้งค่าความปลอดภัย*

| ชื่อไฟล์ | ขนาด Frame | รายละเอียดและหน้าที่ของหน้าจอ (Functionality & UI Elements) |
| :--- | :---: | :--- |
| **`frame_1.svg`** | 1440×937 | **My Profile Overview:** สรุปข้อมูลส่วนตัว (Avatar, Display Name, Email, วันที่เข้าร่วม, สรุปจำนวนออเดอร์) |
| **`frame_2.svg`** | 1440×900 | **Edit Profile Details (US-08-3, US-08-4):** ฟอร์มแก้ไขชื่อแสดงผล (Display Name), เปลี่ยนเบอร์โทรศัพท์สำหรับขนส่ง และอัปโหลด Avatar |
| **`frame_3.svg`** | 1440×900 | **Address Book Management (US-08-1, US-08-2):** หน้ารวมที่อยู่จัดส่ง, ปุ่มเพิ่มที่อยู่ใหม่ (Add Address), ปุ่มแก้ไข (Edit), และตั้งเป็นที่อยู่หลัก (Default) |
| **`frame_4.svg`** | 1440×900 | **Security & Password Settings:** ฟอร์มเปลี่ยนรหัสผ่านและประวัติการเข้าสู่ระบบเพื่อความปลอดภัย |

---

### 6. 📂 `seller/` — Seller Center & Store Management (US-05, US-06, US-07)
*โมดูลระบบจัดการหลังบ้านของร้านค้าผู้ขายการ์ด*

| ชื่อไฟล์ | ขนาด Frame | รายละเอียดและหน้าที่ของหน้าจอ (Functionality & UI Elements) |
| :--- | :---: | :--- |
| **`frame_1.svg`** | 1440×900 | **Seller Dashboard Summary (US-06):** รายได้รวม, ยอดขายประจำเดือน, จำนวนออเดอร์ใหม่, สินค้าพร้อมส่ง และกราฟแนวโน้มยอดขาย |
| **`frame_2.svg`** | 1686×1100 | **Inventory Management Table (US-05):** ตารางสต็อกการ์ดทั้งหมด (รูป, ชื่อ, สภาพ, ราคา, สต็อกคงเหลือ, สวิตช์ Show/Hide, ปุ่ม Edit/Delete) |
| **`frame_3.svg`** | 1686×1100 | **Add New Product Form (US-05-1):** ฟอร์มลงขายการ์ด (ค้นหาชื่อการ์ดจาก Master Data, ระบุสภาพ, ใส่ราคา, จำนวน, อัปโหลดรูปการ์ดจริง) |
| **`frame_4.svg`** | 1686×900 | **Edit Product Details (US-05-3):** แก้ไขราคาขายและจำนวนสต็อกการ์ดที่ลงขายอยู่ |
| **`frame_5.svg`** | 1686×900 | **Seller Order Management (US-07):** รายการคำสั่งซื้อที่ต้องจัดส่ง (แท็บ: To Ship เข้า Hub, In Transit, Arrived at Hub, Completed) |
| **`frame_6.svg`** | 1388×755 | **Leg 1 Fulfillment & Shipping Label:** หน้ารายละเอียดออเดอร์ และปุ่มพิมพ์ใบปะหน้าพัสดุสำหรับส่งไปยังศูนย์ QC Hub |
| **`frame_7.svg`** | 1388×627 | **Tracking Number Modal:** กล่องกรอกเลขพัสดุขนส่ง (Kerry, Flash, EMS) เพื่อแจ้งว่าส่งของเข้า Hub แล้ว |
| **`frame_8.svg`** | 1440×900 | **Bulk Upload / CSV Import:** หน้าจอสำหรับอัปโหลดรายการการ์ดหลายสิบใบพร้อมกันผ่านไฟล์ CSV |
| **`frame_9.svg`** | 1440×900 | **Seller Wallet & Escrow Funds:** ยอดเงินในกระเป๋า (เงินที่ถอนได้ vs เงินที่พักอยู่ใน Escrow รอการตรวจรับ) |
| **`frame_10.svg`** | 1440×1100 | **Withdrawal Request Screen:** ฟอร์มสั่งถอนเงินเข้าบัญชีธนาคาร พร้อมคำนวณหักค่าธรรมเนียม |
| **`frame_11.svg`** | 1388×627 | **Bank Account Settings:** จัดการผูกบัญชีธนาคารสำหรับรับเงิน |
| **`frame_12.svg`** | 1440×900 | **Shop Branding Settings:** ตั้งค่าโปรไฟล์ร้าน (เปลี่ยนชื่อร้าน, อัปโหลดโลโก้, แบนเนอร์, คำอธิบายร้าน) |
| **`frame_13.svg`** | 1686×900 | **Sales Analytics & Filter (US-06):** รายงานยอดขาย กรองตาม วันนี้, รายสัปดาห์, รายเดือน, ราย 3 เดือน พร้อมปุ่ม Export CSV |
| **`frame_14.svg` - `frame_20.svg`** | 1686×900 | **Seller Alerts, Modals & QC Feedback:** หน้าต่างแจ้งผลการตรวจสภาพการ์ดจาก Hub (QC Pass / Fail) และกล่องยืนยันการลบสินค้า |

---

### 7. 📂 `platform-admin/` — Super Admin & QC Hub Console
*โมดูลสำหรับผู้ดูแลระบบสูงสุด (Super Admin) และเจ้าหน้าที่ศูนย์ตรวจสภาพ (QC Hub Staff)*

| ชื่อไฟล์ | ขนาด Frame | รายละเอียดและหน้าที่ของหน้าจอ (Functionality & UI Elements) |
| :--- | :---: | :--- |
| **`frame_1.svg`** | 1440×900 | **Super Admin Executive Dashboard:** ภาพรวมทั้งแพลตฟอร์ม (Platform GMV, Escrow Vault Balance, รายได้ค่าธรรมเนียม Commission, ยอดผู้ใช้รวม) |
| **`frame_2.svg`** | 1686×900 | **Platform All Orders Console:** ตารางคำสั่งซื้อทั้งหมดในระบบ ควบคุมสถานะ Escrow แบบ Real-time |
| **`frame_3.svg`** | 1686×1000 | **QC Hub Inspection Queue (ศูนย์ตรวจสภาพการ์ด):** คิวการ์ดที่พัสดุส่งมาถึง Hub รอเจ้าหน้าที่แกะกล่องตรวจเช็คของแท้และสภาพ |
| **`frame_4.svg`** | 1686×1299 | **QC Inspection Action & Decision Modal:** หน้าบันทึกผลการตรวจการ์ด: **Pass** (ส่งต่อ Leg 2) หรือ **Fail** (ระงับ Escrow และส่งคืน) |
| **`frame_5.svg`** | 1686×1000 | **Leg 2 Fulfillment Dispatch:** พิมพ์ใบปะหน้าส่งให้ผู้ซื้อปลายทาง พร้อมสร้าง Tracking Number อัตโนมัติ |
| **`frame_6.svg`** | 1686×1200 | **Escrow Ledger & Fund Release:** หน้าควบคุมการปล่อยเงินให้ผู้ขาย (Manual/Auto Payout) เมื่อพัสดุส่งถึงผู้ซื้อสมบูรณ์ |
| **`frame_7.svg`** | 1686×1000 | **Dispute & Claims Resolution Center:** หน้าตัดสินข้อพิพาทระหว่างผู้ซื้อกับผู้ขาย (ตรวจสอบรูปถ่ายหลักฐาน และตัดสินใจคืนเงิน) |
| **`frame_8.svg`** | 1686×1100 | **User & Seller Management Console:** จัดการบัญชีผู้ใช้, ระงับบัญชี (Ban/Unban), และตรวจสอบประวัติการทำธุรกรรม |
| **`frame_9.svg`** | 1686×1000 | **Seller KYC & Store Approval:** ตรวจสอบเอกสารบัตรประชาชนและอนุมัติร้านค้าใหม่ที่ขอเปิดขาย |
| **`frame_10.svg`** | 1686×1000 | **Master Card Catalog Database:** จัดการฐานข้อมูลการ์ดกลางของระบบ (เพิ่มชื่อการ์ด, รูปภาพมาตรฐาน, ชุดการ์ด) |
| **`frame_11.svg`** | 1686×1000 | **Platform Commission & Fee Settings:** ตั้งค่าอัตราค่าธรรมเนียมแพลตฟอร์ม (Platform Fee %), ค่าบริการ QC, และค่าธรรมเนียม Escrow |
| **`frame_12.svg` - `frame_18.svg`** | 1686×1000 | **Audit Trail Logs & System History:** บันทึกประวัติการกระทำทั้งหมดของระบบและเจ้าหน้าที่ (Audit Logs) เพื่อความโปร่งใส |

---

## 🎯 สรุปความเข้าใจเชิงสถาปัตยกรรม (Architecture Insights)

1. **สถาปัตยกรรม Escrow 2-Leg Shipping:**
   - การซื้อขายไม่ได้ส่งตรงจากผู้ขายไปหาผู้ซื้อ แต่จะส่งผ่าน **QC Hub** เสมอ
   - **Leg 1:** Seller ➔ QC Hub Staff (ตรวจแท้/ปลอม และสภาพการ์ด)
   - **Leg 2:** QC Hub Staff ➔ Buyer (เงิน Escrow จะถูกปล่อยให้ Seller เมื่อ Buyer ได้รับสินค้าถูกต้อง)
2. **การแยกบทบาทชัดเจน 5 ระดับ (5 Distinct Roles):**
   - 🌐 **Guest:** ดู Marketplace, ค้นหาการ์ด, ดูหน้าร้านค้า
   - 🛒 **Customer (Buyer):** สั่งซื้อ, จ่ายเงินเข้า Escrow, ติดตามสถานะ, จัดการ Profile & ที่อยู่ (US-08, US-09)
   - 🏪 **Seller:** จัดการสต็อกการ์ด (US-05), ดูยอดขายร้านตนเอง (US-06), ส่งของเข้า Hub (US-07)
   - 🔍 **QC Hub Staff:** ตรวจสอบสภาพการ์ด, บันทึกผล QC Pass/Fail, จัดส่ง Leg 2
   - 👑 **Super Admin:** ดูภาพรวมการเงินทั้งระบบ (GMV/Commission), คุมระบบ Escrow, อนุมัติร้านค้า และตัดสิน Dispute
