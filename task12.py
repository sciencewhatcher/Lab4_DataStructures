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

#Generate a sequence dynamically
generated_list = [x * base_val for x in range(1, 6)]
filtered_list = [x for x in generated_list if x > 15]
print(f"Generated Comprehension (Values > 15): {filtered_list}")
