🔐 Command-Line Password Manager

A secure, local password manager that runs in your terminal. This project allows users to register, log in, and securely store their account passwords. All sensitive information is encrypted using AES, and user login credentials are protected with bcrypt hashing.

✨ Features

User Authentication: Securely register, log in, update, or delete your user account.

CRUD Operations for Passwords:

Add: Save new account credentials (e.g., website, username, password).

View: Display all saved account passwords after decrypting them with your master password.

Update: Modify the password for an existing account.

Delete: Remove a saved account entry.

Strong Security:

AES Encryption: All saved account passwords are encrypted using AES-256. They can only be decrypted with your unique master password.

Bcrypt Hashing: Your main login password is never stored in plaintext. It is hashed using bcrypt, a strong and slow hashing algorithm designed to resist brute-force attacks.

Password Utilities:

Password Generator: Create strong, random passwords of a specified length.

Strength Checker: Evaluate the strength of your passwords based on length, character variety, and common patterns.

Web API (Optional): Includes a basic Flask server (app.py) to expose the core functionalities through a REST API, providing a backend for a potential web or desktop client.

🛠️ Core Technologies & Libraries

Python 3

cryptography: For robust AES encryption and key derivation.

bcrypt: For hashing user passwords securely.

Flask: (Optional) For the web API.

📂 Project Structure

Here is a breakdown of the key files in this project:

File

Description

Main.py

The main entry point to run the command-line interface (CLI) of the password manager.

login.py

Handles all user authentication logic: registration, login, user deletion, and password updates.

functions.py

Manages the core password storage features: adding, viewing, updating, and deleting account credentials.

AES.py

Contains the functions for AES encryption and decryption of account passwords.

hash_with_bcrypt.py

Implements password hashing and verification using the bcrypt library.

random_pass.py

A utility class to generate strong, random passwords.

password_strength.py

A utility to check the strength of a given password and provide a verdict.

app.py

A simple Flask web server that provides an API for the manager's functions.

users.json

(Generated) Stores registered user data, including hashed passwords.

secured.json

(Generated) Stores the encrypted account credentials for each user.

🚀 Setup and Installation

To get this project up and running on your local machine, follow these steps.

Clone the Repository

git clone [https://github.com/your-username/password-manager.git](https://github.com/your-username/password-manager.git)
cd password-manager


Create a Virtual Environment (Recommended)

# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate


Install Dependencies
Create a file named requirements.txt and add the following lines:

cryptography
bcrypt
flask
flask-cors


Then, install them using pip:

pip install -r requirements.txt


💻 How to Use

Command-Line Interface (CLI)

This is the primary way to interact with the password manager.

Run the Main.py script from your terminal:

python Main.py


You will be greeted with a menu to register a new user or log in to an existing account. Once logged in, you can manage your passwords.

Web API (Optional)

If you wish to run the backend server for a potential UI, run the app.py script:

python app.py


The Flask API will start, typically on http://127.0.0.1:8080. You can then interact with it using API clients like Postman or by building a front-end application.

🛡️ Security Considerations

Master Password: Your master password is the single key used to encrypt and decrypt your stored account passwords. It is never stored anywhere. If you forget your master password, your stored data will be irrecoverable.

Hashing vs. Encryption:

Your main login password is hashed. This is a one-way process. We can verify if you entered the correct password, but we can't recover it.

Your stored account passwords are encrypted. This is a two-way process that can be reversed, but only with your master password.

Local Storage: All data (users.json, secured.json) is stored locally on your machine.

