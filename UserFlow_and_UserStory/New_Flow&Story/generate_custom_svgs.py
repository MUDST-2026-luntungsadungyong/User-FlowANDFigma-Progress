import os
import html
import xml.etree.ElementTree as ET

# Helper to create SVG XML matching Old_User_Flow.pdf styling
def create_svg_flow(title, actor_type, lanes, nodes, connections, width=1600, height=800):
    styles = """
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Sarabun:wght@400;600;700&amp;display=swap');
            text {
                font-family: 'Sarabun', 'Segoe UI', Tahoma, sans-serif;
                font-size: 13px;
                fill: #1e293b;
                text-anchor: middle;
                dominant-baseline: central;
            }
            .title { font-size: 20px; font-weight: 700; fill: #0f172a; text-anchor: start; }
            .legend-text { font-size: 13px; fill: #475569; text-anchor: start; }
            .lane-label { font-size: 15px; font-weight: 600; fill: #64748b; }
            .edge-label { font-size: 12px; font-weight: 600; fill: #475569; }
            
            .node-start-end { fill: #86efac; stroke: #22c55e; stroke-width: 1.5; }
            .node-customer { fill: #d8b4fe; stroke: #a855f7; stroke-width: 1.5; }
            .node-seller { fill: #fef08a; stroke: #eab308; stroke-width: 1.5; }
            .node-system { fill: #fed7aa; stroke: #f97316; stroke-width: 1.5; }
            .node-error { fill: #fca5a5; stroke: #ef4444; stroke-width: 1.5; }
            .node-decision { fill: #ffffff; stroke: #64748b; stroke-width: 1.5; }
            
            .lane-line { stroke: #cbd5e1; stroke-width: 1.5; stroke-dasharray: 6 4; }
            .flow-line { stroke: #64748b; stroke-width: 1.8; fill: none; }
        </style>
    """
    
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">']
    svg.append('<defs>')
    svg.append(styles)
    # Marker for arrowheads
    svg.append('''
        <marker id="arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
            <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#64748b" />
        </marker>
        <marker id="circle-start" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6">
            <circle cx="5" cy="5" r="4" fill="#64748b" />
        </marker>
    ''')
    svg.append('</defs>')
    
    # Canvas background
    svg.append(f'<rect width="{width}" height="{height}" fill="#ffffff" />')
    
    # Header / Title
    svg.append(f'<text x="40" y="45" class="title">{html.escape(title)}</text>')
    
    # Legend in top left (matching Old_User_Flow)
    lx = 40
    ly = 85
    if actor_type in ['customer', 'both']:
        svg.append(f'<circle cx="{lx}" cy="{ly}" r="9" fill="#d8b4fe" />')
        svg.append(f'<text x="{lx+18}" y="{ly}" class="legend-text">Customer actions</text>')
        lx += 160
    if actor_type in ['seller', 'both']:
        svg.append(f'<circle cx="{lx}" cy="{ly}" r="9" fill="#fef08a" />')
        svg.append(f'<text x="{lx+18}" y="{ly}" class="legend-text">Seller actions</text>')
        lx += 140
    
    svg.append(f'<circle cx="{lx}" cy="{ly}" r="9" fill="#1e293b" />')
    svg.append(f'<text x="{lx+18}" y="{ly}" class="legend-text">Decisions</text>')
    lx += 110
    
    svg.append(f'<circle cx="{lx}" cy="{ly}" r="9" fill="#fed7aa" />')
    svg.append(f'<text x="{lx+18}" y="{ly}" class="legend-text">System actions</text>')
    lx += 140
    
    svg.append(f'<circle cx="{lx}" cy="{ly}" r="9" fill="#fca5a5" />')
    svg.append(f'<text x="{lx+18}" y="{ly}" class="legend-text">Error</text>')
    
    # Swimlane divider lines & labels
    for idx, lane in enumerate(lanes):
        name, y_start, y_end = lane
        mid_y = (y_start + y_end) // 2
        # Vertical text label on the left margin
        svg.append(f'<text x="45" y="{mid_y}" class="lane-label" transform="rotate(-90 45 {mid_y})">{html.escape(name)}</text>')
        
        # Lane divider line (if not last)
        if idx < len(lanes) - 1:
            svg.append(f'<line x1="80" y1="{y_end}" x2="{width-40}" y2="{y_end}" class="lane-line" />')
            
    # Draw connections first (under nodes)
    for conn in connections:
        pts = conn.get('points', [])
        p_str = " ".join([f"{x},{y}" for x, y in pts])
        svg.append(f'<polyline points="{p_str}" class="flow-line" marker-end="url(#arrow)" />')
        
        if 'label' in conn and 'label_pos' in conn:
            lx, ly = conn['label_pos']
            # Small background for label
            txt = conn['label']
            tw = len(txt) * 8 + 12
            svg.append(f'<rect x="{lx - tw//2}" y="{ly - 10}" width="{tw}" height="20" fill="#ffffff" rx="4" />')
            svg.append(f'<text x="{lx}" y="{ly}" class="edge-label">{html.escape(txt)}</text>')

    # Draw nodes
    for node in nodes:
        ntype = node['type']
        x, y, w, h = node['x'], node['y'], node['w'], node['h']
        lines = node['text']
        
        if ntype in ['start', 'end']:
            svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h//2}" ry="{h//2}" class="node-start-end" />')
        elif ntype == 'action_customer':
            svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" ry="8" class="node-customer" />')
        elif ntype == 'action_seller':
            svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" ry="8" class="node-seller" />')
        elif ntype == 'action_system':
            svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" ry="8" class="node-system" />')
        elif ntype == 'error':
            svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" ry="8" class="node-error" />')
        elif ntype == 'decision':
            # Diamond polygon
            pts = f"{x + w//2},{y} {x + w},{y + h//2} {x + w//2},{y + h} {x},{y + h//2}"
            svg.append(f'<polygon points="{pts}" class="node-decision" />')
            
        # Draw node text
        line_height = 16
        total_text_h = len(lines) * line_height
        start_text_y = y + (h - total_text_h) // 2 + line_height // 2
        for i, line in enumerate(lines):
            cur_y = start_text_y + i * line_height
            svg.append(f'<text x="{x + w//2}" y="{cur_y}">{html.escape(line)}</text>')
            
    svg.append('</svg>')
    res = "\n".join(svg)
    
    # Validate XML
    try:
        ET.fromstring(res)
    except Exception as e:
        print(f"ERROR: XML validation failed for {title}: {e}")
        raise e
        
    return res

