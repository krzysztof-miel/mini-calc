#!/usr/bin/env python3
import csv, sys

if len(sys.argv) < 1:
    print("Usage: locust_assert.py <stats_csv_path>")
    sys.exit(2)

path = sys.argv[-1]
with open(path, newline="") as f:
    rows = list(csv.DictReader(f))

# Szukamy wiersza zbiorczego (nazwy kolumn różnią się między wersjami)
total = None
for r in rows:
    name = r.get("Name") or r.get("Request Name") or r.get("name") or ""
    if name.strip().lower() in ("total", "aggregated", "aggregated results"):
        total = r
        break

if not total:
    # Czasem Locust nie dodaje "Total" – bierzemy sumę po wszystkich wierszach
    total = rows[-1] if rows else None

if not total:
    print("❌ Nie znaleziono danych z Locusta (pusty CSV).")
    sys.exit(1)

def get_num(d, keys, default=0.0, cast=float):
    for k in keys:
        if k in d and d[k] != "":
            try:
                return cast(str(d[k]).replace(",", "."))
            except Exception:
                pass
    return default

failures = int(get_num(total, ["# failures", "Failure Count", "failures"], 0, int))
p95 = get_num(total, ["95%", "95th percentile", "95%ile"], 0.0, float)

ok = True
if failures > 0:
    print(f"❌ Locust zgłosił błędy: failures={failures}")
    ok = False
if p95 > 500:
    print(f"❌ 95 percentyl {p95:.1f} ms > 500 ms")
    ok = False

if ok:
    print(f"✅ Locust OK: failures={failures}, p95={p95:.1f} ms")
    sys.exit(0)
else:
    sys.exit(1)
