#!/usr/bin/env bash
# Push the site to GitHub. Pages rebuilds automatically from the main branch.
set -euo pipefail

cd "$(dirname "$0")/.."

git add -A
if git diff --cached --quiet; then
  echo "没有需要提交的改动"
else
  git -c user.name="Yongjie Qian" \
      -c user.email="YongjieQian03@users.noreply.github.com" \
      commit -m "${1:-update site content}"
fi

git push origin main
echo "已推送，稍等几十秒后访问 https://YongjieQian03.github.io/"
