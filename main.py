'''Contact Management System'''

from contact_manager import ContactManager
from contact import Contact

#Function to add contact
def add_contact(manager):
    """adding contacts to DB
    
    Args: OBJ of ContactManager
    """
    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")
    contact = Contact(name, phone, email, address)
    if contact.validate_phone(phone) and contact.validate_email(email):
        manager.add_contact(contact)
        print("Contact added successfully.")
    else:
        print("Invalid phone number or email address.")

#Function to update contact
def update_contact(manager):
    """Updating contacts to DB
    
    Args: OBJ of ContactManager
    """
    contact_id = int(input("Enter Contact ID to update: "))
    name = input("Enter New Name (leave blank to keep current): ") or None
    phone = input("Enter New Phone (leave blank to keep current): ") or None
    email = input("Enter New Email (leave blank to keep current): ") or None
    address = input("Enter New Address (leave blank to keep current): ") or None
    updates = {}
    if name:
        updates['name'] = name
    if phone:
        updates['phone'] = phone
    if email:
        updates['email'] = email
    if address:
        updates['address'] = address
    if updates:
        manager.update_contact(contact_id, **updates)
        print("Contact updated successfully.")
    else:
        print("No updates provided.")

#Main Function
def main():
    """The main funtion which runs the management system"""

    #Connecting to database and contact manager
    manager = ContactManager('contacts.db')

    #Contact Management Dasboard
    while True:
        print("\n-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
        print("\n\tContact Management System\n")
        print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Search Contacts")
        print("6. Exit")
        choice = input("Enter your choice: ")

        #Contact management functions

        #Add contact
        if choice == '1':
            add_contact(manager)
        #View Contacts
        elif choice == '2':
            contacts = manager.view_contacts()
            for contact in contacts:
                print(Contact(*contact[1:]))
        #Update Contact
        elif choice == '3':
            update_contact(manager)
        #Delete contact
        elif choice == '4':
            contact_id = int(input("Enter Contact ID to delete: "))
            manager.delete_contact(contact_id)
            print("Contact deleted successfully.")
        #Search contacts
        elif choice == '5':
            search_term = input("Enter search term: ")
            results = manager.search_contacts(search_term)
            for result in results:
                print(Contact(*result[1:]))
        #Exit system
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
