import hashlib


def hash_file(filepath):
    hasher = hashlib.sha256()  # Create a SHA-256 hash object
    with open(filepath, "rb") as f:  # Open file in binary mode
        for chunk in iter(lambda: f.read(4096), b""):  # Read in chunks of 4096 bytes
            hasher.update(chunk)  # Update hash with chunk
    return hasher.hexdigest()  # Return the final hash as a hex string

# Define file paths
original_filepath = "original.txt"
modified_filepath = "modified.txt"

# Compute hashes
original_hash = hash_file(original_filepath)
modified_hash = hash_file(modified_filepath)

# Print hashes
print(f"Original Hash: {original_hash}")
print(f"Modified Hash: {modified_hash}")

# Compare hashes
if original_hash == modified_hash:
    print("Files are identical.")
else:
    print("Files have been modified.")