import os
import html
import xml.etree.ElementTree as ET

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
    svg.append('''
        <marker id="arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
            <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#64748b" />
        </marker>
    ''')
    svg.append('</defs>')
    svg.append(f'<rect width="{width}" height="{height}" fill="#ffffff" />')
    svg.append(f'<text x="40" y="45" class="title">{html.escape(title)}</text>')
    
    lx = 40
    ly = 85
    if actor_type in ['customer', 'both']:
        svg.append(f'<circle cx="{lx}" cy="{ly}" r="9" fill="#d8b4fe" />')
        svg.append(f'<text x="{lx+18}" y="{ly}" class="legend-text">Customer actions</text>')
        lx += 160
    if actor_type in ['seller', 'both', 'admin_seller']:
        svg.append(f'<circle cx="{lx}" cy="{ly}" r="9" fill="#fef08a" />')
        lbl = "Seller actions" if actor_type != 'admin_seller' else "Seller Admin actions"
        svg.append(f'<text x="{lx+18}" y="{ly}" class="legend-text">{lbl}</text>')
        lx += 150
    
    svg.append(f'<circle cx="{lx}" cy="{ly}" r="9" fill="#1e293b" />')
    svg.append(f'<text x="{lx+18}" y="{ly}" class="legend-text">Decisions</text>')
    lx += 110
    
    svg.append(f'<circle cx="{lx}" cy="{ly}" r="9" fill="#fed7aa" />')
    svg.append(f'<text x="{lx+18}" y="{ly}" class="legend-text">System actions</text>')
    lx += 140
    
    svg.append(f'<circle cx="{lx}" cy="{ly}" r="9" fill="#fca5a5" />')
    svg.append(f'<text x="{lx+18}" y="{ly}" class="legend-text">Error</text>')
    
    for idx, lane in enumerate(lanes):
        name, y_start, y_end = lane
        mid_y = (y_start + y_end) // 2
        svg.append(f'<text x="45" y="{mid_y}" class="lane-label" transform="rotate(-90 45 {mid_y})">{html.escape(name)}</text>')
        if idx < len(lanes) - 1:
            svg.append(f'<line x1="80" y1="{y_end}" x2="{width-40}" y2="{y_end}" class="lane-line" />')
            
    for conn in connections:
        pts = conn.get('points', [])
        p_str = " ".join([f"{x},{y}" for x, y in pts])
        svg.append(f'<polyline points="{p_str}" class="flow-line" marker-end="url(#arrow)" />')
        if 'label' in conn and 'label_pos' in conn:
            lx, ly = conn['label_pos']
            txt = conn['label']
            tw = len(txt) * 8 + 12
            svg.append(f'<rect x="{lx - tw//2}" y="{ly - 10}" width="{tw}" height="20" fill="#ffffff" rx="4" />')
            svg.append(f'<text x="{lx}" y="{ly}" class="edge-label">{html.escape(txt)}</text>')

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
            pts = f"{x + w//2},{y} {x + w},{y + h//2} {x + w//2},{y + h} {x},{y + h//2}"
            svg.append(f'<polygon points="{pts}" class="node-decision" />')
            
        line_height = 16
        total_text_h = len(lines) * line_height
        start_text_y = y + (h - total_text_h) // 2 + line_height // 2
        for i, line in enumerate(lines):
            cur_y = start_text_y + i * line_height
            svg.append(f'<text x="{x + w//2}" y="{cur_y}">{html.escape(line)}</text>')
            
    svg.append('</svg>')
    res = "\n".join(svg)
    ET.fromstring(res)
    return res

output_dir = r"C:\Devops_NEW\UserFlow_and_UserStory\New_Flow&Story"
def save_svg(name, xml):
    with open(os.path.join(output_dir, name), "w", encoding="utf-8") as f:
        f.write(xml)

