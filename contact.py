import json

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, store_name, phone_number, email, address):
        contact = {
            'store_name': store_name,
            'phone_number': phone_number,
            'email': email,
            'address': address
        }
        self.contacts.append(contact)
        print("Contact added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            for idx, contact in enumerate(self.contacts, start=1):
                print(f"{idx}. {contact['store_name']} - {contact['phone_number']}")

    def search_contact(self, query):
        results = [contact for contact in self.contacts if query in contact['store_name'] or query in contact['phone_number']]
        if not results:
            print("No contacts found.")
        else:
            for contact in results:
                print(f"Store Name: {contact['store_name']}, Phone: {contact['phone_number']}, Email: {contact['email']}, Address: {contact['address']}")

    def update_contact(self, phone_number, store_name=None, new_phone_number=None, email=None, address=None):
        for contact in self.contacts:
            if contact['phone_number'] == phone_number:
                if store_name:
                    contact['store_name'] = store_name
                if new_phone_number:
                    contact['phone_number'] = new_phone_number
                if email:
                    contact['email'] = email
                if address:
                    contact['address'] = address
                print("Contact updated successfully.")
                return
        print("Contact not found.")

    def delete_contact(self, phone_number):
        for contact in self.contacts:
            if contact['phone_number'] == phone_number:
                self.contacts.remove(contact)
                print("Contact deleted successfully.")
                return
        print("Contact not found.")

def main():
    manager = ContactManager()
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            store_name = input("Enter store name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            manager.add_contact(store_name, phone_number, email, address)
        elif choice == '2':
            manager.view_contacts()
        elif choice == '3':
            query = input("Enter name or phone number to search: ")
            manager.search_contact(query)
        elif choice == '4':
            phone_number = input("Enter the phone number of the contact to update: ")
            store_name = input("Enter new store name (leave blank to keep current): ")
            new_phone_number = input("Enter new phone number (leave blank to keep current): ")
            email = input("Enter new email (leave blank to keep current): ")
            address = input("Enter new address (leave blank to keep current): ")
            manager.update_contact(phone_number, store_name or None, new_phone_number or None, email or None, address or None)
        elif choice == '5':
            phone_number = input("Enter the phone number of the contact to delete: ")
            manager.delete_contact(phone_number)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

import json

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, store_name, phone_number, email, address):
        contact = {
            'store_name': store_name,
            'phone_number': phone_number,
            'email': email,
            'address': address
        }
        self.contacts.append(contact)
        print("Contact added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            for idx, contact in enumerate(self.contacts, start=1):
                print(f"{idx}. {contact['store_name']} - {contact['phone_number']}")

    def search_contact(self, query):
        results = [contact for contact in self.contacts if query in contact['store_name'] or query in contact['phone_number']]
        if not results:
            print("No contacts found.")
        else:
            for contact in results:
                print(f"Store Name: {contact['store_name']}, Phone: {contact['phone_number']}, Email: {contact['email']}, Address: {contact['address']}")

    def update_contact(self, phone_number, store_name=None, new_phone_number=None, email=None, address=None):
        for contact in self.contacts:
            if contact['phone_number'] == phone_number:
                if store_name:
                    contact['store_name'] = store_name
                if new_phone_number:
                    contact['phone_number'] = new_phone_number
                if email:
                    contact['email'] = email
                if address:
                    contact['address'] = address
                print("Contact updated successfully.")
                return
        print("Contact not found.")

    def delete_contact(self, phone_number):
        for contact in self.contacts:
            if contact['phone_number'] == phone_number:
                self.contacts.remove(contact)
                print("Contact deleted successfully.")
                return
        print("Contact not found.")

def main():
    manager = ContactManager()
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            store_name = input("Enter store name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            manager.add_contact(store_name, phone_number, email, address)
        elif choice == '2':
            manager.view_contacts()
        elif choice == '3':
            query = input("Enter name or phone number to search: ")
            manager.search_contact(query)
        elif choice == '4':
            phone_number = input("Enter the phone number of the contact to update: ")
            store_name = input("Enter new store name (leave blank to keep current): ")
            new_phone_number = input("Enter new phone number (leave blank to keep current): ")
            email = input("Enter new email (leave blank to keep current): ")
            address = input("Enter new address (leave blank to keep current): ")
            manager.update_contact(phone_number, store_name or None, new_phone_number or None, email or None, address or None)
        elif choice == '5':
            phone_number = input("Enter the phone number of the contact to delete: ")
            manager.delete_contact(phone_number)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

import json

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, store_name, phone_number, email, address):
        contact = {
            'store_name': store_name,
            'phone_number': phone_number,
            'email': email,
            'address': address
        }
        self.contacts.append(contact)
        print("Contact added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            for idx, contact in enumerate(self.contacts, start=1):
                print(f"{idx}. {contact['store_name']} - {contact['phone_number']}")

    def search_contact(self, query):
        results = [contact for contact in self.contacts if query in contact['store_name'] or query in contact['phone_number']]
        if not results:
            print("No contacts found.")
        else:
            for contact in results:
                print(f"Store Name: {contact['store_name']}, Phone: {contact['phone_number']}, Email: {contact['email']}, Address: {contact['address']}")

    def update_contact(self, phone_number, store_name=None, new_phone_number=None, email=None, address=None):
        for contact in self.contacts:
            if contact['phone_number'] == phone_number:
                if store_name:
                    contact['store_name'] = store_name
                if new_phone_number:
                    contact['phone_number'] = new_phone_number
                if email:
                    contact['email'] = email
                if address:
                    contact['address'] = address
                print("Contact updated successfully.")
                return
        print("Contact not found.")

    def delete_contact(self, phone_number):
        for contact in self.contacts:
            if contact['phone_number'] == phone_number:
                self.contacts.remove(contact)
                print("Contact deleted successfully.")
                return
        print("Contact not found.")

def main():
    manager = ContactManager()
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            store_name = input("Enter store name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            manager.add_contact(store_name, phone_number, email, address)
        elif choice == '2':
            manager.view_contacts()
        elif choice == '3':
            query = input("Enter name or phone number to search: ")
            manager.search_contact(query)
        elif choice == '4':
            phone_number = input("Enter the phone number of the contact to update: ")
            store_name = input("Enter new store name (leave blank to keep current): ")
            new_phone_number = input("Enter new phone number (leave blank to keep current): ")
            email = input("Enter new email (leave blank to keep current):")
            address = input("Enter new address (leave blank to keep current):")
            manager.update_contact(phone_number, store_name or None, new_phone_number or None, email or None, address or None)
        elif choice == '5':
            phone_number = input("Enter the phone number of the contact to delete: ")
            manager.delete_contact(phone_number)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()





