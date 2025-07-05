#!/bin/bash

echo "🔧 Installing InstaIntelX v3.5 ..."
pkg update -y && pkg install -y git python
pip install -r requirements.txt 2>/dev/null || true

mkdir -p ~/InstaIntelX
cp -r * ~/InstaIntelX/

echo "✅ Installed successfully."
echo "🚀 To start, run:"
echo "cd ~/InstaIntelX && python run.py"
