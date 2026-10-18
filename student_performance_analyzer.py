# Appendix Exercise 2: Student Performance Data Analyzer
from collections import defaultdict

# Student-specific inputs
LAST_NAME = "GUALBERTO"
STUDENT_ID = "TUPM-26-1130"
FAVORITE_ARTIST = "Amiel Sol"
SEED_NUM = int(STUDENT_ID[-1])

letters = [c for c in FAVORITE_ARTIST.upper() if c.isalpha()]
alpha_pos = lambda ch: ord(ch) - ord("A") + 1

students = [f"{LAST_NAME}_S{n}" for n in range(1, 6)]
subjects = ["PROGRAMMING", "MATHEMATICS", "ELECTRONICS", "PHYSICS", "ENGLISH"]

def category(score):
    if score >= 90: return "EXCELLENT"
    if score >= 80: return "VERY GOOD"
    if score >= 75: return "SATISFACTORY"
    return "NEEDS IMPROVEMENT"

# Generate performance records
records = []   # [student, subject, score]
for j in range(10):
    ch = letters[j % len(letters)]
    score = 60 + (SEED_NUM + alpha_pos(ch) * 7 + j * 3) % 41   # 60-100
    records.append([students[j % 5], subjects[(j * 2 + j // 5) % 5], score])
records.append(list(records[2]))            
records.append([students[4], subjects[0], None])

print("=== 1. GENERATED PERFORMANCE RECORDS ===")
for i, (st, sb, sc) in enumerate(records, 1):
    print(f"{i:>2}. {st:<14} {sb:<12} {sc if sc is not None else 'MISSING'}")

# Organize student/subject data
organized = defaultdict(dict)
repeated, incomplete = [], []
for st, sb, sc in records:
    if sc is None:
        incomplete.append((st, sb)); continue
    if sb in organized[st]:
        repeated.append((st, sb, sc)); continue
    organized[st][sb] = sc

print("\n=== 2. ORGANIZED STUDENT/SUBJECT DATA ===")
for st in students:
    print(st, dict(organized[st]))

# Repeated / incomplete
print("\n=== 3. REPEATED / INCOMPLETE RECORDS ===")
print(f"Repeated (ignored in summaries): {repeated}")
print(f"Incomplete (missing score)     : {incomplete}")

# Performance categories
print("\n=== 4. PERFORMANCE CATEGORIES ===")
for st in students:
    for sb, sc in organized[st].items():
        print(f"{st:<14} {sb:<12} {sc:>3}  {category(sc)}")

# Student and subject summaries
stud_sum, subj_scores = {}, defaultdict(list)
for st in students:
    sc = list(organized[st].values())
    best = max(organized[st], key=organized[st].get)
    stud_sum[st] = {"subjects": len(sc), "avg": round(sum(sc) / len(sc), 2),
                    "best": (best, organized[st][best])}
    for sb, v in organized[st].items():
        subj_scores[sb].append(v)
subj_sum = {sb: {"count": len(v), "avg": round(sum(v) / len(v), 2),
                 "high": max(v), "low": min(v)} for sb, v in subj_scores.items()}

print("\n=== 5. STUDENT AND SUBJECT SUMMARIES ===")
print("Students:")
for st, d in stud_sum.items(): print(f"   {st:<14} {d}")
print("Subjects:")
for sb, d in subj_sum.items(): print(f"   {sb:<12} {d}")

# Ordered results
print("\n=== 6. ORDERED RESULTS ===")
print("Student ranking (average, high to low):")
for rank, (st, d) in enumerate(sorted(stud_sum.items(), key=lambda kv: kv[1]["avg"], reverse=True), 1):
    print(f"   {rank}. {st:<14} {d['avg']}  [{category(d['avg'])}]")
print("Subjects (average, high to low):")
for sb, d in sorted(subj_sum.items(), key=lambda kv: kv[1]["avg"], reverse=True):
    print(f"   {sb:<12} {d['avg']}")

# Final report
valid = [sc for st in students for sc in organized[st].values()]
print("\n=== FINAL STUDENT PERFORMANCE REPORT ===")
print(f"Operator: {LAST_NAME} | ID: {STUDENT_ID} | Seed: {SEED_NUM} | Artist: {FAVORITE_ARTIST}")
print(f"Records generated: {len(records)} | Valid: {len(valid)} | "
      f"Repeated: {len(repeated)} | Incomplete: {len(incomplete)}")
print(f"Class average: {round(sum(valid)/len(valid), 2)} | Highest: {max(valid)} | Lowest: {min(valid)}")