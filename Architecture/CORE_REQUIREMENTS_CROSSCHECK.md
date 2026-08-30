# Core Requirements Cross-check — "Mythix TCG Platform" Deep Research (Rev.4)

> Cross-check ระหว่าง 8 core requirement ของ course PDF กับเนื้อหา research doc "Mythix TCG
> Platform — Deep Research & Product Requirements Reset" (Rev.4, 2026-08-29, source:
> `C:\Users\Lenovo\tcg-store-frontend` — เครื่องเพื่อนร่วมทีม ยังไม่ยืนยันว่า sync เข้า repo กลาง)
> **Decision ที่ล็อกแล้ว (2026-08-29):** `Admin` ใน core requirement = **Seller Admin** เท่านั้น
> ไม่มี platform-level Admin แยกต่างหาก อ่านคู่กับ `SCOPE_PIVOT_P2P_CROSSCHECK.md` — เอกสารนั้นเคย
> สมมติมี Admin กลางไว้อนุมัติ seller verification, ตอนนี้ **ส่วนนั้นถูก override โดย decision นี้**

รายการที่เคย mark ว่า `##เกิน Requirement##` (P-06, P-07, P-09) **ไม่ตัดออก** ตามคำสั่งผู้ใช้ — เก็บ
ไว้เป็น stretch/enhancement ที่เกินขอบเขต grading บังคับ แต่ไม่ใช่ของที่ต้องรื้อ

---

## 1. ตารางความครบถ้วน (หลังเติม gap)

