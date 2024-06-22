'''Contact manager and functions'''

import sqlite3

class ContactManager:
    """Class ContactManager for contact management and DB connection and manupulation"""
    #Initializing the Database
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    #Creating Table
    def create_table(self):
        """Create table function"""

        query = '''CREATE TABLE IF NOT EXISTS contacts (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    phone TEXT NOT NULL,
                    email TEXT NOT NULL,
                    address TEXT)'''
        self.cursor.execute(query)

    #Function to add contacts to DB
    def add_contact(self, contact):
        """Add contacts to DB Function
        
        Args:
            contact: class contact obj
        """

        query = '''INSERT INTO contacts (name, phone, email, address)
                   VALUES (?,?,?,?)'''
        self.cursor.execute(query, (contact.name, contact.phone, contact.email, contact.address))
        self.conn.commit()

    #Function to view contacts from DB
    def view_contacts(self):
        """View contacts from DB Function"""

        query = "SELECT * FROM contacts"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    #Function to update contacts to DB
    def update_contact(self, contact_id, **kwargs):
        """Update contacts to DB Functions
        
        Args:
            contact_id: contact SL No.
            kwargs: dictionary of updated contact details
        """

        fields = ', '.join(f'{k}=?' for k in kwargs.keys())
        values = tuple(kwargs.values())
        query = f"UPDATE contacts SET {fields} WHERE id=?"
        self.cursor.execute(query, (*values, contact_id))
        self.conn.commit()

    #Function to delete contacts from DB
    def delete_contact(self, contact_id):
        """ Delete contact from DB Function
        
        Args:
            contact_id: contact SL No.
        """

        query = "DELETE FROM contacts WHERE id=?"
        self.cursor.execute(query, (contact_id,))
        self.conn.commit()

    #Function to search contacts from DB
    def search_contacts(self, search_term):
        """Search contact from DB Function
        
        Args:
            search_term: search key to find contacts from DB
        """
        query = "SELECT * FROM contacts WHERE name LIKE? OR phone LIKE? OR email LIKE? OR address LIKE?"
        self.cursor.execute(query, ('%' + search_term + '%', '%' + search_term + '%', '%' + search_term + '%', '%' + search_term + '%'))
        return self.cursor.fetchall()