output_dir = r"C:\Devops_NEW\UserFlow_and_UserStory\New_Flow&Story"

# -------------------------------------------------------------
# 1. US-04: Place Order System
# -------------------------------------------------------------
us04_nodes = [
    {'id': 'start', 'type': 'start', 'x': 100, 'y': 220, 'w': 70, 'h': 40, 'text': ['start']},
    {'id': 'c1', 'type': 'action_customer', 'x': 210, 'y': 210, 'w': 140, 'h': 60, 'text': ['ลูกค้าเปิดหน้า', 'Shopping Cart']},
    {'id': 'c2', 'type': 'action_customer', 'x': 390, 'y': 210, 'w': 140, 'h': 60, 'text': ['กดปุ่ม', '"Checkout"']},
    {'id': 'c3', 'type': 'action_customer', 'x': 570, 'y': 210, 'w': 150, 'h': 60, 'text': ['ตรวจสอบสรุปรายการ', 'และข้อมูลผู้ขาย']},
    {'id': 'c4', 'type': 'action_customer', 'x': 760, 'y': 210, 'w': 140, 'h': 60, 'text': ['กดปุ่ม', '"Confirm Order"']},
    
    {'id': 's1', 'type': 'decision', 'x': 940, 'y': 480, 'w': 160, 'h': 80, 'text': ['มีสต๊อกว่างพอ?', '(OnHand-Reserved)']},
    {'id': 's_err', 'type': 'error', 'x': 940, 'y': 360, 'w': 160, 'h': 50, 'text': ['แจ้งเตือนสต๊อกไม่พอ']},
    {'id': 's2', 'type': 'action_system', 'x': 1140, 'y': 490, 'w': 150, 'h': 60, 'text': ['จองสต๊อกสินค้า', '(เพิ่ม Reserved)']},
    {'id': 's3', 'type': 'action_system', 'x': 1330, 'y': 490, 'w': 150, 'h': 60, 'text': ['สร้าง Order', 'สถานะ "Pending"']},
    
    {'id': 'c5', 'type': 'action_customer', 'x': 1330, 'y': 210, 'w': 150, 'h': 60, 'text': ['แสดงหน้าสำเร็จพร้อม', 'ช่องทางติดต่อ Seller']},
    {'id': 'end', 'type': 'end', 'x': 1520, 'y': 220, 'w': 70, 'h': 40, 'text': ['End']}
]