# -------------------------------------------------------------
# US-05-1: Add Product
# -------------------------------------------------------------
n_05_1 = [
    {'id': 'start', 'type': 'start', 'x': 100, 'y': 220, 'w': 70, 'h': 40, 'text': ['start']},
    {'id': 's1', 'type': 'action_seller', 'x': 210, 'y': 210, 'w': 140, 'h': 60, 'text': ['เข้าหน้า Product', 'Management']},
    {'id': 's2', 'type': 'action_seller', 'x': 390, 'y': 210, 'w': 140, 'h': 60, 'text': ['กดปุ่ม "Add Product"']},
    {'id': 's3', 'type': 'action_seller', 'x': 570, 'y': 210, 'w': 150, 'h': 60, 'text': ['เลือกลิสต์การ์ดจาก', 'My Collection']},
    {'id': 's4', 'type': 'action_seller', 'x': 760, 'y': 210, 'w': 140, 'h': 60, 'text': ['กรอกราคาขาย', 'และจำนวนสต๊อก']},
    {'id': 's5', 'type': 'action_seller', 'x': 940, 'y': 210, 'w': 140, 'h': 60, 'text': ['กด "Save/Publish"']},
    {'id': 'dec1', 'type': 'decision', 'x': 1120, 'y': 420, 'w': 140, 'h': 80, 'text': ['ข้อมูลถูกต้อง?']},
    {'id': 'err1', 'type': 'error', 'x': 1120, 'y': 310, 'w': 140, 'h': 50, 'text': ['แจ้ง Error ข้อมูลไม่ครบ']},
    {'id': 'sys1', 'type': 'action_system', 'x': 1300, 'y': 430, 'w': 150, 'h': 60, 'text': ['บันทึก Product', '(owner = sellerId)']},
    {'id': 'sys2', 'type': 'action_system', 'x': 1490, 'y': 430, 'w': 150, 'h': 60, 'text': ['แจ้ง Popup สำเร็จ']},
    {'id': 'end', 'type': 'end', 'x': 1680, 'y': 220, 'w': 70, 'h': 40, 'text': ['End']}
]
c_05_1 = [
    {'points': [(170, 240), (210, 240)]},
    {'points': [(350, 240), (390, 240)]},
    {'points': [(530, 240), (570, 240)]},
    {'points': [(720, 240), (760, 240)]},
    {'points': [(900, 240), (940, 240)]},
    {'points': [(1080, 240), (1190, 240), (1190, 420)]},
    {'points': [(1190, 420), (1190, 360)], 'label': 'No', 'label_pos': (1205, 390)},
    {'points': [(1120, 335), (830, 335), (830, 270)]},
    {'points': [(1260, 460), (1300, 460)], 'label': 'Yes', 'label_pos': (1280, 445)},
    {'points': [(1450, 460), (1490, 460)]},
    {'points': [(1565, 430), (1565, 240), (1680, 240)]}
]
save_svg("US-05-1_Add-Product.svg", create_svg_flow("US-05-1: Add Product (Seller)", "seller", [("Seller", 130, 370), ("System", 370, 560)], n_05_1, c_05_1, 1800, 580))

# -------------------------------------------------------------
# US-05-2: Delete Product
# -------------------------------------------------------------
n_05_2 = [
    {'id': 'start', 'type': 'start', 'x': 100, 'y': 220, 'w': 70, 'h': 40, 'text': ['start']},
    {'id': 's1', 'type': 'action_seller', 'x': 210, 'y': 210, 'w': 140, 'h': 60, 'text': ['เข้าหน้า', '"Product List"']},
    {'id': 's2', 'type': 'action_seller', 'x': 390, 'y': 210, 'w': 140, 'h': 60, 'text': ['กด "Delete"', 'ที่สินค้ารายการหนึ่ง']},
    {'id': 'dec1', 'type': 'decision', 'x': 570, 'y': 200, 'w': 140, 'h': 80, 'text': ['ยืนยันการลบ?']},
    
    {'id': 'dec2', 'type': 'decision', 'x': 750, 'y': 420, 'w': 150, 'h': 80, 'text': ['สินค้าอยู่ใน Order', 'ที่ยังไม่จบ (Pending)?']},
    {'id': 'err1', 'type': 'error', 'x': 750, 'y': 310, 'w': 150, 'h': 50, 'text': ['Error: ไม่สามารถลบได้']},
    {'id': 'sys1', 'type': 'action_system', 'x': 940, 'y': 430, 'w': 150, 'h': 60, 'text': ['ลบ/Archive', 'Record ใน DB']},
    {'id': 's3', 'type': 'action_seller', 'x': 1130, 'y': 210, 'w': 150, 'h': 60, 'text': ['แสดงหน้า Product List', 'ที่อัปเดตแล้ว']},
    {'id': 'end', 'type': 'end', 'x': 1320, 'y': 220, 'w': 70, 'h': 40, 'text': ['End']}
]
c_05_2 = [
    {'points': [(170, 240), (210, 240)]},
    {'points': [(350, 240), (390, 240)]},
    {'points': [(530, 240), (570, 240)]},
    {'points': [(640, 280), (640, 360), (460, 360), (460, 270)], 'label': 'No', 'label_pos': (655, 300)},
    {'points': [(710, 240), (825, 240), (825, 420)], 'label': 'Yes', 'label_pos': (730, 225)},
    {'points': [(825, 420), (825, 360)], 'label': 'Yes', 'label_pos': (840, 390)},
    {'points': [(750, 335), (690, 335), (690, 240)], 'label': '', 'label_pos': (0,0)},
    {'points': [(900, 460), (940, 460)], 'label': 'No', 'label_pos': (920, 445)},
    {'points': [(1090, 460), (1205, 460), (1205, 270)]},
    {'points': [(1280, 240), (1320, 240)]}
]
save_svg("US-05-2_Delete-Product.svg", create_svg_flow("US-05-2: Delete Product (Seller)", "seller", [("Seller", 130, 380), ("System", 380, 580)], n_05_2, c_05_2, 1450, 600))

