#!/bin/bash
set -e

echo "=== 1. Setting up Virtual Environment ==="
if [ ! -d ".venv" ]; then
    python3 -m venv .venv
fi
source .venv/bin/activate
pip install --upgrade pip
pip install -r scripts/requirements.txt

echo "=== 2. Fetching Contributions ==="
python3 scripts/fetch_contributions.py

echo "=== 3. Rendering Heatmap SVG ==="
python3 scripts/render_heatmap_svg.py

echo "=== 4. Generating Info Card SVG ==="
python3 scripts/make_info_card.py

if [ -f "source-photo.jpg" ]; then
    echo "=== 5. Processing Photo & Generating ASCII SVG ==="
    python3 scripts/prep_photo.py source-photo.jpg
    python3 scripts/make_ascii_svg.py
else
    echo "Skipping ASCII portrait: Place a photo named 'source-photo.jpg' in the root directory if you want to generate your ASCII avatar."
fi

echo "=== Done! All assets ready. ==="