us04_conns = [
    {'points': [(170, 240), (210, 240)]},
    {'points': [(350, 240), (390, 240)]},
    {'points': [(530, 240), (570, 240)]},
    {'points': [(720, 240), (760, 240)]},
    {'points': [(830, 270), (830, 520), (940, 520)]},
    {'points': [(1020, 480), (1020, 410)], 'label': 'No', 'label_pos': (1035, 445)},
    {'points': [(940, 385), (645, 385), (645, 270)]},
    {'points': [(1100, 520), (1140, 520)], 'label': 'Yes', 'label_pos': (1120, 505)},
    {'points': [(1290, 520), (1330, 520)]},
    {'points': [(1405, 490), (1405, 270)]},
    {'points': [(1480, 240), (1520, 240)]}
]

svg_04 = create_svg_flow(
    "US-04: Place Order System (Checkout & Stock Reservation)",
    "customer",
    [("Customer", 130, 390), ("System", 390, 650)],
    us04_nodes, us04_conns, width=1640, height=680
)
with open(os.path.join(output_dir, "US-04-Place-Order.svg"), "w", encoding="utf-8") as f:
    f.write(svg_04)

# -------------------------------------------------------------
# 2. US-05: CRUD Inventory Management
# -------------------------------------------------------------
us05_nodes = [
    {'id': 'start', 'type': 'start', 'x': 100, 'y': 220, 'w': 70, 'h': 40, 'text': ['start']},
    {'id': 'sel1', 'type': 'action_seller', 'x': 210, 'y': 210, 'w': 140, 'h': 60, 'text': ['Seller เข้าหน้า', '"My Inventory"']},
    {'id': 'dec1', 'type': 'decision', 'x': 390, 'y': 200, 'w': 140, 'h': 80, 'text': ['เลือกคำสั่ง']},
    
    # Path Add
    {'id': 'sel_add', 'type': 'action_seller', 'x': 570, 'y': 150, 'w': 150, 'h': 55, 'text': ['เลือกการ์ดจาก', 'My Collection']},
    {'id': 'sel_add2', 'type': 'action_seller', 'x': 750, 'y': 150, 'w': 140, 'h': 55, 'text': ['กำหนดราคาขาย', 'และจำนวนสต็อก']},
    {'id': 'sys_add', 'type': 'action_system', 'x': 930, 'y': 440, 'w': 150, 'h': 55, 'text': ['บันทึก Product', '(owner = sellerId)']},
    
    # Path Edit
    {'id': 'sel_edit', 'type': 'action_seller', 'x': 660, 'y': 230, 'w': 150, 'h': 55, 'text': ['แก้ไขราคา / สต็อก /', 'รายละเอียดสินค้า']},
    {'id': 'sys_edit', 'type': 'action_system', 'x': 930, 'y': 510, 'w': 150, 'h': 55, 'text': ['อัปเดตข้อมูลสินค้า']},
    
    # Path Delete
    {'id': 'sel_del', 'type': 'action_seller', 'x': 570, 'y': 310, 'w': 140, 'h': 55, 'text': ['กดยืนยันการลบ']},
    {'id': 'sys_chk_del', 'type': 'decision', 'x': 750, 'y': 570, 'w': 140, 'h': 80, 'text': ['มีใน Order', 'Pending?']},
    {'id': 'sys_err_del', 'type': 'error', 'x': 750, 'y': 470, 'w': 140, 'h': 50, 'text': ['แจ้งเตือนไม่สามารถลบ']},
    {'id': 'sys_del', 'type': 'action_system', 'x': 930, 'y': 585, 'w': 150, 'h': 55, 'text': ['ลบ / Archive', 'สินค้าออกจากร้าน']},
    
    # Path Hide/Show
    {'id': 'sel_tog', 'type': 'action_seller', 'x': 570, 'y': 380, 'w': 140, 'h': 50, 'text': ['กด Toggle', 'Show/Hide']},
    {'id': 'sys_tog', 'type': 'action_system', 'x': 930, 'y': 660, 'w': 150, 'h': 50, 'text': ['เปลี่ยนสถานะการมองเห็น']},
    
    {'id': 'sys_res', 'type': 'action_system', 'x': 1140, 'y': 530, 'w': 150, 'h': 60, 'text': ['รีเฟรชหน้ารายการ', 'สินค้าของ Seller']},
    {'id': 'end', 'type': 'end', 'x': 1330, 'y': 540, 'w': 70, 'h': 40, 'text': ['End']}
]

