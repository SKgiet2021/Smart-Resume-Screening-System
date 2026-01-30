# =============================================
# 🐛 test_bugs.py - Intentionally Buggy Code
# Use this file to test VertexRabbit's detection
# =============================================

import time
import pickle
import base64
import requests

# ---------------------------------------------
# 🔥 Bug 1: SQL Injection
# ---------------------------------------------
def get_user(user_id):
    """VULNERABLE: User input directly in SQL query"""
    query = f"SELECT * FROM users WHERE id = {user_id}"
    return db.execute(query)


# ---------------------------------------------
# 🔥 Bug 2: Hardcoded API Key
# ---------------------------------------------
def fetch_weather():
    """VULNERABLE: Secret key exposed in source code"""
    headers = {"Authorization": "Bearer sk-live-a1b2c3d4e5f6g7h8i9j0"}
    return requests.get("https://api.weather.io/v1/forecast", headers=headers)


# ---------------------------------------------
# 🔥 Bug 3: Race Condition
# ---------------------------------------------
balance = 1000

def withdraw(amount):
    """VULNERABLE: Check-then-act with time gap allows double-withdrawal"""
    global balance
    if balance >= amount:
        time.sleep(0.1)  # Time gap here!
        balance -= amount
        return True
    return False


# ---------------------------------------------
# 🔥 Bug 4: Path Traversal
# ---------------------------------------------
def download_file(filename):
    """VULNERABLE: User can pass '../../../etc/passwd'"""
    return open(f"/uploads/{filename}", "rb").read()


# ---------------------------------------------
# 🔥 Bug 5: Insecure Deserialization (RCE)
# ---------------------------------------------
def load_session(data):
    """VULNERABLE: Pickle allows Remote Code Execution"""
    return pickle.loads(base64.b64decode(data))


# ---------------------------------------------
# 🔥 Bug 6: Missing Error Handling
# ---------------------------------------------
def process_payment(card_number, amount):
    """VULNERABLE: No error handling - PCI-DSS violation"""
    response = stripe.charge(card_number, amount)
    # What if payment fails? Email still sends!
    send_confirmation_email()
    update_inventory()


# ---------------------------------------------
# 🔥 Bug 7: Weak Password Hashing
# ---------------------------------------------
import hashlib

def store_password(password):
    """VULNERABLE: MD5 is cryptographically broken"""
    return hashlib.md5(password.encode()).hexdigest()


# ---------------------------------------------
# 🔥 Bug 8: Command Injection
# ---------------------------------------------
import os

def ping_host(hostname):
    """VULNERABLE: User input passed to shell command"""
    os.system(f"ping -c 4 {hostname}")
