#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TEMP_DIR="$(mktemp -d)"
trap 'rm -rf "$TEMP_DIR"' EXIT

(
  cd "$TEMP_DIR"
  "$REPO_ROOT/scripts/run.sh"
)

test -f "$REPO_ROOT/output/summary.csv.gz"
test -d "$REPO_ROOT/logs"

echo "Basic shell test passed."