us05_conns = [
    {'points': [(170, 240), (210, 240)]},
    {'points': [(350, 240), (390, 240)]},
    # Add branch
    {'points': [(460, 200), (460, 175), (570, 175)], 'label': 'Add', 'label_pos': (510, 160)},
    {'points': [(720, 175), (750, 175)]},
    {'points': [(890, 175), (1005, 175), (1005, 440)]},
    # Edit branch
    {'points': [(530, 240), (530, 255), (660, 255)], 'label': 'Edit', 'label_pos': (580, 240)},
    {'points': [(810, 255), (1005, 255), (1005, 510)]},
    # Delete branch
    {'points': [(460, 280), (460, 335), (570, 335)], 'label': 'Delete', 'label_pos': (510, 320)},
    {'points': [(710, 335), (820, 335), (820, 570)]},
    {'points': [(820, 570), (820, 520)], 'label': 'Yes', 'label_pos': (835, 545)},
    {'points': [(890, 610), (930, 610)], 'label': 'No', 'label_pos': (910, 595)},
    # Toggle branch
    {'points': [(420, 270), (420, 405), (570, 405)], 'label': 'Hide/Show', 'label_pos': (480, 390)},
    {'points': [(710, 405), (1005, 405), (1005, 660)]},
    # Converge
    {'points': [(1080, 467), (1110, 467), (1110, 560), (1140, 560)]},
    {'points': [(1080, 537), (1140, 537)]},
    {'points': [(1080, 612), (1110, 612), (1110, 560), (1140, 560)]},
    {'points': [(1080, 685), (1110, 685), (1110, 560), (1140, 560)]},
    {'points': [(1290, 560), (1330, 560)]}
]

svg_05 = create_svg_flow(
    "US-05: CRUD Inventory Management System (Seller Self-Management)",
    "seller",
    [("Seller", 130, 430), ("System", 430, 740)],
    us05_nodes, us05_conns, width=1450, height=760
)
with open(os.path.join(output_dir, "US-05-CRUD-Inventory.svg"), "w", encoding="utf-8") as f:
    f.write(svg_05)

# -------------------------------------------------------------
# 3. US-06: Seller Dashboard (Cost & Profit)
# -------------------------------------------------------------
us06_nodes = [
    {'id': 'start', 'type': 'start', 'x': 100, 'y': 220, 'w': 70, 'h': 40, 'text': ['start']},
    {'id': 's1', 'type': 'action_seller', 'x': 210, 'y': 210, 'w': 150, 'h': 60, 'text': ['เปิดหน้า', 'Seller Dashboard']},
    {'id': 's2', 'type': 'action_seller', 'x': 400, 'y': 210, 'w': 160, 'h': 60, 'text': ['ระบุ/แก้ไข "ต้นทุนการ์ด"', '(Cost per Card)']},
    {'id': 's3', 'type': 'action_seller', 'x': 600, 'y': 210, 'w': 140, 'h': 60, 'text': ['กดปุ่ม "บันทึกต้นทุน"']},
    
    {'id': 'sys1', 'type': 'action_system', 'x': 600, 'y': 440, 'w': 150, 'h': 60, 'text': ['บันทึก Cost ลงฐานข้อมูล', 'เฉพาะของ Seller']},
    {'id': 'sys2', 'type': 'action_system', 'x': 800, 'y': 440, 'w': 170, 'h': 60, 'text': ['คำนวณกำไรประมาณการ', '(Price - Cost) x Qty']},
    
    {'id': 's4', 'type': 'action_seller', 'x': 800, 'y': 210, 'w': 170, 'h': 60, 'text': ['ดูตัวเลขสรุปยอดขาย', 'และ Estimated Profit']},
    {'id': 'end', 'type': 'end', 'x': 1020, 'y': 220, 'w': 70, 'h': 40, 'text': ['End']}
]

