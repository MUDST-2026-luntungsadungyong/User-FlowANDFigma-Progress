from gen_base import create_svg_flow, save_svg

# US-01-1: Customer Register & Login
n1 = [
    {'id': 'start', 'type': 'start', 'x': 100, 'y': 220, 'w': 70, 'h': 40, 'text': ['start']},
    {'id': 'c1', 'type': 'action_customer', 'x': 210, 'y': 210, 'w': 140, 'h': 60, 'text': ['เข้าสู่หน้าเว็บไซต์']},
    {'id': 'd1', 'type': 'decision', 'x': 390, 'y': 200, 'w': 140, 'h': 80, 'text': ['มีบัญชีอยู่แล้ว?']},
    
    {'id': 'c2', 'type': 'action_customer', 'x': 570, 'y': 150, 'w': 140, 'h': 60, 'text': ['เข้าหน้า Login']},
    {'id': 'c3', 'type': 'action_customer', 'x': 750, 'y': 150, 'w': 140, 'h': 60, 'text': ['กรอกข้อมูล Login']},
    
    {'id': 'c4', 'type': 'action_customer', 'x': 570, 'y': 280, 'w': 140, 'h': 60, 'text': ['เข้าหน้า Register']},
    {'id': 'c5', 'type': 'action_customer', 'x': 750, 'y': 280, 'w': 140, 'h': 60, 'text': ['กรอกข้อมูลสมัคร']},
    {'id': 'd2', 'type': 'decision', 'x': 930, 'y': 270, 'w': 140, 'h': 80, 'text': ['ข้อมูลครบถ้วน?']},
    {'id': 'err1', 'type': 'error', 'x': 930, 'y': 180, 'w': 140, 'h': 50, 'text': ['แจ้งกรอกไม่ครบ']},
    {'id': 'sys1', 'type': 'action_system', 'x': 930, 'y': 430, 'w': 140, 'h': 60, 'text': ['สร้างบัญชีสำเร็จ']},
    
    {'id': 'd3', 'type': 'decision', 'x': 1110, 'y': 420, 'w': 140, 'h': 80, 'text': ['ตรวจสอบข้อมูล', '(Auth)']},
    {'id': 'err2', 'type': 'error', 'x': 1110, 'y': 310, 'w': 140, 'h': 50, 'text': ['Auth Failed']},
    {'id': 'sys2', 'type': 'action_system', 'x': 1300, 'y': 430, 'w': 140, 'h': 60, 'text': ['เข้าสู่ระบบสำเร็จ']},
    
    {'id': 'end', 'type': 'end', 'x': 1480, 'y': 440, 'w': 70, 'h': 40, 'text': ['End']}
]
c1 = [
    {'points': [(170, 240), (210, 240)]},
    {'points': [(350, 240), (390, 240)]},
    {'points': [(460, 200), (460, 180), (570, 180)], 'label': 'Yes', 'label_pos': (515, 165)},
    {'points': [(460, 280), (460, 310), (570, 310)], 'label': 'No', 'label_pos': (515, 295)},
    {'points': [(710, 180), (750, 180)]},
    {'points': [(890, 180), (1050, 180), (1050, 460), (1110, 460)]},
    {'points': [(710, 310), (750, 310)]},
    {'points': [(890, 310), (930, 310)]},
    {'points': [(1000, 270), (1000, 205), (1070, 205)]},
    {'points': [(1000, 350), (1000, 460), (930, 460)], 'label': 'Yes', 'label_pos': (1015, 380)},
    {'points': [(1180, 420), (1180, 335), (1250, 335)], 'label': 'No', 'label_pos': (1195, 380)},
    {'points': [(1250, 460), (1300, 460)], 'label': 'Yes', 'label_pos': (1275, 445)},
    {'points': [(1440, 460), (1480, 460)]}
]
save_svg("US-01-1_Register-Login.svg", create_svg_flow("US-01-1: Customer Register & Login", "customer", [("Customer", 130, 380), ("System", 380, 560)], n1, c1, 1600, 580))

# US-02-1: Browse Cards
n2 = [
    {'id': 'start', 'type': 'start', 'x': 100, 'y': 220, 'w': 70, 'h': 40, 'text': ['start']},
    {'id': 'c1', 'type': 'action_customer', 'x': 210, 'y': 210, 'w': 140, 'h': 60, 'text': ['เข้าหน้า Home']},
    {'id': 'c2', 'type': 'action_customer', 'x': 390, 'y': 210, 'w': 140, 'h': 60, 'text': ['เลือกเมนู Browse Cards']},
    {'id': 'sys1', 'type': 'action_system', 'x': 385, 'y': 430, 'w': 150, 'h': 60, 'text': ['ดึงข้อมูล Card Catalog']},
    {'id': 'c3', 'type': 'action_customer', 'x': 570, 'y': 210, 'w': 140, 'h': 60, 'text': ['ค้นหาและ Filter']},
    {'id': 'sys2', 'type': 'action_system', 'x': 565, 'y': 430, 'w': 150, 'h': 60, 'text': ['แสดงผลลัพธ์การค้นหา']},
    {'id': 'end', 'type': 'end', 'x': 770, 'y': 440, 'w': 70, 'h': 40, 'text': ['End']}
]
c2 = [
    {'points': [(170, 240), (210, 240)]},
    {'points': [(350, 240), (390, 240)]},
    {'points': [(460, 270), (460, 430)]},
    {'points': [(535, 460), (550, 460), (550, 240), (570, 240)]},
    {'points': [(640, 270), (640, 430)]},
    {'points': [(715, 460), (770, 460)]}
]
save_svg("US-02-1_Browse-Cards.svg", create_svg_flow("US-02-1: Browse TCG Cards with Filters", "customer", [("Customer", 130, 360), ("System", 360, 560)], n2, c2, 900, 580))

