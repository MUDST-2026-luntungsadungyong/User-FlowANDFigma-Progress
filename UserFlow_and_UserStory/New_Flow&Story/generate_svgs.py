import os
import base64
import urllib.request
import time

directory = r"C:\Devops_NEW\UserFlow_and_UserStory\New_Flow&Story"
files = [f for f in os.listdir(directory) if f.endswith(".mmd")]

for filename in files:
    mmd_path = os.path.join(directory, filename)
    svg_filename = filename.replace(".mmd", ".svg")
    svg_path = os.path.join(directory, svg_filename)
    
    with open(mmd_path, "r", encoding="utf-8") as f:
        code = f.read()
        
    payload = base64.b64encode(code.encode('utf-8')).decode('ascii')
    url = f"https://mermaid.ink/svg/{payload}"
    
    print(f"Generating {svg_filename}...")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
            svg_data = response.read()
            with open(svg_path, "wb") as out_f:
                out_f.write(svg_data)
        print(f"-> Successfully saved {svg_filename}")
    except Exception as e:
        print(f"-> Failed for {filename}: {e}")
    time.sleep(0.5)

print("\nAll SVGs generated!")
