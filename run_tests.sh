#!/usr/bin/env bash
set -e
python3 -m venv venv 2>/dev/null || true
source venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
python3 -m playwright install chromium
mkdir -p artifacts
python3 -m pytest -q --html=artifacts/report.html --self-contained-html
echo "Report: artifacts/report.html"
