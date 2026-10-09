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

from collections import defaultdict

# Initialize with a default integer factory (creates a 0 for missing keys)
default_data = defaultdict(int)

# Assign a known key
default_data['active_key'] = sys_config["vector_dim"]

print(f"Existing Key Value: {default_data['active_key']}")
# Accessing an uninitialized key will not throw a KeyError
print(f"Missing Key Value (Auto-generated): {default_data['unknown_key']}")