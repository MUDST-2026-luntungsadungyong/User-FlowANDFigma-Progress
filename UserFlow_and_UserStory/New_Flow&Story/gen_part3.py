from gen_base import create_svg_flow, save_svg

# US-08-1: Edit Contact Info (Originally Address)
n8_1 = [
    {'id': 'start', 'type': 'start', 'x': 100, 'y': 220, 'w': 70, 'h': 40, 'text': ['start']},
    {'id': 'c1', 'type': 'action_customer', 'x': 210, 'y': 210, 'w': 140, 'h': 60, 'text': ['เข้าหน้า Profile']},
    {'id': 'c2', 'type': 'action_customer', 'x': 390, 'y': 210, 'w': 140, 'h': 60, 'text': ['แก้ไข Contact Info', '(Facebook, Line, etc.)']},
    {'id': 'c3', 'type': 'action_customer', 'x': 570, 'y': 210, 'w': 140, 'h': 60, 'text': ['กด "Save"']},
    {'id': 'sys1', 'type': 'action_system', 'x': 750, 'y': 430, 'w': 150, 'h': 60, 'text': ['อัปเดตข้อมูลผู้ใช้ใน DB']},
    {'id': 'end', 'type': 'end', 'x': 940, 'y': 440, 'w': 70, 'h': 40, 'text': ['End']}
]
c8_1 = [
    {'points': [(170, 240), (210, 240)]},
    {'points': [(350, 240), (390, 240)]},
    {'points': [(530, 240), (570, 240)]},
    {'points': [(640, 270), (640, 460), (750, 460)]},
    {'points': [(900, 460), (940, 460)]}
]
save_svg("US-08-1_Edit-Contact.svg", create_svg_flow("US-08-1: Edit Contact Information", "customer", [("Customer", 130, 360), ("System", 360, 560)], n8_1, c8_1, 1050, 580))

# US-08-3: Edit Name
n8_3 = [
    {'id': 'start', 'type': 'start', 'x': 100, 'y': 220, 'w': 70, 'h': 40, 'text': ['start']},
    {'id': 'c1', 'type': 'action_customer', 'x': 210, 'y': 210, 'w': 140, 'h': 60, 'text': ['เข้าหน้า Profile']},
    {'id': 'c2', 'type': 'action_customer', 'x': 390, 'y': 210, 'w': 140, 'h': 60, 'text': ['แก้ไขชื่อ (Name)']},
    {'id': 'c3', 'type': 'action_customer', 'x': 570, 'y': 210, 'w': 140, 'h': 60, 'text': ['กด "Save"']},
    {'id': 'sys1', 'type': 'action_system', 'x': 750, 'y': 430, 'w': 150, 'h': 60, 'text': ['อัปเดตชื่อใน DB']},
    {'id': 'end', 'type': 'end', 'x': 940, 'y': 440, 'w': 70, 'h': 40, 'text': ['End']}
]
save_svg("US-08-3_Edit-Name.svg", create_svg_flow("US-08-3: Edit Name", "customer", [("Customer", 130, 360), ("System", 360, 560)], n8_3, c8_1, 1050, 580))

# US-08-4: Edit Phone
n8_4 = [
    {'id': 'start', 'type': 'start', 'x': 100, 'y': 220, 'w': 70, 'h': 40, 'text': ['start']},
    {'id': 'c1', 'type': 'action_customer', 'x': 210, 'y': 210, 'w': 140, 'h': 60, 'text': ['เข้าหน้า Profile']},
    {'id': 'c2', 'type': 'action_customer', 'x': 390, 'y': 210, 'w': 140, 'h': 60, 'text': ['แก้ไขเบอร์โทรศัพท์']},
    {'id': 'c3', 'type': 'action_customer', 'x': 570, 'y': 210, 'w': 140, 'h': 60, 'text': ['กด "Save"']},
    {'id': 'sys1', 'type': 'action_system', 'x': 750, 'y': 430, 'w': 150, 'h': 60, 'text': ['อัปเดตเบอร์ใน DB']},
    {'id': 'end', 'type': 'end', 'x': 940, 'y': 440, 'w': 70, 'h': 40, 'text': ['End']}
]
save_svg("US-08-4_Edit-Phone.svg", create_svg_flow("US-08-4: Edit Phone Number", "customer", [("Customer", 130, 360), ("System", 360, 560)], n8_4, c8_1, 1050, 580))

