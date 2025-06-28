#!/bin/bash

echo "🔧 Starting Zeus dev environment..."

# Check for venv
if [ ! -d ".venv" ]; then
  echo "Creating virtual environment..."
  python -m venv .venv
fi

source .venv/bin/activate

echo "Installing dependencies..."
pip install -r requirements.txt

echo "✅ Zeus environment ready. Run your agent with:"
echo "python -m zeus.cli"
