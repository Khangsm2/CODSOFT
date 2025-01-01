class Contact:
    """Class to represent a contact."""
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}, Address: {self.address}"


class ContactManager:
    """Class to manage contacts."""
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        """Add a new contact."""
        contact = Contact(name, phone, email, address)
        self.contacts.append(contact)
        print("Contact added successfully.")

    def view_contacts(self):
        """View all contacts."""
        if not self.contacts:
            print("No contacts found.")
        else:
            print("\nContact List:")
            for i, contact in enumerate(self.contacts, start=1):
                print(f"{i}. {contact.name} - {contact.phone}")
        print()

    def search_contact(self, keyword):
        """Search for a contact by name or phone number."""
        results = [contact for contact in self.contacts if keyword.lower() in contact.name.lower() or keyword in contact.phone]
        if not results:
            print("No matching contacts found.")
        else:
            print("\nSearch Results:")
            for contact in results:
                print(contact)
        print()

    def update_contact(self, name):
        """Update a contact's details."""
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print("Contact found. Enter new details.")
                contact.phone = input("Phone: ")
                contact.email = input("Email: ")
                contact.address = input("Address: ")
                print("Contact updated successfully.")
                return
        print("Contact not found.")

    def delete_contact(self, name):
        """Delete a contact by name."""
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print("Contact deleted successfully.")
                return
        print("Contact not found.")


def main():
    manager = ContactManager()
    while True:
        print("\n--- Contact Management System ---")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                name = input("Name: ")
                phone = input("Phone: ")
                email = input("Email: ")
                address = input("Address: ")
                manager.add_contact(name, phone, email, address)
            elif choice == 2:
                manager.view_contacts()
            elif choice == 3:
                keyword = input("Enter name or phone to search: ")
                manager.search_contact(keyword)
            elif choice == 4:
                name = input("Enter the name of the contact to update: ")
                manager.update_contact(name)
            elif choice == 5:
                name = input("Enter the name of the contact to delete: ")
                manager.delete_contact(name)
            elif choice == 6:
                print("Exiting Contact Management System. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    main()
