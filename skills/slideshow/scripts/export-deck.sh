#!/usr/bin/env bash
# Export a deck to PDF/PPTX/SPA depending on its engine.
# Usage: ./export-deck.sh <reveal|slidev|marp> <deck-path> [out-dir]
set -euo pipefail
ENGINE="${1:?usage: export-deck.sh <reveal|slidev|marp> <deck-path> [out-dir]}"
DECK="${2:?usage: export-deck.sh <reveal|slidev|marp> <deck-path> [out-dir]}"
OUT="${3:-dist}"
mkdir -p "$OUT"

case "$ENGINE" in
  reveal)
    # decktape renders reveal.js to PDF (requires decktape + chromium)
    npx --yes decktape reveal "$DECK" "$OUT/deck.pdf"
    ;;
  slidev)
    # run from the slidev project dir; exports PDF + SPA
    npx --yes slidev export "$DECK" --output "$OUT/deck.pdf" --format pdf
    npx --yes slidev build "$DECK" --out "$OUT/spa"
    ;;
  marp)
    # --allow-local-files so local ./assets resolve during export
    npx --yes @marp-team/marp-cli@latest "$DECK" -o "$OUT/deck.html" --allow-local-files
    npx --yes @marp-team/marp-cli@latest "$DECK" -o "$OUT/deck.pdf" --pdf --allow-local-files
    npx --yes @marp-team/marp-cli@latest "$DECK" -o "$OUT/deck.pptx" --pptx --allow-local-files
    ;;
  *)
    echo "unknown engine: $ENGINE (reveal|slidev|marp)" >&2
    exit 1
    ;;
esac
echo "exported $ENGINE deck to $OUT/"
