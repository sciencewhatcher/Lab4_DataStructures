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

# Initialize a list with deliberate duplicate values
raw_data = [base_val, base_val + 5, base_val, sys_config["vector_dim"], base_val + 5]
print(f"Raw List (with duplicates): {raw_data}")

# Convert the list to a Set to remove duplicates
unique_data = set(raw_data)
print(f"Unique Set: {unique_data}")