# Password Manager

A simple local password vault for educational purposes. Stores credentials securely using `cryptography.Fernet` encryption. Includes `key_manager.py` to generate/manage encryption keys and `vault.py` to add/retrieve passwords.

> ⚠️ **Note:** This is for learning purposes only. For production, use a vetted password manager like Bitwarden or 1Password.

---

## Features

- Securely store credentials with symmetric encryption  
- Manage encryption keys with `key_manager.py`  
- Add, view, and retrieve passwords from `vault.py`  
- Lightweight and easy to understand  

---

## Setup

1. **Create and activate a virtual environment:**

```bash
python3 -m venv .venv
source .venv/bin/activate        # Linux/macOS
# or
.venv\Scripts\activate           # Windows
```
### Install dependencies:

```bash 
pip install -r requirements.txt
```


#### requirements.txt:

```bash 
cryptography
```

## Usage
### Key management

**Generate a new encryption key:**
```bash
python key_manager.py generate
```
**Load or display the current key:**
```bash
python key_manager.py show
```

### Vault management

**Add a new password:**
```bash
python vault.py add "example.com" "username" "password123"
```
**Retrieve a password:**
```bash
python vault.py get "example.com"
```

**List all stored entries:**
```bash
python vault.py list
```
### Security Notes

- Keys are stored locally. Keep them safe!

- Credentials are encrypted with Fernet.

- Do not use this for critical or production passwords