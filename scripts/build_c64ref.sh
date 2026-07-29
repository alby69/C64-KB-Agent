#!/bin/bash
set -e

echo "=== Building c64ref documentation ==="
python -m cleaners.c64ref_cleaner

echo "=== Done ==="
