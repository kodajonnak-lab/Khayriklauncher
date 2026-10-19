#!/usr/bin/env python3
"""Change visible launcher strings in a freshly cloned Amethyst source tree.
The upstream source is fetched at build time; this script does not redistribute it.
"""
from pathlib import Path
import re
import sys

root = Path(sys.argv[1] if len(sys.argv) > 1 else "upstream")
res = root / "app_pojavlauncher" / "src" / "main" / "res"
if not res.is_dir():
    raise SystemExit(f"Can't find Android resources directory: {res}")

names = {"app_name", "app_short_name"}
changed = 0
for file in res.rglob("strings.xml"):
    old = file.read_text(encoding="utf-8")
    new = old
    for name in names:
        pattern = rf'(<string\s+name=["\']{re.escape(name)}["\'][^>]*>).*?(</string>)'
        new, count = re.subn(pattern, rf'\g<1>KhayrikLauncher\g<2>', new, flags=re.DOTALL)
        changed += count
    if new != old:
        file.write_text(new, encoding="utf-8")

if changed == 0:
    raise SystemExit("No app_name/app_short_name strings found; stopping instead of building an unbranded APK.")
print(f"Updated {changed} visible app-name string(s).")
