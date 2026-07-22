# ==========================================
# CONTACT BOOK MANAGEMENT SYSTEM
# Internship Project
# Developed in Python
# ==========================================

import json
import os

FILE_NAME = "contacts.json"


# -------------------------------
# Load Contacts
# -------------------------------
def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


# -------------------------------
# Save Contacts
# -------------------------------
def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)


# -------------------------------
# Add Contact
# -------------------------------
def add_contact(contacts):
    print("\n===== Add New Contact =====")

    name = input("Enter Name: ").strip()
    phone = input("Enter Phone Number: ").strip()
    email = input("Enter Email: ").strip()
    address = input("Enter Address: ").strip()

    # Check duplicate phone number
    for contact in contacts:
        if contact["phone"] == phone:
            print("\nContact with this phone number already exists!")
            return

    new_contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(new_contact)
    save_contacts(contacts)

    print("\nContact added successfully!")


# -------------------------------
# View Contacts
# -------------------------------
def view_contacts(contacts):
    print("\n========== Contact List ==========")

    if not contacts:
        print("No contacts found.")
        return

    print("{:<5} {:<20} {:<15}".format("No.", "Name", "Phone"))
    print("-" * 45)

    for i, contact in enumerate(contacts, start=1):
        print("{:<5} {:<20} {:<15}".format(
            i,
            contact["name"],
            contact["phone"]
        ))


# -------------------------------
# Search Contact
# -------------------------------
def search_contact(contacts):
    keyword = input("\nEnter Name or Phone Number: ").lower()

    found = False

    for contact in contacts:
        if keyword in contact["name"].lower() or keyword in contact["phone"]:
            print("\nContact Found")
            print("-" * 30)
            print("Name    :", contact["name"])
            print("Phone   :", contact["phone"])
            print("Email   :", contact["email"])
            print("Address :", contact["address"])
            found = True

    if not found:
        print("\nNo matching contact found.")


# -------------------------------
# Update Contact
# -------------------------------
def update_contact(contacts):
    phone = input("\nEnter Phone Number of Contact to Update: ")

    for contact in contacts:
        if contact["phone"] == phone:

            print("\nLeave field empty to keep old value.\n")

            new_name = input(f"Name ({contact['name']}): ")
            new_phone = input(f"Phone ({contact['phone']}): ")
            new_email = input(f"Email ({contact['email']}): ")
            new_address = input(f"Address ({contact['address']}): ")

            if new_name:
                contact["name"] = new_name

            if new_phone:
                contact["phone"] = new_phone

            if new_email:
                contact["email"] = new_email

            if new_address:
                contact["address"] = new_address

            save_contacts(contacts)

            print("\nContact updated successfully!")
            return

    print("\nContact not found.")


# -------------------------------
# Delete Contact
# -------------------------------
def delete_contact(contacts):
    phone = input("\nEnter Phone Number to Delete: ")

    for contact in contacts:
        if contact["phone"] == phone:
            contacts.remove(contact)
            save_contacts(contacts)
            print("\nContact deleted successfully!")
            return

    print("\nContact not found.")


# -------------------------------
# Main Menu
# -------------------------------
def main():

    contacts = load_contacts()

    while True:

        print("\n")
        print("=" * 45)
        print("     CONTACT BOOK MANAGEMENT SYSTEM")
        print("=" * 45)
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        print("=" * 45)

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_contact(contacts)

        elif choice == "2":
            view_contacts(contacts)

        elif choice == "3":
            search_contact(contacts)

        elif choice == "4":
            update_contact(contacts)

        elif choice == "5":
            delete_contact(contacts)

        elif choice == "6":
            print("\nThank you for using Contact Book!")
            break

        else:
            print("\nInvalid choice. Please try again.")


# -------------------------------
# Program Starts Here
# -------------------------------
if __name__ == "__main__":
    main()