us06_conns = [
    {'points': [(170, 240), (210, 240)]},
    {'points': [(360, 240), (400, 240)]},
    {'points': [(560, 240), (600, 240)]},
    {'points': [(670, 270), (670, 440)]},
    {'points': [(750, 470), (800, 470)]},
    {'points': [(885, 440), (885, 270)]},
    {'points': [(970, 240), (1020, 240)]}
]

svg_06 = create_svg_flow(
    "US-06: Seller Dashboard (Estimated Cost & Profit Calculator)",
    "seller",
    [("Seller", 130, 360), ("System", 360, 580)],
    us06_nodes, us06_conns, width=1150, height=600
)
with open(os.path.join(output_dir, "US-06-Seller-Dashboard.svg"), "w", encoding="utf-8") as f:
    f.write(svg_06)

# -------------------------------------------------------------
# 4. US-07: Order Management (Fulfilled / Cancelled)
# -------------------------------------------------------------
us07_nodes = [
    {'id': 'start', 'type': 'start', 'x': 100, 'y': 220, 'w': 70, 'h': 40, 'text': ['start']},
    {'id': 's1', 'type': 'action_seller', 'x': 210, 'y': 210, 'w': 140, 'h': 60, 'text': ['เปิดหน้ารายการ', '"My Incoming Orders"']},
    {'id': 's2', 'type': 'action_seller', 'x': 390, 'y': 210, 'w': 140, 'h': 60, 'text': ['เลือก Order ที่สถานะ', 'เป็น "Pending"']},
    {'id': 'dec1', 'type': 'decision', 'x': 570, 'y': 200, 'w': 140, 'h': 80, 'text': ['เปลี่ยนสถานะ?']},
    
    # Fulfilled branch
    {'id': 's_ful', 'type': 'action_seller', 'x': 750, 'y': 150, 'w': 150, 'h': 55, 'text': ['กดปุ่ม "Fulfilled"', '(ซื้อขายสำเร็จ)']},
    {'id': 'sys_ful', 'type': 'action_system', 'x': 940, 'y': 410, 'w': 170, 'h': 65, 'text': ['ตัดสต๊อกจริง (OnHand - n)', 'ลบ Reserved และปรับ', 'สถานะเป็น Fulfilled']},
    
    # Cancelled branch
    {'id': 's_can', 'type': 'action_seller', 'x': 750, 'y': 260, 'w': 150, 'h': 55, 'text': ['กดปุ่ม "Cancelled"', '(ยกเลิกคำสั่งซื้อ)']},
    {'id': 'sys_can', 'type': 'action_system', 'x': 940, 'y': 510, 'w': 170, 'h': 65, 'text': ['คืนสต๊อกคงเหลือ', '(ลด Reserved)', 'ปรับสถานะ Cancelled']},
    
    {'id': 'sys_done', 'type': 'action_system', 'x': 1160, 'y': 465, 'w': 140, 'h': 60, 'text': ['อัปเดตหน้าแสดงผล', 'Order สำเร็จ']},
    {'id': 'end', 'type': 'end', 'x': 1340, 'y': 475, 'w': 70, 'h': 40, 'text': ['End']}
]

us07_conns = [
    {'points': [(170, 240), (210, 240)]},
    {'points': [(350, 240), (390, 240)]},
    {'points': [(530, 240), (570, 240)]},
    {'points': [(640, 200), (640, 177), (750, 177)], 'label': 'Fulfilled', 'label_pos': (680, 160)},
    {'points': [(640, 280), (640, 287), (750, 287)], 'label': 'Cancelled', 'label_pos': (680, 270)},
    {'points': [(900, 177), (1025, 177), (1025, 410)]},
    {'points': [(900, 287), (1025, 287), (1025, 510)]},
    {'points': [(1110, 442), (1135, 442), (1135, 495), (1160, 495)]},
    {'points': [(1110, 542), (1135, 542), (1135, 495), (1160, 495)]},
    {'points': [(1300, 495), (1340, 495)]}
]

