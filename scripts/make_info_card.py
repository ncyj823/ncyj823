def generate():
    print("Generating neofetch info card...")
    
    svg_content = """<svg xmlns="http://www.w3.org/2000/svg" width="490" height="370" viewBox="0 0 490 370">
<style>
  text { font-family: 'Courier New', Courier, monospace; font-size: 13px; fill: #c9d1d9; }
  .title { fill: #58a6ff; font-weight: bold; }
  .key { fill: #7ee787; font-weight: bold; }
  .line { opacity: 0; animation: fadeIn 0.5s ease-out forwards; }
  @keyframes fadeIn { to { opacity: 1; } }
</style>
<rect width="100%" height="100%" fill="#0d1117" rx="6"/>
<g transform="translate(20, 25)">
  <text x="0" y="20" class="title line" style="animation-delay: 0.1s;">ncyj@github</text>
  <text x="0" y="38" class="line" style="animation-delay: 0.15s; fill: #484f58;">--------------------------------</text>
  
  <text x="0" y="65" class="line" style="animation-delay: 0.2s;"><tspan class="key">OS:</tspan> Linux / Ubuntu 24.04 LTS</text>
  <text x="0" y="90" class="line" style="animation-delay: 0.3s;"><tspan class="key">Host:</tspan> KIIT CSE (B.Tech)</text>
  <text x="0" y="115" class="line" style="animation-delay: 0.4s;"><tspan class="key">Focus:</tspan> AI &amp; Backend Engineering</text>
  <text x="0" y="140" class="line" style="animation-delay: 0.5s;"><tspan class="key">Stack:</tspan> Python, FastAPI, LangGraph, Redis</text>
  <text x="0" y="165" class="line" style="animation-delay: 0.6s;"><tspan class="key">Tools:</tspan> Docker, Supabase, Modal, PyTorch</text>
  <text x="0" y="190" class="line" style="animation-delay: 0.7s;"><tspan class="key">Current:</tspan> AI Product Eng @ ActTrident</text>
  <text x="0" y="225" class="line" style="animation-delay: 0.8s; fill: #8b949e;">&#x25CF; #58a6ff &#x25CF; #7ee787 &#x25CF; #d2a8ff &#x25CF; #f0883e</text>
</g>
</svg>"""

    with open("info-card.svg", "w") as f:
        f.write(svg_content)

    print("Saved info-card.svg successfully.")

if __name__ == "__main__":
    generate()
