import json
import os
from cryptography.fernet import Fernet
from dotenv import load_dotenv

load_dotenv()

KEY_FILE = os.getenv("KEY_FILE_NAME")
DATA_FILE = os.getenv("DATA_FILE_NAME")

if not KEY_FILE or not DATA_FILE:
    print("❌ ENV issue: KEY_FILE_NAME or DATA_FILE_NAME missing")
    exit(1)


class PasswordVault:
    def __init__(self, key_file: str, data_file: str):
        self.key_file = key_file
        self.data_file = data_file
        self.fernet = Fernet(self._load_key())

    def _load_key(self) -> bytes:
        with open(self.key_file, "rb") as f:
            return f.read()

    def _load_data(self) -> dict:
        if not os.path.exists(self.data_file):
            return {}
        with open(self.data_file, "r") as f:
            return json.load(f)

    def _save_data(self, data: dict):
        with open(self.data_file, "w") as f:
            json.dump(data, f, indent=4)

    def encrypt(self, text: str) -> str:
        return self.fernet.encrypt(text.encode()).decode()

    def decrypt(self, text: str) -> str:
        return self.fernet.decrypt(text.encode()).decode()

    def add_entry(self, name: str, email: str, password: str):
        data = self._load_data()
        data[name.lower()] = {
            "email": self.encrypt(email),
            "password": self.encrypt(password)
        }
        self._save_data(data)

    def get_entry(self, name: str):
        data = self._load_data()
        entry = data.get(name.lower())

        if not entry:
            return None

        return {
            "email": self.decrypt(entry["email"]),
            "password": self.decrypt(entry["password"])
        }
    
    def list_entries(self):
        data = self._load_data()
        return list(data.keys())
