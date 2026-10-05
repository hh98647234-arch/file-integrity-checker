import hashlib
import os
def calculate_hash(filename):
    sha256 = hashlib.sha256()

    with open(filename, "rb") as file:
        while True:
            data = file.read(4096)

            if not data:
             break
            sha256.update(data) 
        return sha256.hexdigest()
filename = input("Enter file name: ")
if not os.path.exists(filename):
    print("ERROR: File not found!")
else:
    current_hash = calculate_hash(filename)
    hash_file = filename + ".hash"
    if not os.path.exists(hash_file):
        with open(hash_file, "w") as file:
            file.write(current_hash)
        print("Baseline hash saved.")
        print("SHA-256:", current_hash)
    else:
        with open(hash_file, "r") as file:
            saved_hash = file.read().strip()
        print("saved hash: ", saved_hash)
        print("current hash:", current_hash)
        if current_hash == saved_hash:
            print("SAFE: File has not been modified.")
        else:
            print("WARNING: FILE MODIFIED!")