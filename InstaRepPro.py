from cryptography.fernet import Fernet
import os

# Load the encrypted code and key
with open("SourceCode.bin", "rb") as f:
    encrypted_code = f.read()

# Prompt for the password to derive the key
password = input("Enter the password to decrypt the code: ")
# In a real scenario, you'd derive the key from the password (e.g., using PBKDF2)
# For simplicity, we'll assume the key file is provided and password validates it
with open("SourceKey.key", "rb") as f:
    key = f.read()
cipher = Fernet(key)

try:
    # Decrypt the code
    decrypted_code = cipher.decrypt(encrypted_code).decode()
    # Execute the decrypted code
    exec(decrypted_code)
except Exception as e:
    print(f"Decryption or execution failed: {e}")
    exit()