import cv2
import numpy as np

RAMP = " .`:-=+*cs#%@"
CHAR_W = 6
CHAR_H = 11

def convert():
    print("Generating clean ASCII portrait SVG...")
    img = cv2.imread("source-prepped.png", cv2.IMREAD_GRAYSCALE)
    if img is None:
        print("Error: source-prepped.png not found.")
        return

    h, w = img.shape
    scale = 100 / w
    new_w = 100
    new_h = int(h * scale * 0.55)
    resized = cv2.resize(img, (new_w, new_h))

    svg_w = new_w * CHAR_W
    svg_h = new_h * CHAR_H

    svg_lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{svg_w}" height="{svg_h}" viewBox="0 0 {svg_w} {svg_h}">',
        '<style>',
        f"  text {{ font-family: 'Courier New', Courier, monospace; font-size: {CHAR_H}px; fill: #58a6ff; }}",
        "  .row { animation: wipe 0.8s ease-out forwards; opacity: 0; }",
        "  @keyframes wipe { to { opacity: 1; } }",
        '</style>',
        '<rect width="100%" height="100%" fill="#0d1117" rx="6"/>',
        '<g transform="translate(10, 20)">'
    ]

    for y_idx in range(new_h):
        row_str = ""
        for x_idx in range(new_w):
            pixel = resized[y_idx, x_idx]
            
            # If pixel is near-black (background), treat as space
            if pixel < 15:
                row_str += "&#160;"
                continue

            ramp_idx = int((pixel / 255.0) * (len(RAMP) - 1))
            char = RAMP[ramp_idx]
            if char == " ": row_str += "&#160;"
            elif char == "<": row_str += "&lt;"
            elif char == ">": row_str += "&gt;"
            elif char == "&": row_str += "&amp;"
            else: row_str += char

        delay = f"{y_idx * 0.02:.2f}s"
        svg_lines.append(f'<text x="0" y="{y_idx * CHAR_H}" class="row" style="animation-delay: {delay}">{row_str}</text>')

    svg_lines.append("</g>")
    svg_lines.append("</svg>")

    with open("ncyj-ascii-v2.svg", "w") as f:
        f.write("\n".join(svg_lines))

    print("Saved clean ncyj-ascii-v2.svg successfully.")

if __name__ == "__main__":
    convert()