# -------------------------------------------------------------
# US-05-3: Update Product
# -------------------------------------------------------------
n_05_3 = [
    {'id': 'start', 'type': 'start', 'x': 100, 'y': 220, 'w': 70, 'h': 40, 'text': ['start']},
    {'id': 's1', 'type': 'action_seller', 'x': 210, 'y': 210, 'w': 140, 'h': 60, 'text': ['เข้าหน้า', '"Product List"']},
    {'id': 's2', 'type': 'action_seller', 'x': 390, 'y': 210, 'w': 140, 'h': 60, 'text': ['กด "Edit"', 'แก้ไขข้อมูล']},
    {'id': 's3', 'type': 'action_seller', 'x': 570, 'y': 210, 'w': 140, 'h': 60, 'text': ['กรอกข้อมูลใหม่', 'เช่น ราคา, สต๊อก']},
    {'id': 's4', 'type': 'action_seller', 'x': 750, 'y': 210, 'w': 140, 'h': 60, 'text': ['กด "Save"']},
    
    {'id': 'dec1', 'type': 'decision', 'x': 930, 'y': 420, 'w': 140, 'h': 80, 'text': ['Validate', 'ฟอร์มถูกต้อง?']},
    {'id': 'err1', 'type': 'error', 'x': 930, 'y': 310, 'w': 140, 'h': 50, 'text': ['แจ้ง Error inline']},
    {'id': 'sys1', 'type': 'action_system', 'x': 1110, 'y': 430, 'w': 150, 'h': 60, 'text': ['อัปเดต Record']},
    {'id': 'sys2', 'type': 'action_system', 'x': 1300, 'y': 430, 'w': 150, 'h': 60, 'text': ['แจ้งสำเร็จ']},
    {'id': 's5', 'type': 'action_seller', 'x': 1300, 'y': 210, 'w': 150, 'h': 60, 'text': ['กลับหน้า Product List']},
    {'id': 'end', 'type': 'end', 'x': 1490, 'y': 220, 'w': 70, 'h': 40, 'text': ['End']}
]
c_05_3 = [
    {'points': [(170, 240), (210, 240)]},
    {'points': [(350, 240), (390, 240)]},
    {'points': [(530, 240), (570, 240)]},
    {'points': [(710, 240), (750, 240)]},
    {'points': [(890, 240), (1000, 240), (1000, 420)]},
    {'points': [(1000, 420), (1000, 360)], 'label': 'No', 'label_pos': (1015, 390)},
    {'points': [(930, 335), (640, 335), (640, 270)]},
    {'points': [(1070, 460), (1110, 460)], 'label': 'Yes', 'label_pos': (1090, 445)},
    {'points': [(1260, 460), (1300, 460)]},
    {'points': [(1375, 430), (1375, 270)]},
    {'points': [(1450, 240), (1490, 240)]}
]
save_svg("US-05-3_Update-Product.svg", create_svg_flow("US-05-3: Update Product (Seller)", "seller", [("Seller", 130, 370), ("System", 370, 560)], n_05_3, c_05_3, 1600, 580))