# US-09-1: View Order History
n9_1 = [
    {'id': 'start', 'type': 'start', 'x': 100, 'y': 220, 'w': 70, 'h': 40, 'text': ['start']},
    {'id': 'c1', 'type': 'action_customer', 'x': 210, 'y': 210, 'w': 140, 'h': 60, 'text': ['เข้าเมนู', '"My Orders"']},
    {'id': 'sys1', 'type': 'action_system', 'x': 390, 'y': 430, 'w': 150, 'h': 60, 'text': ['ดึงออเดอร์ของตนเอง']},
    {'id': 'c2', 'type': 'action_customer', 'x': 570, 'y': 210, 'w': 150, 'h': 60, 'text': ['แสดงประวัติคำสั่งซื้อ']},
    {'id': 'end', 'type': 'end', 'x': 760, 'y': 220, 'w': 70, 'h': 40, 'text': ['End']}
]
c9_1 = [
    {'points': [(170, 240), (210, 240)]},
    {'points': [(280, 270), (280, 460), (390, 460)]},
    {'points': [(540, 460), (645, 460), (645, 270)]},
    {'points': [(720, 240), (760, 240)]}
]
save_svg("US-09-1_View-Order-History.svg", create_svg_flow("US-09-1: View Order History (Customer)", "customer", [("Customer", 130, 360), ("System", 360, 560)], n9_1, c9_1, 900, 580))

# US-09-2: Filter Order History
n9_2 = [
    {'id': 'start', 'type': 'start', 'x': 100, 'y': 220, 'w': 70, 'h': 40, 'text': ['start']},
    {'id': 'c1', 'type': 'action_customer', 'x': 210, 'y': 210, 'w': 140, 'h': 60, 'text': ['อยู่หน้า "My Orders"']},
    {'id': 'c2', 'type': 'action_customer', 'x': 390, 'y': 210, 'w': 140, 'h': 60, 'text': ['เลือกสถานะออเดอร์', 'เพื่อกรอง (Filter)']},
    {'id': 'sys1', 'type': 'action_system', 'x': 570, 'y': 430, 'w': 150, 'h': 60, 'text': ['Query ออเดอร์ตามสถานะ']},
    {'id': 'c3', 'type': 'action_customer', 'x': 750, 'y': 210, 'w': 150, 'h': 60, 'text': ['แสดงผลลัพธ์ที่กรองแล้ว']},
    {'id': 'end', 'type': 'end', 'x': 940, 'y': 220, 'w': 70, 'h': 40, 'text': ['End']}
]
c9_2 = [
    {'points': [(170, 240), (210, 240)]},
    {'points': [(350, 240), (390, 240)]},
    {'points': [(460, 270), (460, 460), (570, 460)]},
    {'points': [(720, 460), (825, 460), (825, 270)]},
    {'points': [(900, 240), (940, 240)]}
]
save_svg("US-09-2_Filter-Order-History.svg", create_svg_flow("US-09-2: Filter Order History by Status", "customer", [("Customer", 130, 360), ("System", 360, 560)], n9_2, c9_2, 1050, 580))

# US-10-1: View Collection (NEW)
n10_1 = [
    {'id': 'start', 'type': 'start', 'x': 100, 'y': 220, 'w': 70, 'h': 40, 'text': ['start']},
    {'id': 'c1', 'type': 'action_both', 'x': 210, 'y': 210, 'w': 140, 'h': 60, 'text': ['เข้าเมนู "My Collection"']},
    {'id': 'sys1', 'type': 'action_system', 'x': 390, 'y': 430, 'w': 150, 'h': 60, 'text': ['ดึงข้อมูลการ์ดสะสม']},
    {'id': 'c2', 'type': 'action_both', 'x': 570, 'y': 210, 'w': 150, 'h': 60, 'text': ['ดูรายการการ์ดของตนเอง']},
    {'id': 'end', 'type': 'end', 'x': 760, 'y': 220, 'w': 70, 'h': 40, 'text': ['End']}
]
save_svg("US-10-1_View-Collection.svg", create_svg_flow("US-10-1: View Personal Collection", "both", [("User (Cust/Seller)", 130, 360), ("System", 360, 560)], n10_1, c9_1, 900, 580))

# US-10-2: Add to Collection (NEW)
n10_2 = [
    {'id': 'start', 'type': 'start', 'x': 100, 'y': 220, 'w': 70, 'h': 40, 'text': ['start']},
    {'id': 'c1', 'type': 'action_both', 'x': 210, 'y': 210, 'w': 140, 'h': 60, 'text': ['ค้นหาจาก TCG API Database']},
    {'id': 'c2', 'type': 'action_both', 'x': 390, 'y': 210, 'w': 140, 'h': 60, 'text': ['กด "Add to Collection"']},
    {'id': 'sys1', 'type': 'action_system', 'x': 570, 'y': 430, 'w': 150, 'h': 60, 'text': ['บันทึกเข้า Collection', 'ใน DB']},
    {'id': 'c3', 'type': 'action_both', 'x': 750, 'y': 210, 'w': 150, 'h': 60, 'text': ['ดูผลการเพิ่มสำเร็จ']},
    {'id': 'end', 'type': 'end', 'x': 940, 'y': 220, 'w': 70, 'h': 40, 'text': ['End']}
]
save_svg("US-10-2_Add-Collection.svg", create_svg_flow("US-10-2: Add Card to Collection", "both", [("User (Cust/Seller)", 130, 360), ("System", 360, 560)], n10_2, c9_2, 1050, 580))

