import os

# File to store contacts
FILENAME = "contacts.txt"

# List to hold contacts
contacts = []

# Load contacts from file
def load_contacts():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            for line in file:
                name, phone = line.strip().split(",")
                contacts.append({"name": name, "phone": phone})

# Save contacts to file
def save_contacts():
    with open(FILENAME, "w") as file:
        for contact in contacts:
            file.write(f"{contact['name']},{contact['phone']}\n")

def show_menu():
    print("\n--- Contact List Manager ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")
def add_contact():
    name = input("Enter name: ").strip()

    # Check for duplicate name
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            print("A contact with this name already exists.")
            return

    # Ask for valid 8-digit phone number
    while True:
        phone = input("Enter 8-digit phone number: ").strip()

        # Check if it's digits and 8 characters
        if not (phone.isdigit() and len(phone) == 8):
            print("Invalid phone number. Please enter exactly 8 digits.")
            continue

        # Check for duplicate phone number
        for contact in contacts:
            if contact['phone'] == phone:
                print("This phone number is already in use.")
                return

        break  # Valid phone number, exit loop

    # Add contact if no duplicates
    contacts.append({"name": name, "phone": phone})
    save_contacts()
    print(f"Contact '{name}' added successfully!")



def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        print("\n--- Contact List ---")
        for i, contact in enumerate(contacts, start=1):
            print(f"{i}. {contact['name']} - {contact['phone']}")

def search_contact():
    search_name = input("Enter name to search: ").lower()
    found = False
    for contact in contacts:
        if search_name in contact['name'].lower():
            print(f"Found: {contact['name']} - {contact['phone']}")
            found = True
    if not found:
        print("Contact not found.")

def delete_contact():
    del_name = input("Enter name to delete: ").lower()
    for contact in contacts:
        if del_name == contact['name'].lower():
            contacts.remove(contact)
            save_contacts()
            print(f"Contact '{contact['name']}' deleted.")
            return
    print("Contact not found.")

# Main program
load_contacts()

while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        delete_contact()
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
