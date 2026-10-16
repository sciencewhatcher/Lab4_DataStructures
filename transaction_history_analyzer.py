# Appendix Exercise 3: Transaction History Analyzer
from collections import defaultdict, Counter

# Student-specific inputs
LAST_NAME = "GUALBERTO"
STUDENT_ID = "TUPM-26-1130"
FAVORITE_ARTIST = "Amiel Sol"        
SEED_NUM = int(STUDENT_ID[-1])

letters = [c for c in FAVORITE_ARTIST.upper() if c.isalpha()]
alpha_pos = lambda ch: ord(ch) - ord("A") + 1

customers = [f"{LAST_NAME}_C{n}" for n in range(1, 6)]
prices = {"NOTEBOOK": 45.00, "PEN": 12.50, "USB": 250.00,
          "HEADPHONES": 600.00, "CALCULATOR": 350.00}
products = list(prices)

# Generate transactions
transactions = []  
for j in range(10):
    ch = letters[j % len(letters)]
    qty = SEED_NUM + (alpha_pos(ch) % 9) + 1
    transactions.append((customers[j % 5], products[(j + j // 5) % 5], qty))
c0, p0, q0 = transactions[0]
transactions.append((c0, p0, q0 + 1)) 

print("=== 1. GENERATED TRANSACTION RECORDS ===")
for i, (c, p, q) in enumerate(transactions, 1):
    print(f"{i:>2}. {c:<14} {p:<11} qty={q:<2} price={prices[p]:>7.2f}")

# Organize and compute values
table = [{"customer": c, "product": p, "qty": q, "price": prices[p],
          "value": round(q * prices[p], 2)} for c, p, q in transactions]
grand_total = round(sum(r["value"] for r in table), 2)

print("\n=== 2. ORGANIZED TRANSACTION DATA ===")
for r in table:
    print(r)

print("\n=== 4. TRANSACTION VALUES ===")
for i, r in enumerate(table, 1):
    print(f"{i:>2}. {r['customer']:<14} {r['product']:<11} {r['qty']} x {r['price']:.2f} = {r['value']:.2f}")
print(f"Overall dataset total: {grand_total:.2f}")

# Repeated / distinct
pair_counts = Counter((r["customer"], r["product"]) for r in table)
repeats = {k: n for k, n in pair_counts.items() if n > 1}
print("\n=== 3. REPEATED / DISTINCT TRANSACTIONS ===")
print(f"Repeated customer-product purchases: {repeats}")
print(f"Distinct customers: {sorted({r['customer'] for r in table})}")
print(f"Distinct products : {sorted({r['product'] for r in table})}")

# Customer and product summaries
cust = defaultdict(lambda: {"transactions": 0, "items": 0, "spent": 0.0})
prod = defaultdict(lambda: {"transactions": 0, "units": 0, "revenue": 0.0})
for r in table:
    c, p = cust[r["customer"]], prod[r["product"]]
    c["transactions"] += 1; c["items"] += r["qty"]; c["spent"] = round(c["spent"] + r["value"], 2)
    p["transactions"] += 1; p["units"] += r["qty"]; p["revenue"] = round(p["revenue"] + r["value"], 2)

print("\n=== 5. CUSTOMER SUMMARIES ===")
for k, v in cust.items(): print(f"   {k:<14} {v}")
print("\n=== 6. PRODUCT SUMMARIES ===")
for k, v in prod.items(): print(f"   {k:<11} {v}")

# Ordered results
print("\n=== 7. ORDERED RESULTS ===")
print("Customers by total spent (high to low):")
for k, v in sorted(cust.items(), key=lambda kv: kv[1]["spent"], reverse=True):
    print(f"   {k:<14} {v['spent']:.2f}")
print("Products by revenue (high to low):")
for k, v in sorted(prod.items(), key=lambda kv: kv[1]["revenue"], reverse=True):
    print(f"   {k:<11} {v['revenue']:.2f}")
print("Transactions by value (high to low):")
for r in sorted(table, key=lambda r: r["value"], reverse=True)[:5]:
    print(f"   {r['customer']:<14} {r['product']:<11} {r['value']:.2f}")

# Overall summary / final report
top_c = max(cust, key=lambda k: cust[k]["spent"])
top_p = max(prod, key=lambda k: prod[k]["revenue"])
print("\n=== 8. OVERALL TRANSACTION SUMMARY / FINAL REPORT ===")
print(f"Operator: {LAST_NAME} | ID: {STUDENT_ID} | Seed: {SEED_NUM} | Artist: {FAVORITE_ARTIST}")
print(f"Transactions: {len(table)} | Total value: {grand_total:.2f} | "
      f"Average per transaction: {grand_total/len(table):.2f}")
print(f"Top customer: {top_c} ({cust[top_c]['spent']:.2f})")
print(f"Top product : {top_p} ({prod[top_p]['revenue']:.2f})")
print(f"Repeated purchase: {list(repeats)[0]}")