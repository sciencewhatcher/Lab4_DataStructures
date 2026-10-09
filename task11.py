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

import array

# Initialize an integer array using the type code 'i'
number_array = array.array('i', [sys_config["base_seed"], sys_config["vector_dim"], 100])
print(f"Integer Array: {number_array}")

# Attempt to append a non-integer data type (Expected to fail)
print("\nAttempting to append a string...")
try:
    number_array.append("invalid")
except TypeError as error_msg:
    print(f"Type Error: {error_msg}")