svg_07 = create_svg_flow(
    "US-07: Order Management System (Fulfilled & Cancelled Without Shipping)",
    "seller",
    [("Seller", 130, 360), ("System", 360, 620)],
    us07_nodes, us07_conns, width=1460, height=640
)
with open(os.path.join(output_dir, "US-07-Order-Management.svg"), "w", encoding="utf-8") as f:
    f.write(svg_07)

# -------------------------------------------------------------
# 5. US-08: User Profile (Contact Info)
# -------------------------------------------------------------
us08_nodes = [
    {'id': 'start', 'type': 'start', 'x': 100, 'y': 220, 'w': 70, 'h': 40, 'text': ['start']},
    {'id': 'c1', 'type': 'action_customer', 'x': 210, 'y': 210, 'w': 150, 'h': 60, 'text': ['ผู้ใช้เข้าสู่หน้า', '"Profile Settings"']},
    {'id': 'c2', 'type': 'action_customer', 'x': 400, 'y': 210, 'w': 160, 'h': 60, 'text': ['กรอก/แก้ไข "ข้อมูลติดต่อ"', '(Phone, Line, FB)']},
    {'id': 'c3', 'type': 'action_customer', 'x': 600, 'y': 210, 'w': 140, 'h': 60, 'text': ['กดปุ่ม "Save"']},
    
    {'id': 'dec1', 'type': 'decision', 'x': 780, 'y': 420, 'w': 140, 'h': 80, 'text': ['ข้อมูลถูกต้อง?']},
    {'id': 'err1', 'type': 'error', 'x': 780, 'y': 310, 'w': 140, 'h': 50, 'text': ['แจ้งเตือนรูปแบบผิด']},
    {'id': 'sys1', 'type': 'action_system', 'x': 970, 'y': 430, 'w': 150, 'h': 60, 'text': ['บันทึก Contact Info', 'ลงในฐานข้อมูล']},
    
    {'id': 'c4', 'type': 'action_customer', 'x': 970, 'y': 210, 'w': 150, 'h': 60, 'text': ['แสดงข้อความ', '"บันทึกข้อมูลสำเร็จ"']},
    {'id': 'end', 'type': 'end', 'x': 1160, 'y': 220, 'w': 70, 'h': 40, 'text': ['End']}
]

us08_conns = [
    {'points': [(170, 240), (210, 240)]},
    {'points': [(360, 240), (400, 240)]},
    {'points': [(560, 240), (600, 240)]},
    {'points': [(740, 240), (850, 240), (850, 420)]},
    {'points': [(850, 420), (850, 360)], 'label': 'No', 'label_pos': (865, 390)},
    {'points': [(780, 335), (480, 335), (480, 270)]},
    {'points': [(920, 460), (970, 460)], 'label': 'Yes', 'label_pos': (945, 445)},
    {'points': [(1045, 430), (1045, 270)]},
    {'points': [(1120, 240), (1160, 240)]}
]

svg_08 = create_svg_flow(
    "US-08: User Profile System (Contact Information Management)",
    "customer",
    [("Customer", 130, 360), ("System", 360, 560)],
    us08_nodes, us08_conns, width=1280, height=580
)
with open(os.path.join(output_dir, "US-08-User-Profile.svg"), "w", encoding="utf-8") as f:
    f.write(svg_08)

