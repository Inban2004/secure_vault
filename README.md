# Local Password Vault 🔐

A simple, secure command-line password vault built in Python.

Uses Fernet encryption to store credentials locally in an encrypted JSON file.
Perfect for learning symmetric encryption or managing personal logins offline.
⚠️ Always backup your secret.key safely—it's required to decrypt your data!

## Features
- Generate a secure encryption key (one-time)
- Store credentials (name, email, password) with strong symmetric encryption
- Retrieve or list entries via simple CLI menu
- Configurable file names via `.env`
- No external dependencies beyond standard libs

## Quick Start

1. **Clone and install dependencies**
   ```bash
   git clone ''url''
   cd your-repo-name
   pip install cryptography python-dotenv
   
2. **Need this files name**
     secret.key
     passwords.json
   
**Fully one line terminal useage for fun**
    
