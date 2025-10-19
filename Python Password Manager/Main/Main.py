from login import register_user, login_user, delete_user_account, update_user_password
from functions import add_account, update_account, delete_account_file, view_accounts

def main():
    while True:
        print("\n=== 🔐 PASSWORD MANAGER SYSTEM ===")
        print("1️⃣  Register")
        print("2️⃣  Login")
        print("3️⃣  Delete User Account")
        print("4️⃣  Update User Password")
        print("5️⃣  Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice == "1":
            register_user()
        elif choice == "2":
            success, username, master_password = login_user()
            if success:
                while True:
                    print("\n=== 🔐 PASSWORD MANAGER MENU ===")
                    print("1️⃣  Add Account")
                    print("2️⃣  Update Account Password")
                    print("3️⃣  Delete Account")
                    print("4️⃣  View All Accounts")
                    print("5️⃣  Logout")

                    ch = input("Enter Your Choice (1-5): ")

                    if ch == "1":
                        add_account(username, master_password)
                    elif ch == "2":
                        update_account(username, master_password)
                    elif ch == "3":
                        delete_account_file(username, master_password)
                    elif ch == "4":
                        view_accounts(username, master_password)
                    elif ch == "5":
                        print("👋 Logging out...")
                        break
                    else:
                        print("❌ Invalid choice. Please enter between 1-5.")
        elif choice == "3":
            delete_user_account()
        elif choice == "4":
            update_user_password()
        elif choice == "5":
            print("👋 Exiting Password Manager... Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter between 1-5.")

if __name__ == "__main__":
    main()
