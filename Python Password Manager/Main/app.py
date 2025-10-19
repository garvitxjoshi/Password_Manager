from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from login import load_users, save_users, register_user, login_user, delete_user_account, update_user_password
from functions import load_accounts, save_accounts, add_account, update_account, delete_account_file, view_accounts
from AES import encrypt, decrypt

app = Flask(__name__)
CORS(app)  # Enable CORS for JS fetch calls

# Serve the main page
@app.route('/')
def index():
    return render_template('index.html')

# API to register user
@app.route('/api/register', methods=['POST'])
def api_register():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    users = load_users()
    if username in users:
        return jsonify({'success': False, 'message': 'Username already exists'})
    users[username] = password  # Store password hash already done in frontend? Better hash here
    save_users(users)
    return jsonify({'success': True, 'message': 'Account created'})

# API to login user
@app.route('/api/login', methods=['POST'])
def api_login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    users = load_users()
    if username not in users:
        return jsonify({'success': False, 'message': 'User not found'})
    # You should verify password with bcrypt here (decode would be needed)
    stored_hash = users[username].encode('utf-8')
    from hash_with_bcrypt import check_password
    if not check_password(password, stored_hash):
        return jsonify({'success': False, 'message': 'Incorrect password'})
    return jsonify({'success': True, 'message': 'Logged in'})

# API to add account password for user
@app.route('/api/account/add', methods=['POST'])
def api_add_account():
    data = request.json
    username = data.get('username')
    site = data.get('site')
    site_username = data.get('site_username')
    site_password = data.get('site_password')

    # Encrypt password before saving
    master_password = data.get('master_password')
    encrypted_password = encrypt(site_password, master_password)

    accounts = load_accounts()
    if username not in accounts:
        accounts[username] = {}
    accounts[username][site] = encrypted_password
    save_accounts(accounts)
    return jsonify({'success': True, 'message': 'Account added'})

# API to get all accounts for user (returns decrypted passwords) - secure with master password
@app.route('/api/accounts/<username>', methods=['POST'])
def api_get_accounts(username):
    data = request.json
    master_password = data.get('master_password')
    accounts = load_accounts()
    if username not in accounts:
        return jsonify({'success': True, 'accounts': {}})
    decrypted_accounts = {}
    for site, enc_pass in accounts[username].items():
        try:
            decrypted = decrypt(enc_pass, master_password)
            decrypted_accounts[site] = decrypted
        except Exception:
            decrypted_accounts[site] = '***'  # Cannot decrypt with wrong master password
    return jsonify({'success': True, 'accounts': decrypted_accounts})

if __name__ == '__main__':
    app.run(port=8080, debug=True)