# US-03-1: Add to Cart
n3_1 = [
    {'id': 'start', 'type': 'start', 'x': 100, 'y': 220, 'w': 70, 'h': 40, 'text': ['start']},
    {'id': 'c1', 'type': 'action_customer', 'x': 210, 'y': 210, 'w': 140, 'h': 60, 'text': ['ดูรายละเอียดสินค้า']},
    {'id': 'c2', 'type': 'action_customer', 'x': 390, 'y': 210, 'w': 140, 'h': 60, 'text': ['กด "Add to Cart"']},
    {'id': 'sys1', 'type': 'action_system', 'x': 570, 'y': 430, 'w': 150, 'h': 60, 'text': ['เพิ่มสินค้าลง Session/DB', 'อัปเดต Cart']},
    {'id': 'end', 'type': 'end', 'x': 770, 'y': 440, 'w': 70, 'h': 40, 'text': ['End']}
]
c3_1 = [
    {'points': [(170, 240), (210, 240)]},
    {'points': [(350, 240), (390, 240)]},
    {'points': [(460, 270), (460, 460), (570, 460)]},
    {'points': [(720, 460), (770, 460)]}
]
save_svg("US-03-1_Add-Cart.svg", create_svg_flow("US-03-1: Add Cards to Cart", "customer", [("Customer", 130, 360), ("System", 360, 560)], n3_1, c3_1, 900, 580))

# US-03-2: Delete Cart
n3_2 = [
    {'id': 'start', 'type': 'start', 'x': 100, 'y': 220, 'w': 70, 'h': 40, 'text': ['start']},
    {'id': 'c1', 'type': 'action_customer', 'x': 210, 'y': 210, 'w': 140, 'h': 60, 'text': ['เปิดหน้า Shopping Cart']},
    {'id': 'c2', 'type': 'action_customer', 'x': 390, 'y': 210, 'w': 140, 'h': 60, 'text': ['กดลบสินค้า']},
    {'id': 'sys1', 'type': 'action_system', 'x': 570, 'y': 430, 'w': 150, 'h': 60, 'text': ['ลบสินค้าออกจาก Cart']},
    {'id': 'end', 'type': 'end', 'x': 770, 'y': 440, 'w': 70, 'h': 40, 'text': ['End']}
]
c3_2 = c3_1.copy()
save_svg("US-03-2_Delete-Cart.svg", create_svg_flow("US-03-2: Delete Cards from Cart", "customer", [("Customer", 130, 360), ("System", 360, 560)], n3_2, c3_2, 900, 580))

# US-03-3: Decrease Cart
n3_3 = [
    {'id': 'start', 'type': 'start', 'x': 100, 'y': 220, 'w': 70, 'h': 40, 'text': ['start']},
    {'id': 'c1', 'type': 'action_customer', 'x': 210, 'y': 210, 'w': 140, 'h': 60, 'text': ['เปิดหน้า Shopping Cart']},
    {'id': 'c2', 'type': 'action_customer', 'x': 390, 'y': 210, 'w': 140, 'h': 60, 'text': ['กดลดจำนวน (-)']},
    {'id': 'sys1', 'type': 'action_system', 'x': 570, 'y': 430, 'w': 150, 'h': 60, 'text': ['ลดจำนวนใน Cart', 'หากเหลือ 0 ให้ลบออก']},
    {'id': 'end', 'type': 'end', 'x': 770, 'y': 440, 'w': 70, 'h': 40, 'text': ['End']}
]
save_svg("US-03-3_Decrease-Cart.svg", create_svg_flow("US-03-3: Decrease Amount in Cart", "customer", [("Customer", 130, 360), ("System", 360, 560)], n3_3, c3_1, 900, 580))

# US-03-4: Increase Cart
n3_4 = [
    {'id': 'start', 'type': 'start', 'x': 100, 'y': 220, 'w': 70, 'h': 40, 'text': ['start']},
    {'id': 'c1', 'type': 'action_customer', 'x': 210, 'y': 210, 'w': 140, 'h': 60, 'text': ['เปิดหน้า Shopping Cart']},
    {'id': 'c2', 'type': 'action_customer', 'x': 390, 'y': 210, 'w': 140, 'h': 60, 'text': ['กดเพิ่มจำนวน (+)']},
    {'id': 'sys1', 'type': 'action_system', 'x': 570, 'y': 430, 'w': 150, 'h': 60, 'text': ['เพิ่มจำนวนใน Cart']},
    {'id': 'end', 'type': 'end', 'x': 770, 'y': 440, 'w': 70, 'h': 40, 'text': ['End']}
]
save_svg("US-03-4_Increase-Cart.svg", create_svg_flow("US-03-4: Increase Amount in Cart", "customer", [("Customer", 130, 360), ("System", 360, 560)], n3_4, c3_1, 900, 580))
