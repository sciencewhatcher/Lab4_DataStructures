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

from collections import deque

# Initialize a double-ended queue
data_queue = deque([sys_config["base_seed"], sys_config["vector_dim"]])
print(f"Initial Deque: {data_queue}")

# Append to both ends
data_queue.append(100)
data_queue.appendleft(200)
print(f"After Appends: {data_queue}")