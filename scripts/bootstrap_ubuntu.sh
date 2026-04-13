#!/usr/bin/env bash

set -euo pipefail

PROJECT_DIR="${1:-library-system-school}"

sudo apt update
sudo apt install -y python3 python3-venv python3-pip git

cd "$PROJECT_DIR"

python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python -m scripts.seed_demo

cat <<'EOF'

Bootstrap complete.

Run the application with:
  .venv/bin/python -m apps.web_app

Open:
  http://127.0.0.1:5000

Default admin:
  admin@library.local / admin123
EOF