| # | Core Requirement (PDF) | Rev.4 doc คุมด้วยอะไร | สถานะก่อนเติม | เติมอะไร (ด้านล่าง) |
|---|---|---|---|---|
| 1 | User login system | ไม่มีในเนื้อหาที่ได้รับ | ❌ ขาด | เพิ่ม §2.1 |
| 2 | Browse (game/name/price/stock/**image**) | Catalog Card / ProductListing (P-03, P-06) — ไม่พูดถึง `image` field ตรง ๆ | ⚠️ partial | เพิ่ม §2.2 |
| 3 | Cart + **update quantity** | Workflow พูดแค่ "Browse → Cart → Place Order" ไม่มี update-quantity | ⚠️ partial | เพิ่ม §2.3 |
| 4 | Place order (no online payment) | P-05 ตรงเป๊ะ | ✅ ครบ | ไม่ต้องเติม |
| 5 | Admin dashboard CRUD inventory | Executive decision item 7 (Seller Admin ทำ CRUD ของตน) — เดิมขัดกับ item 3/8 ที่พูดถึงงานอนุมัติ/moderation ที่ไม่มีใครทำ | ⚠️ contradiction | เคลียร์ที่ §2.4 (ล็อก Admin=Seller แล้ว) |
| 6 | Admin add cost + calc profit | P-08 + item 7 | ✅ ครบ | ไม่ต้องเติม |
| 7 | Mark fulfilled/pending | P-09 + item 7 (มี `Cancelled` เพิ่มมา — เกิน requirement, เก็บไว้) | ✅ ครบ (+เกิน) | ไม่ต้องเติม |
| 8 | Stock levels per item | P-09 reservation semantics (เกิน requirement ในแง่ทำ reservation จริง ไม่ใช่แค่ display) | ✅ ครบ (+เกิน) | ไม่ต้องเติม |

---

## 2. Gap ที่เติมให้

### 2.1 User login system

Rev.4 doc ไม่พูดถึง auth เลย ทั้งที่เป็น requirement ข้อแรกของ PDF และ frontend ปัจจุบัน
(`tcg-store-frontend`) มี implementation อยู่แล้วบางส่วน (`LoginPage`, `SignUpPage`, forgot/reset
flow, `useAuthStore`, `ProtectedRoute`) — ให้ยึด flow เดิมนี้เป็น baseline แล้วปรับตาม role ใหม่:

- **Login/Register:** email + password, ไม่ผูก external OAuth (ตาม hard rule ห้าม external
  service) — เก็บ JWT ใน localStorage ตามที่ implement ไว้แล้ว
- **Guest access:** browse catalog ได้โดยไม่ login (สอดคล้อง P-01 "ทุกคนเป็น Member ก่อน" — สื่อว่า
  สิทธิ Buyer ทั่วไปเริ่มทันทีหลัง register แต่ **browse ไม่ต้อง login เลยด้วยซ้ำ**)
- **Login-gated actions:** add-to-cart, place order, สร้าง Collection, ยื่นขอเป็น Seller —
  ต้อง login ก่อนเท่านั้น (ContextualLoginModal ที่มีอยู่แล้วใช้ต่อได้)
- **Role หลัง login:** `Role = 'USER'` เดียวเท่านั้นในระบบ (ไม่มี `ADMIN` แยกอีกต่อไป ตาม §2.4) —
  ความเป็น Seller คือ flag บน user ไม่ใช่ role

### 2.2 Browse — image field

Catalog Card / ProductListing ต้องมี field รูปภาพชัดเจน ไม่ใช่แค่โดยนัย:

- `imageUrl` (บังคับ 1 รูปขึ้นไป) — ใช้ default catalog image ของการ์ดรุ่นนั้นเป็นค่าเริ่มต้นได้
  (เช่น official card art) เพื่อให้ browse ใช้งานได้แม้ Seller ยังไม่อัปโหลดรูปจริง
- Seller **ควร** (ไม่บังคับสำหรับ MVP) อัปโหลดรูปถ่ายจริงของสำเนาที่ตัวเองถืออยู่แทน default image
  เพราะเป็นสินค้าสะสมที่สภาพจริงต่างกันได้ — ตรงนี้เป็น enhancement เกิน core requirement เก็บไว้
  เป็นตัวเลือกได้ ไม่บังคับ
- ฟิลด์นี้มีอยู่แล้วใน `Product.image` (`src/types/index.ts`) ของ frontend ปัจจุบัน — ใช้ต่อได้เลย
  ไม่ต้องเพิ่ม field ใหม่

### 2.3 Cart — update quantity

เพิ่ม behavior ที่ต้องมีให้ตรง PDF ("Add items... and update quantity"):

- เพิ่ม/ลดจำนวนต่อรายการในตะกร้า (stepper +/-) และพิมพ์จำนวนตรง ๆ ได้
- Clamp ไม่ให้เกิน `availableStock` ของ listing นั้น (ผูกกับ reservation semantics ใน P-09 — เช็ค
  `onHand - reserved` ทุกครั้งที่ปรับจำนวน ไม่ใช่เช็คแค่ตอน place order)
- ลดจำนวนเหลือ 0 = ลบรายการออกจากตะกร้า (ไม่ใช่ error state)
- `useCartStore` ที่มีอยู่แล้วใน frontend รองรับ `updateQuantity` อยู่แล้วในระดับ store — เช็คว่า UI
  (`CartPage.tsx`) เปิดใช้ครบหรือยัง ไม่ใช่แค่ add/remove

### 2.4 Admin = Seller — เคลียร์ contradiction (locked decision)

**ตัดสินแล้ว:** ไม่มี platform-level Admin ในระบบนี้ คำว่า "Admin" ใน PDF core requirement
หมายถึง **Seller Admin Dashboard** — พื้นที่จัดการ inventory/order ของ Seller ราย ๆ นั้นเอง ไม่ใช่
คนกลางดูแลทั้งแพลตฟอร์ม

ผลที่ตามมาต่อ Executive decision เดิมที่เคยขัดกันเอง:

- **Item 3 "ตรวจสอบและอนุมัติผู้ที่ต้องการขาย" (seller verification gate)** — เมื่อไม่มี admin กลาง
  คอยอนุมัติ ต้องเปลี่ยนเป็น **self-serve**: user กรอก Seller Profile (ชื่อร้าน/ช่องทางติดต่อ) แล้ว
  `sellerStatus` เปลี่ยนเป็น `VERIFIED` ทันที ไม่มี manual approval step คำว่า "Verified" ในที่นี้
  หมายถึง "กรอกโปรไฟล์ผู้ขายครบแล้ว" ไม่ใช่ KYC หรือ identity verification จริง — ต้อง sync คำนี้
  กับ `SCOPE_PIVOT_P2P_CROSSCHECK.md` (เดิมเขียนไว้ว่ามี "Admin อนุมัติคำขอ verify seller" — **ส่วน
  นั้น superseded โดย decision นี้แล้ว**)
- **Item 8 "ดูแล Report, moderation และ seller trust"** — ไม่มี platform admin มาทำหน้าที่นี้อีก
  ต่อไป **descope ออกจาก MVP** เข้ากลุ่มเดียวกับ P-07 (safety layer) ที่ผู้เขียนเอง mark ไว้แล้วว่า
  เกิน requirement — ปล่อยไว้เป็น backlog ไม่ใช่ blocker ของ core requirement 8 ข้อ
- **Role model สรุปสุดท้าย:** `Role = 'USER'` ตัวเดียว + `sellerStatus: 'NONE' | 'VERIFIED'` (ตัด
  `'PENDING'` ออกด้วยเพราะไม่มีใครอนุมัติ — self-serve ข้ามสถานะรอตรงไปที่ VERIFIED ได้เลย)

---

## 3. รายการที่ mark ว่าเกิน Requirement — เก็บไว้ตามเดิม ไม่ตัด

| Item | อยู่ตรงไหน | เหตุผลที่เก็บไว้ (ตามคำสั่งผู้ใช้) |
|---|---|---|
| P-06 Structured data (set/collector number/language/finish/condition/grade เป็น field แยก ไม่ใช่ free text) | Catalog Card schema | เกิน core requirement (PDF ขอแค่ game/name/price/stock/image) แต่เป็น data quality ที่ดีสำหรับ TCG marketplace จริง — เก็บไว้ |
| P-07 Safety layer (contact handoff, warning, report, block, audit trail) | Order/conversation layer | เกินเพราะไม่มี payment/shipping ให้ป้องกันอยู่แล้วตาม scope ที่ตัดไป — แต่เก็บไว้เป็นแนวทางอนาคตถ้าจะขยาย |
| P-09 Stock reservation semantics (`onHand - reserved`, ไม่ใช่แค่ตัวเลข static) | Stock model | เกินเพราะ PDF ขอแค่ "display stock levels" ไม่ได้ขอ reservation logic — แต่จำเป็นถ้าจะรองรับ update-quantity (§2.3) ให้ไม่ overselling จริง เก็บไว้เพราะ 2.3 พึ่งพา P-09 อยู่แล้ว |

---

## 4. สรุปหลังเติม

Core requirement ทั้ง 8 ข้อ **ครบแล้ว** หลังเติม §2.1–§2.3 และเคลียร์ contradiction ที่ §2.4:

1. Login ✅ (เติม §2.1)
2. Browse w/ image ✅ (เติม §2.2, field มีอยู่แล้วในโค้ด)
3. Cart + update quantity ✅ (เติม §2.3, store รองรับอยู่แล้ว เช็ค UI)
4. Place order no payment ✅ (มีอยู่แล้วใน Rev.4)
5. Admin CRUD inventory ✅ (เคลียร์แล้วว่า Admin=Seller, ไม่มี contradiction อีก)
6. Cost/profit calculator ✅ (มีอยู่แล้วใน Rev.4)
7. Fulfilled/Pending ✅ (มีอยู่แล้ว + Cancelled เกิน)
8. Stock display ✅ (มีอยู่แล้ว + reservation เกิน)

ของที่เกิน requirement (P-06, P-07, P-09) เก็บไว้ทั้งหมดตามคำสั่ง ไม่ตัด — ถือเป็น enhancement
backlog ที่ทำได้ถ้าเวลาเหลือ ไม่ใช่ blocker ของ checkpoint

---

*ต้องตามไปแก้ต่อ: `SCOPE_PIVOT_P2P_CROSSCHECK.md` §4 (ลบ "Admin อนุมัติ seller verification" ออก
เพราะกลายเป็น self-serve แล้ว), `CONTEXT.md` (role decision เดิมเรื่อง Seller/Platform-Admin แยก
role ต้อง supersede รอบสุดท้ายด้วย decision นี้)*
