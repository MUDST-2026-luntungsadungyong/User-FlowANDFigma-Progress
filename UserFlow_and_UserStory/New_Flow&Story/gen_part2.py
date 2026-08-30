from gen_base import create_svg_flow, save_svg

# US-04-1: Place Order from Cart
n4_1 = [
    {'id': 'start', 'type': 'start', 'x': 100, 'y': 220, 'w': 70, 'h': 40, 'text': ['start']},
    {'id': 'c1', 'type': 'action_customer', 'x': 210, 'y': 210, 'w': 140, 'h': 60, 'text': ['เข้าหน้า Shopping Cart']},
    {'id': 'c2', 'type': 'action_customer', 'x': 390, 'y': 210, 'w': 140, 'h': 60, 'text': ['เลือกสินค้าที่ต้องการซื้อ', 'กด "Checkout"']},
    
    {'id': 'sys1', 'type': 'action_system', 'x': 570, 'y': 430, 'w': 150, 'h': 60, 'text': ['ตรวจสอบ Stock']},
    {'id': 'd1', 'type': 'decision', 'x': 760, 'y': 420, 'w': 140, 'h': 80, 'text': ['มีสต๊อกเพียงพอ?']},
    {'id': 'err1', 'type': 'error', 'x': 760, 'y': 310, 'w': 140, 'h': 50, 'text': ['Error สินค้าหมด']},
    
    {'id': 'c3', 'type': 'action_customer', 'x': 940, 'y': 210, 'w': 140, 'h': 60, 'text': ['ดูหน้าสรุป Order', 'และกด "Confirm"']},
    {'id': 'sys2', 'type': 'action_system', 'x': 1120, 'y': 430, 'w': 150, 'h': 60, 'text': ['จองสต๊อกสินค้า', '(US-10-5)']},
    {'id': 'sys3', 'type': 'action_system', 'x': 1300, 'y': 430, 'w': 150, 'h': 60, 'text': ['สร้าง Order (Pending)', 'แสดงข้อมูลติดต่อผู้ขาย']},
    {'id': 'c4', 'type': 'action_customer', 'x': 1490, 'y': 210, 'w': 140, 'h': 60, 'text': ['ดู Order Success', 'นัดหมายโอนเงินเอง']},
    
    {'id': 'end', 'type': 'end', 'x': 1670, 'y': 220, 'w': 70, 'h': 40, 'text': ['End']}
]
c4_1 = [
    {'points': [(170, 240), (210, 240)]},
    {'points': [(350, 240), (390, 240)]},
    {'points': [(460, 270), (460, 460), (570, 460)]},
    {'points': [(720, 460), (760, 460)]},
    {'points': [(830, 460), (940, 460), (940, 270)], 'label': 'Yes', 'label_pos': (875, 445)},
    {'points': [(830, 420), (830, 360)], 'label': 'No', 'label_pos': (845, 390)},
    {'points': [(760, 335), (280, 335), (280, 270)]},
    {'points': [(1010, 270), (1010, 460), (1120, 460)]},
    {'points': [(1270, 460), (1300, 460)]},
    {'points': [(1450, 460), (1560, 460), (1560, 270)]},
    {'points': [(1630, 240), (1670, 240)]}
]
save_svg("US-04-1_Place-Order-Cart.svg", create_svg_flow("US-04-1: Place Order From Cart", "customer", [("Customer", 130, 380), ("System", 380, 560)], n4_1, c4_1, 1800, 580))

# US-04-2: Place Order Direct
n4_2 = [
    {'id': 'start', 'type': 'start', 'x': 100, 'y': 220, 'w': 70, 'h': 40, 'text': ['start']},
    {'id': 'c1', 'type': 'action_customer', 'x': 210, 'y': 210, 'w': 140, 'h': 60, 'text': ['อยู่หน้า Product Detail']},
    {'id': 'c2', 'type': 'action_customer', 'x': 390, 'y': 210, 'w': 140, 'h': 60, 'text': ['กด "Buy Now"']},
    
    {'id': 'sys1', 'type': 'action_system', 'x': 570, 'y': 430, 'w': 150, 'h': 60, 'text': ['ตรวจสอบ Stock']},
    {'id': 'd1', 'type': 'decision', 'x': 760, 'y': 420, 'w': 140, 'h': 80, 'text': ['มีสต๊อกเพียงพอ?']},
    {'id': 'err1', 'type': 'error', 'x': 760, 'y': 310, 'w': 140, 'h': 50, 'text': ['Error สินค้าหมด']},
    
    {'id': 'c3', 'type': 'action_customer', 'x': 940, 'y': 210, 'w': 140, 'h': 60, 'text': ['ดูหน้าสรุป Order', 'และกด "Confirm"']},
    {'id': 'sys2', 'type': 'action_system', 'x': 1120, 'y': 430, 'w': 150, 'h': 60, 'text': ['จองสต๊อกสินค้า', '(US-10-5)']},
    {'id': 'sys3', 'type': 'action_system', 'x': 1300, 'y': 430, 'w': 150, 'h': 60, 'text': ['สร้าง Order (Pending)', 'แสดงข้อมูลติดต่อผู้ขาย']},
    {'id': 'c4', 'type': 'action_customer', 'x': 1490, 'y': 210, 'w': 140, 'h': 60, 'text': ['ดู Order Success', 'นัดหมายโอนเงินเอง']},
    
    {'id': 'end', 'type': 'end', 'x': 1670, 'y': 220, 'w': 70, 'h': 40, 'text': ['End']}
]
save_svg("US-04-2_Place-Order-Direct.svg", create_svg_flow("US-04-2: Place Order Directly (Buy Now)", "customer", [("Customer", 130, 380), ("System", 380, 560)], n4_2, c4_1, 1800, 580))

