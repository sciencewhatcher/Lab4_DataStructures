# Appendix Exercise 1: Engineering Test Data Organizer
from collections import Counter, defaultdict

# ---- Student-specific inputs ----
LAST_NAME = "GUALBERTO"
STUDENT_ID = "TUPM-26-1130"
FAVORITE_ARTIST = "Amiel Sol"
SEED_NUM = int(STUDENT_ID[-1])

letters = [c for c in FAVORITE_ARTIST.upper() if c.isalpha()]
alpha_pos = lambda ch: ord(ch) - ord("A") + 1

# Generate test data
sources = [f"{LAST_NAME}_T{n}" for n in range(1, 6)]
categories = ["TEMPERATURE", "VOLTAGE", "CURRENT", "PRESSURE", "SPEED"]

records = []
for j in range(10):
    ch = letters[j % len(letters)]
    value = SEED_NUM + alpha_pos(ch) + (j + 1)
    records.append((sources[j % 5], categories[(j * 2 + j // 5) % 5], value))
records.append(records[0])

print("=== 1. GENERATED TEST DATA ===")
for i, (s, c, v) in enumerate(records, 1):
    print(f"{i:>2}. {s:<14} {c:<12} {v}")

# Organize by source and category
organized = defaultdict(lambda: defaultdict(list))
for s, c, v in records:
    organized[s][c].append(v)

print("\n=== 2. ORGANIZED TEST DATA ===")
for s in sources:
    print(s)
    for c, vals in organized[s].items():
        print(f"   {c:<12} {vals}")

# Repeated / distinct data
repeated = [r for r, n in Counter(records).items() if n > 1]
pair_counts = Counter((s, c) for s, c, _ in records)
multi = [p for p, n in pair_counts.items() if n > 1]
print("\n=== 3. REPEATED / DISTINCT DATA ===")
print(f"Repeated records        : {repeated}")
print(f"Repeated source/category: {multi}")
print(f"Distinct sources        : {sorted({r[0] for r in records})}")
print(f"Distinct categories     : {sorted({r[1] for r in records})}")
print(f"Distinct values         : {sorted({r[2] for r in records})}")

# Numerical and categorical summaries
by_cat = defaultdict(list)
by_src = defaultdict(list)
for s, c, v in records:
    by_cat[c].append(v)
    by_src[s].append(v)

def stats(vals):
    return {"count": len(vals), "min": min(vals), "max": max(vals),
            "sum": sum(vals), "avg": round(sum(vals) / len(vals), 2)}

cat_stats = {c: stats(v) for c, v in by_cat.items()}
src_stats = {s: stats(v) for s, v in by_src.items()}
print("\n=== 4. NUMERICAL AND CATEGORICAL SUMMARIES ===")
print("By category:")
for c, st in cat_stats.items():
    print(f"   {c:<12} {st}")
print("By source:")
for s, st in src_stats.items():
    print(f"   {s:<14} {st}")
print(f"Records per category: {dict(Counter(r[1] for r in records))}")

# Processed results
all_vals = [r[2] for r in records]
unique_records = list(dict.fromkeys(records))
print("\n=== 5. PROCESSED RESULTS ===")
print(f"Total records       : {len(records)}")
print(f"Unique records      : {len(unique_records)}")
print(f"Overall sum / avg   : {sum(all_vals)} / {round(sum(all_vals)/len(all_vals), 2)}")
print(f"Overall min / max   : {min(all_vals)} / {max(all_vals)}")

# Ordered results
print("\n=== 6. ORDERED RESULTS ===")
print("Categories by average (high to low):")
for c, st in sorted(cat_stats.items(), key=lambda kv: kv[1]["avg"], reverse=True):
    print(f"   {c:<12} avg={st['avg']}")
print("Sources by total (high to low):")
for s, st in sorted(src_stats.items(), key=lambda kv: kv[1]["sum"], reverse=True):
    print(f"   {s:<14} sum={st['sum']}")
print(f"Unique records sorted by value: {sorted(unique_records, key=lambda r: r[2])}")

# Final summary
top_cat = max(cat_stats, key=lambda c: cat_stats[c]["avg"])
top_src = max(src_stats, key=lambda s: src_stats[s]["sum"])
print("\n=== 7. FINAL SUMMARY ===")
print(f"Operator: {LAST_NAME} | ID: {STUDENT_ID} | Seed: {SEED_NUM} | Artist: {FAVORITE_ARTIST}")
print(f"{len(records)} records ({len(unique_records)} unique) across "
      f"{len(src_stats)} sources and {len(cat_stats)} categories.")
print(f"Highest-average category: {top_cat} ({cat_stats[top_cat]['avg']})")
print(f"Highest-total source    : {top_src} ({src_stats[top_src]['sum']})")
print(f"Repeated record found   : {repeated[0]}")