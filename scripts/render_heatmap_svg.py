import json

PALETTE = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353", "#69f0a0"]

def render():
    with open("data/contributions.json") as f:
        data = json.load(f)

    days = data["days"]
    total = data["total_contributions"]

    weeks = []
    current_week = []
    for d in days:
        current_week.append(d)
        if len(current_week) == 7:
            weeks.append(current_week)
            current_week = []
    if current_week:
        weeks.append(current_week)

    box_size = 11
    gap = 4
    col_width = box_size + gap

    width = len(weeks) * col_width + 40
    height = 150

    svg_lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<style>',
        "  text { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; font-size: 11px; fill: #8b949e; }",
        "  .box { rx: 2px; ry: 2px; transition: all 0.3s ease; }",
        "  @keyframes slideIn {",
        "    0% { opacity: 0; transform: translateY(10px); }",
        "    100% { opacity: 1; transform: translateY(0); }",
        "  }",
        "  .heatmap-group { animation: slideIn 0.8s ease-out forwards; }",
        '</style>',
        '<rect width="100%" height="100%" fill="#0d1117" rx="6"/>',
        f'<g class="heatmap-group" transform="translate(20, 20)">'
    ]

    for w_idx, week in enumerate(weeks):
        for d_idx, day in enumerate(week):
            x = w_idx * col_width
            y = d_idx * col_width
            color = PALETTE[day["level"] if day["level"] < len(PALETTE) else 5]
            svg_lines.append(f'<rect class="box" x="{x}" y="{y}" width="{box_size}" height="{box_size}" fill="{color}"><title>{day["date"]}: {day["count"]} contributions</title></rect>')

    svg_lines.append(f'<text x="0" y="{7 * col_width + 22}">⚡ {total:,} contributions in the last year</text>')
    svg_lines.append("</g>")
    svg_lines.append("</svg>")

    with open("contrib-heatmap.svg", "w") as f:
        f.write("\n".join(svg_lines))

    print("Rendered contrib-heatmap.svg successfully.")

if __name__ == "__main__":
    render()
