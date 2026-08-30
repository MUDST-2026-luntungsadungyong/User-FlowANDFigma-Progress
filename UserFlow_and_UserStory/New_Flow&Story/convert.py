import os
import zlib
import base64
import urllib.request

def encode_kroki(text):
    compressed = zlib.compress(text.encode('utf-8'), 9)
    encoded = base64.urlsafe_b64encode(compressed).decode('ascii')
    return encoded

directory = r"C:\Devops_NEW\UserFlow_and_UserStory\New_Flow&Story"
for filename in os.listdir(directory):
    if filename.endswith(".mmd"):
        mmd_path = os.path.join(directory, filename)
        svg_filename = filename.replace(".mmd", ".svg")
        svg_path = os.path.join(directory, svg_filename)
        
        with open(mmd_path, "r", encoding="utf-8") as f:
            code = f.read()
            
        payload = encode_kroki(code)
        url = f"https://kroki.io/mermaid/svg/{payload}"
        
        try:
            print(f"Downloading {svg_filename}...")
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as response:
                svg_data = response.read()
                with open(svg_path, "wb") as out_f:
                    out_f.write(svg_data)
            print(f"Saved {svg_filename}")
        except Exception as e:
            print(f"Failed to generate {svg_filename}: {e}")
