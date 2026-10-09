# Student Identity
LAST_NAME = "GUALBERTO"
STUDENT_ID = "TUPM-26-1130"

# Derive computational parameters
seed_digit = int(STUDENT_ID[-1])
id_checksum = sum(int(d) for d in STUDENT_ID if d.isdigit())
vector_dim = len(LAST_NAME)

# Encapsulate state into a Dictionary
sys_config = {
    "operator": LAST_NAME,
    "auth_id": STUDENT_ID,
    "base_seed": seed_digit,
    "checksum": id_checksum,
    "vector_dim": vector_dim,
    "status": "INITIALIZED"
}

base_val = sys_config["base_seed"]

# Re-create the unique set from Task 9
raw_data = [
    base_val,
    base_val + 5,
    base_val,
    sys_config["vector_dim"],
    base_val + 5
]

unique_data = set(raw_data)

# Define a secondary reference set for comparison
reference_set = {base_val, base_val + 10, base_val + 20}
print(f"Reference Set: {reference_set}")

# Perform mathematical intersections and unions
common_elements = unique_data.intersection(reference_set)
combined_elements = unique_data.union(reference_set)

print(f"Intersection (Common): {common_elements}")
print(f"Union (Combined): {combined_elements}")