# US-10-3: Remove from Collection (NEW)
n10_3 = [
    {'id': 'start', 'type': 'start', 'x': 100, 'y': 220, 'w': 70, 'h': 40, 'text': ['start']},
    {'id': 'c1', 'type': 'action_both', 'x': 210, 'y': 210, 'w': 140, 'h': 60, 'text': ['เปิดหน้า "My Collection"']},
    {'id': 'c2', 'type': 'action_both', 'x': 390, 'y': 210, 'w': 140, 'h': 60, 'text': ['กด "Remove"']},
    {'id': 'sys1', 'type': 'action_system', 'x': 570, 'y': 430, 'w': 150, 'h': 60, 'text': ['ลบออกจาก Collection']},
    {'id': 'c3', 'type': 'action_both', 'x': 750, 'y': 210, 'w': 150, 'h': 60, 'text': ['รายการอัปเดตใหม่']},
    {'id': 'end', 'type': 'end', 'x': 940, 'y': 220, 'w': 70, 'h': 40, 'text': ['End']}
]
save_svg("US-10-3_Remove-Collection.svg", create_svg_flow("US-10-3: Remove Card from Collection", "both", [("User (Cust/Seller)", 130, 360), ("System", 360, 560)], n10_3, c9_2, 1050, 580))

# US-10-4: Seller Verification (NEW)
n10_4 = [
    {'id': 'start', 'type': 'start', 'x': 100, 'y': 220, 'w': 70, 'h': 40, 'text': ['start']},
    {'id': 'c1', 'type': 'action_customer', 'x': 210, 'y': 210, 'w': 140, 'h': 60, 'text': ['ไปที่หน้า Seller Verification']},
    {'id': 'c2', 'type': 'action_customer', 'x': 390, 'y': 210, 'w': 140, 'h': 60, 'text': ['อัปโหลดเอกสาร / กรอกข้อมูล']},
    {'id': 'sys1', 'type': 'action_system', 'x': 570, 'y': 430, 'w': 150, 'h': 60, 'text': ['ตรวจสอบอัตโนมัติ', '/ บันทึกข้อมูลรอรีวิว']},
    {'id': 'sys2', 'type': 'action_system', 'x': 750, 'y': 430, 'w': 150, 'h': 60, 'text': ['เปลี่ยน Role เป็น', 'Verified Seller (ถ้าผ่าน)']},
    {'id': 'end', 'type': 'end', 'x': 940, 'y': 440, 'w': 70, 'h': 40, 'text': ['End']}
]
c10_4 = [
    {'points': [(170, 240), (210, 240)]},
    {'points': [(350, 240), (390, 240)]},
    {'points': [(460, 270), (460, 460), (570, 460)]},
    {'points': [(720, 460), (750, 460)]},
    {'points': [(900, 460), (940, 460)]}
]
save_svg("US-10-4_Seller-Verification.svg", create_svg_flow("US-10-4: Self-serve Seller Verification", "customer", [("Customer", 130, 360), ("System", 360, 560)], n10_4, c10_4, 1050, 580))

# US-10-5: Stock Reservation Logic (NEW)
n10_5 = [
    {'id': 'start', 'type': 'start', 'x': 100, 'y': 220, 'w': 70, 'h': 40, 'text': ['start']},
    {'id': 'sys1', 'type': 'action_system', 'x': 210, 'y': 430, 'w': 150, 'h': 60, 'text': ['รับ Request จองสต๊อก']},
    {'id': 'd1', 'type': 'decision', 'x': 390, 'y': 420, 'w': 140, 'h': 80, 'text': ['Available >= Request?']},
    
    {'id': 'err1', 'type': 'error', 'x': 390, 'y': 310, 'w': 140, 'h': 50, 'text': ['Error: จองไม่ได้']},
    
    {'id': 'sys2', 'type': 'action_system', 'x': 570, 'y': 430, 'w': 150, 'h': 60, 'text': ['เปลี่ยน Stock เป็น', '"Reserved/Pending"']},
    {'id': 'end', 'type': 'end', 'x': 760, 'y': 440, 'w': 70, 'h': 40, 'text': ['End']}
]
c10_5 = [
    {'points': [(135, 260), (135, 460), (210, 460)]},
    {'points': [(360, 460), (390, 460)]},
    {'points': [(460, 420), (460, 360)], 'label': 'No', 'label_pos': (475, 390)},
    {'points': [(530, 460), (570, 460)], 'label': 'Yes', 'label_pos': (550, 445)},
    {'points': [(720, 460), (760, 460)]}
]
save_svg("US-10-5_Stock-Reservation.svg", create_svg_flow("US-10-5: Stock Reservation Logic", "both", [("Customer (Trigger)", 130, 360), ("System", 360, 560)], n10_5, c10_5, 900, 580))

print("Part 3 generation complete.")
