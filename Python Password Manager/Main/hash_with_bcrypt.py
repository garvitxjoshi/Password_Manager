import bcrypt

def hash_password(plain_password: str) -> bytes:
    """
    Hash a plain password using bcrypt.
    Returns a salted hash (bytes).
    """
    password_bytes = plain_password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password_bytes, salt)
    return hashed

def check_password(plain_password: str, hashed_password: bytes) -> bool:
    """
    Verify a plain password against the stored hash.
    """
    password_bytes = plain_password.encode('utf-8')
    return bcrypt.checkpw(password_bytes, hashed_password)

# -------------------- Main function --------------------
def main():
    # Input password from user
    plain_password = input("Enter your password: ")
    
    # Show input password
    print(f"\nInput Password: {plain_password}")
    
    # Hash the password
    hashed_password = hash_password(plain_password)
    
    # Show hashed password (bytes)
    print(f"\nHashed Password (bytes): {hashed_password}")
    
    # Decode the hash to string (for storage/display)
    hashed_str = hashed_password.decode('utf-8')
    print(f"\nHashed Password (decoded string): {hashed_str}")
    
    # Encode the string back to bytes (for verification)
    hashed_bytes_again = hashed_str.encode('utf-8')
    print(f"\nHashed Password (encoded back to bytes): {hashed_bytes_again}")
    
    # Verify password using re-encoded bytes
    is_correct = check_password(plain_password, hashed_bytes_again)
    print(f"\nPassword verification result: {is_correct}")

if __name__ == "__main__":
    main()
