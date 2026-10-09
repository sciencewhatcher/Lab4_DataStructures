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

# Create a dictionary representing a structured data payload
data_payload = {
    "identifier": sys_config["auth_id"],
    "dimension": sys_config["vector_dim"],
    "status": "active"
}

# Iterate and display key-value pairs
print("--- Payload Data ---")

for key, value in data_payload.items():
    print(f"{key.capitalize()}: {value}")

# Add a new key-value pair dynamically
data_payload["efficiency_rating"] = 98.5

print(f"\nUpdated Payload: {data_payload}")