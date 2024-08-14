# Contact book
class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def update(self, name=None, phone=None, email=None, address=None):
        if name:
            self.name = name
        if phone:
            self.phone = phone
        if email:
            self.email = email
        if address:
            self.address = address

    def __str__(self):
        return f"Name: {self.name}\nPhone: {self.phone}\nEmail: {self.email}\nAddress: {self.address}"

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        new_contact = Contact(name, phone, email, address)
        self.contacts.append(new_contact)
        print("Contact added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
            return
        for idx, contact in enumerate(self.contacts, 1):
            print(f"\nContact {idx}:\n{contact}")

    def search_contact(self, search_term):
        results = [contact for contact in self.contacts if search_term in contact.name or search_term in contact.phone]
        if not results:
            print("No contacts found.")
            return
        for idx, contact in enumerate(results, 1):
            print(f"\nContact {idx}:\n{contact}")

    def update_contact(self, name, **kwargs):
        for contact in self.contacts:
            if contact.name == name:
                contact.update(**kwargs)
                print("Contact updated successfully!")
                return
        print("Contact not found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print("Contact deleted successfully!")
                return
        print("Contact not found.")

def main():
    manager = ContactManager()
# displaying choices
    while True:
        print("Contact Manager\n")
        print("1. Add a Contact")
        print("2. View Contacts")
        print("3. Search a Contact")
        print("4. Update a Contact")
        print("5. Delete a Contact")
        print("6. Exit")
        choice = input("Choose an option(1-6): ")
# Taking contact information input from user
        if choice == '1':
            name = input("Enter the name of the contact: ")
            phone = input("Enter the phone number of the contact: ")
            email = input("Enter email address of the contact: ")
            address = input("Enter address of the contact: ")
            manager.add_contact(name, phone, email, address)

        elif choice == '2':
            manager.view_contacts()

        elif choice == '3':
            search_term = input("Enter the name or phone number to search: ")
            manager.search_contact(search_term)
# Options for modifications in case of user want to update the contact information
        elif choice == '4':
            name = input("Enter the name of the contact to update: ")
            phone = input("Enter new phone number of the contact (leave blank to keep current): ")
            email = input("Enter the new email address of the contact (leave blank to keep current): ")
            address = input("Enter new address of the contact (leave blank to keep current): ")
            manager.update_contact(name, phone=phone, email=email, address=address)

        elif choice == '5':
            name = input("Enter the name of the contact to delete: ")
            manager.delete_contact(name)

        elif choice == '6':
            break

        else:
            print("your in put choice is a invalid choice. Please try again with entering a valid choice.")

if __name__ == "__main__":
    main()
