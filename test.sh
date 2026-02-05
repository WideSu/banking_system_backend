#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

cd "$SCRIPT_DIR"

echo "Running pytest in $(pwd)"
pytest -q --durations=0 tests
echo "Finish all tests"
exit 0