# -------------------------------------------------------------
# 6. US-NEW-1: Collection Management
# -------------------------------------------------------------
usnew1_nodes = [
    {'id': 'start', 'type': 'start', 'x': 100, 'y': 220, 'w': 70, 'h': 40, 'text': ['start']},
    {'id': 'c1', 'type': 'action_customer', 'x': 210, 'y': 210, 'w': 140, 'h': 60, 'text': ['ผู้ใช้เข้าสู่หน้า', '"My Collection"']},
    {'id': 'dec1', 'type': 'decision', 'x': 390, 'y': 200, 'w': 140, 'h': 80, 'text': ['เลือกคำสั่ง']},
    
    # Add Card
    {'id': 'c_add', 'type': 'action_customer', 'x': 570, 'y': 150, 'w': 150, 'h': 55, 'text': ['ค้นหาการ์ดจาก Catalog']},
    {'id': 'c_add2', 'type': 'action_customer', 'x': 750, 'y': 150, 'w': 150, 'h': 55, 'text': ['ระบุสภาพ/ภาษา/จำนวน']},
    {'id': 'sys_add', 'type': 'action_system', 'x': 940, 'y': 410, 'w': 150, 'h': 55, 'text': ['บันทึกลง Collection']},
    
    # Edit / Delete Card
    {'id': 'c_mod', 'type': 'action_customer', 'x': 660, 'y': 260, 'w': 150, 'h': 55, 'text': ['แก้ไขสภาพ/ลบการ์ด']},
    {'id': 'sys_mod', 'type': 'action_system', 'x': 940, 'y': 490, 'w': 150, 'h': 55, 'text': ['อัปเดตข้อมูล Collection']},
    
    {'id': 'c_res', 'type': 'action_customer', 'x': 1130, 'y': 210, 'w': 150, 'h': 60, 'text': ['แสดงสมุดสะสมการ์ด', 'ส่วนตัว (Private)']},
    {'id': 'end', 'type': 'end', 'x': 1320, 'y': 220, 'w': 70, 'h': 40, 'text': ['End']}
]

usnew1_conns = [
    {'points': [(170, 240), (210, 240)]},
    {'points': [(350, 240), (390, 240)]},
    {'points': [(460, 200), (460, 177), (570, 177)], 'label': 'Add', 'label_pos': (510, 160)},
    {'points': [(720, 177), (750, 177)]},
    {'points': [(900, 177), (1015, 177), (1015, 410)]},
    {'points': [(460, 280), (460, 287), (660, 287)], 'label': 'Edit/Delete', 'label_pos': (560, 270)},
    {'points': [(810, 287), (1015, 287), (1015, 490)]},
    {'points': [(1090, 437), (1110, 437), (1110, 240), (1130, 240)]},
    {'points': [(1090, 517), (1110, 517), (1110, 240), (1130, 240)]},
    {'points': [(1280, 240), (1320, 240)]}
]

svg_new1 = create_svg_flow(
    "US-NEW-1: Collection Management System (Personal Binder)",
    "customer",
    [("Customer / User", 130, 360), ("System", 360, 580)],
    usnew1_nodes, usnew1_conns, width=1440, height=600
)
with open(os.path.join(output_dir, "US-NEW-1-Collection.svg"), "w", encoding="utf-8") as f:
    f.write(svg_new1)

# -------------------------------------------------------------
# 7. US-NEW-2: Self-serve Seller Verification
# -------------------------------------------------------------
usnew2_nodes = [
    {'id': 'start', 'type': 'start', 'x': 100, 'y': 220, 'w': 70, 'h': 40, 'text': ['start']},
    {'id': 'c1', 'type': 'action_customer', 'x': 210, 'y': 210, 'w': 150, 'h': 60, 'text': ['ลูกค้าเปิดหน้า', '"Become a Seller"']},
    {'id': 'c2', 'type': 'action_customer', 'x': 400, 'y': 210, 'w': 160, 'h': 60, 'text': ['กรอกชื่อร้านค้าและ', 'ข้อมูลติดต่อยืนยันตัวตน']},
    {'id': 'c3', 'type': 'action_customer', 'x': 600, 'y': 210, 'w': 140, 'h': 60, 'text': ['กดยืนยันการสมัคร']},
    
    {'id': 'dec1', 'type': 'decision', 'x': 780, 'y': 420, 'w': 140, 'h': 80, 'text': ['กรอกครบถ้วน?']},
    {'id': 'err1', 'type': 'error', 'x': 780, 'y': 310, 'w': 140, 'h': 50, 'text': ['แจ้งเตือนกรอกไม่ครบ']},
    {'id': 'sys1', 'type': 'action_system', 'x': 970, 'y': 430, 'w': 170, 'h': 60, 'text': ['ปรับสถานะผู้ใช้เป็น', 'sellerStatus = VERIFIED']},
    
    {'id': 'c4', 'type': 'action_seller', 'x': 970, 'y': 210, 'w': 170, 'h': 60, 'text': ['ปลดล็อกสิทธิ์เปิดร้าน', 'และเริ่มขายการ์ดได้ทันที']},
    {'id': 'end', 'type': 'end', 'x': 1180, 'y': 220, 'w': 70, 'h': 40, 'text': ['End']}
]

