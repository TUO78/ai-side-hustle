#!/usr/bin/env python3
import gzip,base64,json,os
from pathlib import Path

B=open("/tmp/b64.txt").read()
d=json.loads(gzip.decompress(base64.b64decode(B)).decode())
BASE=Path("/var/www/ai-side-hustle")
(BASE/"agents/config").mkdir(parents=True,exist_ok=True)
(BASE/"agents/logs").mkdir(parents=True,exist_ok=True)
(BASE/"data").mkdir(parents=True,exist_ok=True)
for k,v in d.items():
    if k.startswith("config/") or k=="requirements.txt":
        p=BASE/k
    else:
        p=BASE/"agents"/k
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(v,encoding="utf-8")
    print(f"OK {k} ({len(v)} chars)")
print("\n=== DONE: All agents installed ===")
print("Next steps:")
print("  cd /var/www/ai-side-hustle")
print("  source .venv/bin/activate")
print("  pip install -r requirements.txt --break-system-packages")
print("  cd agents && python3 init_db.py")
print("  python3 orchestrator.py --dry-run")
