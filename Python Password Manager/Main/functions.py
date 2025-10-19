import json
import os
from AES import encrypt, decrypt

SECURED_FILE = "secured.json"

def load_accounts():
    if not os.path.exists(SECURED_FILE):
        return {}
    with open(SECURED_FILE, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return {}

def save_accounts(data):
    with open(SECURED_FILE, "w") as file:
        json.dump(data, file, indent=4)

def add_account(username, master_password):
    data = load_accounts()
    if username not in data:
        data[username] = {}
    acc = input("Enter Account Name: ")
    password = input("Enter Account Password: ")
    encrypted_password = encrypt(password, master_password)
    data[username][acc] = encrypted_password
    save_accounts(data)
    print(f"✅ Account '{acc}' added successfully!")

def update_account(username, master_password):
    data = load_accounts()
    if username not in data or not data[username]:
        print("❌ No accounts found.")
        return
    acc = input("Enter Account Name to Update: ")
    if acc in data[username]:
        old_pass = input("Enter Current Password: ")
        decrypted_password = decrypt(data[username][acc], master_password)
        if decrypted_password == old_pass:
            new_pass = input("Enter New Password: ")
            encrypted_new_pass = encrypt(new_pass, master_password)
            data[username][acc] = encrypted_new_pass
            save_accounts(data)
            print(f"🔑 Password for '{acc}' updated successfully!")
        else:
            print("❌ Wrong Current Password!")
    else:
        print("❌ Account Not Found!")

def delete_account_file(username, master_password):
    data = load_accounts()
    if username not in data or not data[username]:
        print("❌ No accounts found.")
        return
    acc = input("Enter Account Name to Delete: ")
    if acc in data[username]:
        confirm = input("Enter Password to Confirm: ")
        decrypted_password = decrypt(data[username][acc], master_password)
        if decrypted_password == confirm:
            del data[username][acc]
            save_accounts(data)
            print(f"🗑️ Account '{acc}' deleted successfully!")
        else:
            print("❌ Wrong Password!")
    else:
        print("❌ Account Not Found!")

def view_accounts(username, master_password):
    data = load_accounts()
    if username not in data or not data[username]:
        print("📂 No accounts saved yet.")
        return
    print("\n--- Saved Accounts ---")
    for account, encrypted_password in data[username].items():
        password = decrypt(encrypted_password, master_password)
        print(f"🔹 {account} : {password}")