usnew2_conns = [
    {'points': [(170, 240), (210, 240)]},
    {'points': [(360, 240), (400, 240)]},
    {'points': [(560, 240), (600, 240)]},
    {'points': [(740, 240), (850, 240), (850, 420)]},
    {'points': [(850, 420), (850, 360)], 'label': 'No', 'label_pos': (865, 390)},
    {'points': [(780, 335), (480, 335), (480, 270)]},
    {'points': [(920, 460), (970, 460)], 'label': 'Yes', 'label_pos': (945, 445)},
    {'points': [(1055, 430), (1055, 270)]},
    {'points': [(1140, 240), (1180, 240)]}
]

svg_new2 = create_svg_flow(
    "US-NEW-2: Self-serve Seller Verification (No Manual Admin Approval)",
    "both",
    [("Customer / Seller", 130, 360), ("System", 360, 560)],
    usnew2_nodes, usnew2_conns, width=1300, height=580
)
with open(os.path.join(output_dir, "US-NEW-2-Seller-Verification.svg"), "w", encoding="utf-8") as f:
    f.write(svg_new2)

# -------------------------------------------------------------
# 8. US-NEW-3: Stock Reservation Logic
# -------------------------------------------------------------
usnew3_nodes = [
    {'id': 'start', 'type': 'start', 'x': 100, 'y': 220, 'w': 70, 'h': 40, 'text': ['start']},
    {'id': 'c1', 'type': 'action_customer', 'x': 210, 'y': 210, 'w': 140, 'h': 60, 'text': ['ลูกค้าเปิดหน้า', 'Shopping Cart']},
    {'id': 'c2', 'type': 'action_customer', 'x': 390, 'y': 210, 'w': 140, 'h': 60, 'text': ['กดปุ่มบวกจำนวน (+)', 'เพิ่มการ์ดในตะกร้า']},
    
    {'id': 'dec1', 'type': 'decision', 'x': 570, 'y': 420, 'w': 170, 'h': 80, 'text': ['จำนวน <= สต๊อกว่าง?', '(OnHand - Reserved)']},
    {'id': 'err1', 'type': 'error', 'x': 570, 'y': 310, 'w': 170, 'h': 50, 'text': ['แจ้งเตือนสต๊อกไม่พอจอง']},
    {'id': 'sys1', 'type': 'action_system', 'x': 780, 'y': 430, 'w': 150, 'h': 60, 'text': ['อัปเดตจำนวนการ์ด', 'ในตะกร้าสินค้า']},
    
    {'id': 'c3', 'type': 'action_customer', 'x': 780, 'y': 210, 'w': 150, 'h': 60, 'text': ['แสดงยอดรวมและ', 'จำนวนสินค้าอัปเดต']},
    {'id': 'end', 'type': 'end', 'x': 970, 'y': 220, 'w': 70, 'h': 40, 'text': ['End']}
]

usnew3_conns = [
    {'points': [(170, 240), (210, 240)]},
    {'points': [(350, 240), (390, 240)]},
    {'points': [(530, 240), (655, 240), (655, 420)]},
    {'points': [(655, 420), (655, 360)], 'label': 'No', 'label_pos': (670, 390)},
    {'points': [(570, 335), (460, 335), (460, 270)]},
    {'points': [(740, 460), (780, 460)], 'label': 'Yes', 'label_pos': (760, 445)},
    {'points': [(855, 430), (855, 270)]},
    {'points': [(930, 240), (970, 240)]}
]

svg_new3 = create_svg_flow(
    "US-NEW-3: Stock Reservation Semantics (Real-time Cart Clamp)",
    "customer",
    [("Customer", 130, 360), ("System", 360, 560)],
    usnew3_nodes, usnew3_conns, width=1080, height=580
)
with open(os.path.join(output_dir, "US-NEW-3-Stock-Reservation.svg"), "w", encoding="utf-8") as f:
    f.write(svg_new3)

print("All 8 custom SVG swimlane flowcharts generated successfully!")
