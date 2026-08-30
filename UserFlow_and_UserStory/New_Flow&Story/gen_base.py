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
    if actor_type in ['seller', 'both']:
        svg.append(f'<circle cx="{lx}" cy="{ly}" r="9" fill="#fef08a" />')
        svg.append(f'<text x="{lx+18}" y="{ly}" class="legend-text">Seller actions</text>')
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
            lx_lbl, ly_lbl = conn['label_pos']
            txt = conn['label']
            tw = len(txt) * 8 + 12
            svg.append(f'<rect x="{lx_lbl - tw//2}" y="{ly_lbl - 10}" width="{tw}" height="20" fill="#ffffff" rx="4" />')
            svg.append(f'<text x="{lx_lbl}" y="{ly_lbl}" class="edge-label">{html.escape(txt)}</text>')

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

def save_svg(name, xml_data):
    output_dir = r"C:\Devops_NEW\UserFlow_and_UserStory\New_Flow&Story"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    with open(os.path.join(output_dir, name), "w", encoding="utf-8") as f:
        f.write(xml_data)