# US-06-1: Seller Dashboard
n6 = [
    {'id': 'start', 'type': 'start', 'x': 100, 'y': 220, 'w': 70, 'h': 40, 'text': ['start']},
    {'id': 's1', 'type': 'action_seller', 'x': 210, 'y': 210, 'w': 140, 'h': 60, 'text': ['เลือกเมนู', '"Dashboard"']},
    {'id': 'sys1', 'type': 'action_system', 'x': 390, 'y': 430, 'w': 150, 'h': 60, 'text': ['คำนวณ Cost & Profit']},
    {'id': 's2', 'type': 'action_seller', 'x': 570, 'y': 210, 'w': 150, 'h': 60, 'text': ['ดูข้อมูลสถิติ/กำไร', 'ของตัวเอง']},
    {'id': 'end', 'type': 'end', 'x': 760, 'y': 220, 'w': 70, 'h': 40, 'text': ['End']}
]
c6 = [
    {'points': [(170, 240), (210, 240)]},
    {'points': [(280, 270), (280, 460), (390, 460)]},
    {'points': [(540, 460), (645, 460), (645, 270)]},
    {'points': [(720, 240), (760, 240)]}
]
save_svg("US-06-1_Seller-Dashboard.svg", create_svg_flow("US-06-1: Seller Dashboard (Cost & Profit)", "seller", [("Seller", 130, 380), ("System", 380, 560)], n6, c6, 900, 580))

# US-07-1: View Orders (Seller)
n7_1 = [
    {'id': 'start', 'type': 'start', 'x': 100, 'y': 220, 'w': 70, 'h': 40, 'text': ['start']},
    {'id': 's1', 'type': 'action_seller', 'x': 210, 'y': 210, 'w': 140, 'h': 60, 'text': ['เข้าเมนู', '"Order Management"']},
    {'id': 'sys1', 'type': 'action_system', 'x': 390, 'y': 430, 'w': 150, 'h': 60, 'text': ['ดึงออเดอร์ทั้งหมด', '(เฉพาะร้านตัวเอง)']},
    {'id': 's2', 'type': 'action_seller', 'x': 570, 'y': 210, 'w': 150, 'h': 60, 'text': ['ดูรายการออเดอร์', 'กรองตามสถานะได้']},
    {'id': 'end', 'type': 'end', 'x': 760, 'y': 220, 'w': 70, 'h': 40, 'text': ['End']}
]
c7_1 = c6.copy()
save_svg("US-07-1_View-Orders.svg", create_svg_flow("US-07-1: View All Orders (Seller)", "seller", [("Seller", 130, 380), ("System", 380, 560)], n7_1, c7_1, 900, 580))

# US-07-2: Change Order Status
n7_2 = [
    {'id': 'start', 'type': 'start', 'x': 100, 'y': 220, 'w': 70, 'h': 40, 'text': ['start']},
    {'id': 's1', 'type': 'action_seller', 'x': 210, 'y': 210, 'w': 150, 'h': 60, 'text': ['อยู่หน้า Order Management']},
    {'id': 's2', 'type': 'action_seller', 'x': 390, 'y': 210, 'w': 150, 'h': 60, 'text': ['เลือกเปลี่ยนสถานะ', '(Pending -> Fulfilled/Cancelled)']},
    
    {'id': 'sys1', 'type': 'action_system', 'x': 570, 'y': 430, 'w': 160, 'h': 60, 'text': ['อัปเดตสถานะออเดอร์ใน DB']},
    {'id': 'sys2', 'type': 'action_system', 'x': 760, 'y': 430, 'w': 160, 'h': 60, 'text': ['ตัด/คืน สต๊อกในระบบจริง']},
    {'id': 'sys3', 'type': 'action_system', 'x': 950, 'y': 430, 'w': 150, 'h': 60, 'text': ['แจ้งผลอัปเดต']},
    {'id': 'end', 'type': 'end', 'x': 1140, 'y': 440, 'w': 70, 'h': 40, 'text': ['End']}
]
c7_2 = [
    {'points': [(170, 240), (210, 240)]},
    {'points': [(360, 240), (390, 240)]},
    {'points': [(465, 270), (465, 460), (570, 460)]},
    {'points': [(730, 460), (760, 460)]},
    {'points': [(920, 460), (950, 460)]},
    {'points': [(1100, 460), (1140, 460)]}
]
save_svg("US-07-2_Change-Order-Status.svg", create_svg_flow("US-07-2: Change Order Status (Seller)", "seller", [("Seller", 130, 380), ("System", 380, 560)], n7_2, c7_2, 1250, 580))
