import json
import os
from hash_with_bcrypt import hash_password, check_password

USERS_FILE = "users.json"

def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return {}

def save_users(data):
    with open(USERS_FILE, "w") as file:
        json.dump(data, file, indent=4)

def register_user():
    data = load_users()
    username = input("Enter new username: ")
    if username in data:
        print("❌ Username already exists!")
        return
    password = input("Enter password: ")
    master_password = input("Set your master password: ")
    hashed_pw = hash_password(password).decode('utf-8') # Store as UTF-8 string for JSON
    data[username] = {
        "password": hashed_pw,
        "master_password": master_password
    }
    save_users(data)
    print(f"✅ User '{username}' registered!")

def login_user():
    data = load_users()
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in data and check_password(password, data[username]["password"].encode()):
        print(f"✅ Welcome back, {username}!")
        master_password = input("Enter your master password to access accounts: ")
        if master_password == data[username]["master_password"]:
            return True, username, master_password
        else:
            print("❌ Incorrect master password!")
            return False, None, None
    print("❌ Invalid credentials!")
    return False, None, None

def delete_user_account():
    data = load_users()
    username = input("Enter username to delete: ")
    password = input("Enter password: ")
    if username in data and check_password(password, data[username]["password"].encode()):
        del data[username]
        save_users(data)
        print(f"🗑️ User '{username}' deleted!")
    else:
        print("❌ Invalid credentials!")

def update_user_password():
    data = load_users()
    username = input("Enter username to update: ")
    old_pass = input("Enter current password: ")
    if username in data and check_password(old_pass, data[username]["password"].encode()):
        new_pass = input("Enter new password: ")
        data[username]["password"] = hash_password(new_pass).decode('utf-8')
        save_users(data)
        print(f"🔑 Password for '{username}' updated!")
    else:
        print("❌ Invalid credentials!")
