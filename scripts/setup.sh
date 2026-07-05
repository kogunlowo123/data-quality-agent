#!/bin/bash
set -euo pipefail
echo "Setting up Data Quality Agent..."
pip install -e ".[dev]"
echo "Setup complete!"
