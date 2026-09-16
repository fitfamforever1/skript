#!/bin/bash

cd "$(dirname "$0")" || exit 1

git add .

if git diff --cached --quiet; then
    echo "No changes to commit."
    exit 0
fi

git commit -m "Auto" || exit 1
git push

echo "Done."