# -------------------------------------------------------------
# US-05-4 & 6: Check and Filter Product List
# -------------------------------------------------------------
n_05_4 = [
    {'id': 'start', 'type': 'start', 'x': 100, 'y': 220, 'w': 70, 'h': 40, 'text': ['start']},
    {'id': 's1', 'type': 'action_seller', 'x': 210, 'y': 210, 'w': 140, 'h': 60, 'text': ['เปิดหน้า', '"Product List"']},
    {'id': 'sys1', 'type': 'action_system', 'x': 205, 'y': 420, 'w': 150, 'h': 60, 'text': ['ดึง Product List ทั้งหมด', '(owner=sellerId)']},
    
    {'id': 's2', 'type': 'action_seller', 'x': 430, 'y': 210, 'w': 160, 'h': 60, 'text': ['เลือก Filter (Status/Name/Stock)']},
    {'id': 's3', 'type': 'action_seller', 'x': 630, 'y': 210, 'w': 140, 'h': 60, 'text': ['กด "Apply"']},
    
    {'id': 'sys2', 'type': 'action_system', 'x': 625, 'y': 420, 'w': 150, 'h': 60, 'text': ['Query สินค้าตาม Filter']},
    {'id': 'dec1', 'type': 'decision', 'x': 820, 'y': 410, 'w': 140, 'h': 80, 'text': ['ดึงข้อมูลสำเร็จ?']},
    {'id': 'err1', 'type': 'error', 'x': 820, 'y': 310, 'w': 140, 'h': 50, 'text': ['Error: ดึงข้อมูลไม่สำเร็จ']},
    
    {'id': 'sys3', 'type': 'action_system', 'x': 1000, 'y': 420, 'w': 150, 'h': 60, 'text': ['แสดงผลลัพธ์']},
    {'id': 's4', 'type': 'action_seller', 'x': 1000, 'y': 210, 'w': 150, 'h': 60, 'text': ['ดูรายการสินค้า']},
    {'id': 'end', 'type': 'end', 'x': 1190, 'y': 220, 'w': 70, 'h': 40, 'text': ['End']}
]
c_05_4 = [
    {'points': [(170, 240), (210, 240)]},
    {'points': [(280, 270), (280, 420)]},
    {'points': [(355, 450), (395, 450), (395, 240), (430, 240)]},
    {'points': [(590, 240), (630, 240)]},
    {'points': [(700, 270), (700, 420)]},
    {'points': [(775, 450), (820, 450)]},
    {'points': [(890, 450), (890, 360)], 'label': 'No', 'label_pos': (905, 390)},
    {'points': [(820, 335), (510, 335), (510, 270)]},
    {'points': [(960, 450), (1000, 450)], 'label': 'Yes', 'label_pos': (980, 435)},
    {'points': [(1075, 420), (1075, 270)]},
    {'points': [(1150, 240), (1190, 240)]}
]
save_svg("US-05-4-and-6_Check-Filter-Product.svg", create_svg_flow("US-05-4 & US-05-6: Product List & Filter (Seller)", "seller", [("Seller", 130, 380), ("System", 380, 560)], n_05_4, c_05_4, 1300, 580))

# -------------------------------------------------------------
# US-05-5: Toggle Visibility
# -------------------------------------------------------------
n_05_5 = [
    {'id': 'start', 'type': 'start', 'x': 100, 'y': 220, 'w': 70, 'h': 40, 'text': ['start']},
    {'id': 's1', 'type': 'action_seller', 'x': 210, 'y': 210, 'w': 140, 'h': 60, 'text': ['เปิดหน้า', '"Product List"']},
    {'id': 's2', 'type': 'action_seller', 'x': 390, 'y': 210, 'w': 140, 'h': 60, 'text': ['กดปุ่ม Toggle', 'Show/Hide สินค้า']},
    
    {'id': 'sys1', 'type': 'action_system', 'x': 385, 'y': 430, 'w': 150, 'h': 60, 'text': ['อัปเดต Visible Status', 'ในฐานข้อมูล']},
    {'id': 'dec1', 'type': 'decision', 'x': 570, 'y': 420, 'w': 140, 'h': 80, 'text': ['อัปเดตสำเร็จ?']},
    {'id': 'err1', 'type': 'error', 'x': 570, 'y': 310, 'w': 150, 'h': 50, 'text': ['Error: เปลี่ยนสถานะไม่สำเร็จ']},
    
    {'id': 'sys2', 'type': 'action_system', 'x': 750, 'y': 430, 'w': 150, 'h': 60, 'text': ['แจ้งผลอัปเดต']},
    {'id': 's3', 'type': 'action_seller', 'x': 750, 'y': 210, 'w': 150, 'h': 60, 'text': ['เห็นสถานะที่เปลี่ยนไป']},
    {'id': 'end', 'type': 'end', 'x': 940, 'y': 220, 'w': 70, 'h': 40, 'text': ['End']}
]
c_05_5 = [
    {'points': [(170, 240), (210, 240)]},
    {'points': [(350, 240), (390, 240)]},
    {'points': [(460, 270), (460, 430)]},
    {'points': [(535, 460), (570, 460)]},
    {'points': [(640, 460), (640, 360)], 'label': 'No', 'label_pos': (655, 390)},
    {'points': [(570, 335), (320, 335), (320, 270)]},
    {'points': [(710, 460), (750, 460)], 'label': 'Yes', 'label_pos': (730, 445)},
    {'points': [(825, 430), (825, 270)]},
    {'points': [(900, 240), (940, 240)]}
]
save_svg("US-05-5_Toggle-Visibility.svg", create_svg_flow("US-05-5: Change Visible Status (Seller)", "seller", [("Seller", 130, 370), ("System", 370, 560)], n_05_5, c_05_5, 1050, 580))

print("Regenerated all detailed US-05 flows successfully.")
