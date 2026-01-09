import os
import sys
from dotenv import load_dotenv
from vault import PasswordVault
load_dotenv()

# Soft version guard (not security, just clarity)
if sys.version_info < (3, 11):
    print("❌ Python 3.11 or higher required")
    exit(1)

vault = PasswordVault(
    os.getenv("KEY_FILE_NAME"),
    os.getenv("DATA_FILE_NAME")
)


def store_flow():
    while True:
        name = input("Enter name key: ").strip()
        email = input("Enter email: ").strip()
        password = input("Enter password: ").strip()

        print("\nConfirm details:")
        print(f"Name     : {name}")
        print(f"Email    : {email}")
        print(f"Password : {password}")

        confirm = input("Is this correct? (yes/no): ").strip().lower()

        if confirm == "yes":
            vault.add_entry(name, email, password)
            print("✅ Credentials stored securely\n")
            break
        else:
            print("🔁 Re-enter details\n")


def retrieve_flow():
    name = input("Enter name key to search: ").strip()
    result = vault.get_entry(name)

    if not result:
        print("❌ Entry not found\n")
        return

    print("\n🔐 Retrieved credentials")
    print(f"Email    : {result['email']}")
    print(f"Password : {result['password']}\n")

def list_flow():
    entries = vault.list_entries()

    if not entries:
        print("📭 No entries stored yet\n")
        return

    print("\n📂 Stored entries:")
    for idx, name in enumerate(entries, start=1):
        print(f"{idx}. {name}")
    print()

def main():
    print("1. Store credentials")
    print("2. Retrieve credentials")
    print("3. List stored entries")

    choice = input("Choose option (1/2/3): ").strip()

    if choice == "1":
        store_flow()
    elif choice == "2":
        retrieve_flow()
    elif choice == "3":
        list_flow()
    else:
        print("❌ Invalid choice\n")


if __name__ == "__main__":
    main()
