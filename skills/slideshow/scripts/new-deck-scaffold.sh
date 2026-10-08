#!/usr/bin/env bash
# Scaffold a new deck from the bundled engine template.
# Usage: ./new-deck-scaffold.sh <reveal|slidev|marp> <deck-name>
set -euo pipefail
ENGINE="${1:?usage: new-deck-scaffold.sh <reveal|slidev|marp> <deck-name>}"
NAME="${2:?usage: new-deck-scaffold.sh <reveal|slidev|marp> <deck-name>}"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"

case "$ENGINE" in
  reveal) SRC="$ROOT/examples/reveal-demo/index.html"; DEST="$NAME/index.html" ;;
  slidev) SRC="$ROOT/examples/slidev-demo/slides.md"; DEST="$NAME/slides.md" ;;
  marp)   SRC="$ROOT/examples/marp-demo/deck.md";      DEST="$NAME/deck.md" ;;
  *) echo "unknown engine: $ENGINE (reveal|slidev|marp)" >&2; exit 1 ;;
esac

mkdir -p "$NAME/assets"
cp "$SRC" "$DEST"
cat > "$NAME/assets/README.txt" <<'EOF'
Put downloaded images here. For each image add a <name>.txt license record, e.g.:
  Source: https://unsplash.com/photos/...
  License: Unsplash License (free commercial use)
  Date: YYYY-MM-DD
EOF
echo "scaffolded $ENGINE deck at $NAME/"
echo "next: edit $DEST, add images to $NAME/assets, run verify-images.py"
