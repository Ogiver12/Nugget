import hashlib

print("What is expected hash from website (Source)")
expected = input("Expected Hash: ").strip()
print("What is the file path?")
path = input("File Path: ").strip().strip('"')
print(" ")

try:
      
    sha256 = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):  # Read file in chunks
                sha256.update(chunk)
        real_hash = sha256.hexdigest()

    if real_hash == expected:
        print("\033[1;32;40mThey Match!")
    else:
        print("\033[1;31;40mThey Don't Match")

except FileNotFoundError:
    print("\033[1;31;40mError: File not found.\033[0m")
except Exception as e:
    print(f"\033[1;31;40mAn error occurred: {e}\033[0m")

print(" ")
print("\033[0;37;40mPress enter to exit")
input()