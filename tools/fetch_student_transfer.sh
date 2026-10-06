#!/usr/bin/env bash
set -euo pipefail

DEST="${1:-assets_inbox/student-transfer}"
mkdir -p "$(dirname "$DEST")"

if [ -d "$DEST/.git" ]; then
  echo "Updating Student Transfer checkout at $DEST"
  git -C "$DEST" pull --ff-only
else
  echo "Cloning Student Transfer into local-only inbox: $DEST"
  git clone --depth 1 https://git.student-transfer.com/st/student-transfer.git "$DEST"
fi

echo
echo "Student Transfer has been fetched into an ignored local-only directory."
echo "No asset is automatically cleared for redistribution."
echo
python tools/asset_intake.py assets_inbox --output asset_build
