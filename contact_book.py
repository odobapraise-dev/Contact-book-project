# contact_book.py
import json
import os

# file where contacts will be saved (in the same folder as this script)
CONTACTS_FILE = "contacts.json"


# ---------- Persistence helpers ----------
def load_contacts():
    """Load contacts from disk. Returns a dict name -> phone."""
    if os.path.exists(CONTACTS_FILE):
        try:
            with open(CONTACTS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            # If file is corrupted or not valid JSON, start fresh
            print("Warning: couldn't read contacts file, starting with empty contacts.")
            return {}
    return {}


def save_contacts(contacts):
    """Save contacts dict to disk as JSON."""
    with open(CONTACTS_FILE, "w", encoding="utf-8") as f:
        json.dump(contacts, f, ensure_ascii=False, indent=2)


# ---------- Contact operations ----------
def add_contact(contacts):
    """Add or update a contact (name -> phone)."""
    name = input("Enter full name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    phone = input("Enter phone number: ").strip()
    if not phone:
        print("Phone cannot be empty.")
        return

    if name in contacts:
        print(f"{name} already exists with phone: {contacts[name]}")
        if input("Overwrite? (y/n): ").strip().lower() != "y":
            print("Cancelled.")
            return

    contacts[name] = phone
    save_contacts(contacts)
    print(f"Saved: {name} -> {phone}")


def view_contacts(contacts):
    """Print all contacts in a numbered list."""
    if not contacts:
        print("No contacts yet.")
        return

    print("\nContacts:")
    for i, (name, phone) in enumerate(contacts.items(), start=1):
        print(f"{i}. {name} — {phone}")


def search_contacts(contacts):
    """Search contacts by name or phone (partial match)."""
    q = input("Search (name or phone): ").strip().lower()
    if not q:
        print("Empty search.")
        return

    results = []
    for name, phone in contacts.items():
        if q in name.lower() or q in phone.lower():
            results.append((name, phone))

    if not results:
        print("No matches found.")
        return

    print("\nSearch results:")
    for i, (name, phone) in enumerate(results, start=1):
        print(f"{i}. {name} — {phone}")


def delete_contact(contacts):
    """Delete a contact by number or exact name."""
    if not contacts:
        print("No contacts to delete.")
        return

    view_contacts(contacts)
    key = input("Enter contact number or exact name to delete: ").strip()
    if not key:
        return

    # if user typed a number, delete by index
    if key.isdigit():
        idx = int(key)
        if 1 <= idx <= len(contacts):
            name = list(contacts.keys())[idx - 1]
            if input(f"Delete {name}? (y/n): ").strip().lower() == "y":
                del contacts[name]
                save_contacts(contacts)
                print(f"{name} deleted.")
            else:
                print("Cancelled.")
        else:
            print("Invalid number.")
        return

    # otherwise treat input as exact name
    if key in contacts:
        if input(f"Delete {key}? (y/n): ").strip().lower() == "y":
            del contacts[key]
            save_contacts(contacts)
            print(f"{key} deleted.")
        else:
            print("Cancelled.")
    else:
        print("Contact not found.")


# ---------- Main program ----------
def main():
    contacts = load_contacts()

    while True:
        print("\n--- Contact Book ---")
        print("1. Add contact")
        print("2. View all contacts")
        print("3. Search contacts")
        print("4. Delete contact")
        print("5. Quit")

        choice = input("Choose (1-5): ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contacts(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("Bye 👋 — contacts saved to", CONTACTS_FILE)
            break
        else:
            print("Invalid choice, please enter 1-5.")


if __name__ == "__main__":
    main()
