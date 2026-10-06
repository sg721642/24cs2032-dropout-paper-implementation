import re
import os
import subprocess
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
PREVIEW_DIR = Path("/tmp/preview_test/24CS2032_Dropout_Presentation.pptx.qlpreview")
OUT_DIR = PROJECT_ROOT / "presentation" / "rendered"
OUT_DIR.mkdir(parents=True, exist_ok=True)

with open(PREVIEW_DIR / "Preview.html") as f:
    html = f.read()

# Extract styles
styles = re.findall(r"<style.*?</style>", html, re.DOTALL)
all_styles = "\n".join(styles)

# Split into individual slides
slide_indices = [m.start() for m in re.finditer(r'<div class="slide"', html)]
slide_indices.append(html.find("</body>"))

print(f"[*] Found {len(slide_indices)-1} slides in Preview.html")

def add_px(match):
    prop = match.group(1)
    val = match.group(2)
    return f"{prop}:{val}px"

for i in range(len(slide_indices) - 1):
    slide_content = html[slide_indices[i]:slide_indices[i+1]]
    slide_file = f"/tmp/slide_{i+1}.html"
    
    # We update image paths to reference files in PREVIEW_DIR
    slide_content = slide_content.replace('src="Attachment', f'src="{PREVIEW_DIR}/Attachment')
    
    full_html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
{all_styles}
<style>
body {{
    margin: 0;
    padding: 0;
    background: #ffffff;
    width: 959px;
    height: 540px;
    overflow: hidden;
}}
div.slide {{
    margin: 0 !important;
    box-shadow: none !important;
    top: 0 !important;
    left: 0 !important;
    position: absolute !important;
    width: 959px !important;
    height: 540px !important;
}}
</style>
</head>
<body>
{slide_content}
</body>
</html>"""
    
    # Fix unitless CSS dimensions
    fixed_html = re.sub(
        r'\b(top|left|right|bottom|width|height|margin-top|margin-left|margin-right|margin-bottom|padding-top|padding-left|padding-right|padding-bottom|font-size):(\d+)(?=[;\s"\}])',
        add_px,
        full_html
    )
    
    with open(slide_file, "w") as sf:
        sf.write(fixed_html)
        
    out_img = OUT_DIR / f"slide_{i+1}.png"
    subprocess.run([
        "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser",
        "--headless",
        f"--screenshot={out_img}",
        "--window-size=959,540",
        "--hide-scrollbars",
        slide_file
    ], check=True, capture_output=True)
    
    print(f"[*] Rendered slide {i+1} -> {out_img.relative_to(PROJECT_ROOT)} ({out_img.stat().st_size} bytes)")

print("[*] All slides rendered successfully.")
