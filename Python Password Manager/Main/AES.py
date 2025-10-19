import base64
import os
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes, padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

backend = default_backend()

# ----------------- Functions -----------------
def derive_key(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100_000,
        backend=backend
    )
    return kdf.derive(password.encode())

def encrypt(plaintext: str, master_password: str) -> str:
    salt = os.urandom(16)
    key = derive_key(master_password, salt)
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    encryptor = cipher.encryptor()
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_plaintext = padder.update(plaintext.encode()) + padder.finalize()
    ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()
    return base64.b64encode(iv + ciphertext + salt).decode()

def decrypt(b64_encoded_ciphertext: str, master_password: str) -> str:
    data = base64.b64decode(b64_encoded_ciphertext)
    iv = data[:16]
    salt = data[-16:]
    ciphertext = data[16:-16]
    key = derive_key(master_password, salt)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    decryptor = cipher.decryptor()
    padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()
    return plaintext.decode()

# ----------------- Main Function -----------------
def main():
    # 1. Input plaintext and master password
    plaintext = input("Enter the plaintext message: ")
    master_password = input("Enter the master password: ")

    # 2. Encrypt the message
    encrypted_message = encrypt(plaintext, master_password)
    print(f"\nEncrypted message (Base64): {encrypted_message}")

    # 3. Decrypt the message
    decrypted_message = decrypt(encrypted_message, master_password)
    print(f"\nDecrypted message: {decrypted_message}")

if __name__ == "__main__":
    main()
