LAST_NAME = "GUALBERTO"
STUDENT_ID = "TUPM-26-1130"

seed_digit = int(STUDENT_ID[-1])
id_checksum = sum(int(d) for d in STUDENT_ID if d.isdigit())
vector_dim = len(LAST_NAME)

sys_config = {
    "operator": LAST_NAME,
    "auth_id": STUDENT_ID,
    "base_seed": seed_digit,
    "checksum": id_checksum,
    "vector_dim": vector_dim,
    "status": "INITIALIZED"
}

# mmutable tuple using system parameters
fixed_coordinates = (sys_config["vector_dim"], sys_config["base_seed"], 9)

print(f"Fixed Coordinates: {fixed_coordinates}")

# Unpack the tuple into individual variables
x_val, y_val, z_val = fixed_coordinates

print(f"Unpacked Values -> X: {x_val}, Y: {y_val}, Z: {z_val}")

# Attempt to modify the tuple (Expected to fail)
print("\nAttempting modification...")

try:
    fixed_coordinates[0] = 99
except TypeError as error_msg:
    print(f"Modification Error: {error_msg}")