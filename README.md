Contact Management System Documentation

Overview
The Contact Management System is designed to manage contacts using a SQLite database. It allows users to perform operations such as adding, viewing, updating, deleting, and searching contacts. The system consists of three main components: `Contact`, `ContactManager`, and `main` module (`main.py`).

`Contact` Class

The `Contact` class represents a contact with attributes such as name, phone number, email address, and physical address. It includes methods for validation using regular expressions (`validate_phone` and `validate_email`).

- Attributes:
  - `name` (str): Name of the contact.
  - `phone` (str): Phone number of the contact.
  - `email` (str): Email address of the contact.
  - `address` (str): Physical address of the contact.

- Methods:
  - `__str__(self)`: Returns a string representation of the contact.
  - `validate_phone(phone)`: Validates the phone number format using regex.
  - `validate_email(email)`: Validates the email address format using regex.

`ContactManager` Class

The `ContactManager` class handles database operations for managing contacts.

- Attributes:
  - `conn`: SQLite database connection.
  - `cursor`: Cursor object to execute SQL commands.

- Methods:
  - `__init__(self, db_name)`: Initializes the database connection and creates a `contacts` table if it doesn't exist.
  - `create_table(self)`: Creates the `contacts` table with fields `id`, `name`, `phone`, `email`, and `address`.
  - `add_contact(self, contact)`: Adds a new contact to the database.
  - `view_contacts(self)`: Retrieves and returns all contacts from the database.
  - `update_contact(self, contact_id, **kwargs)`: Updates an existing contact in the database.
  - `delete_contact(self, contact_id)`: Deletes a contact from the database.
  - `search_contacts(self, search_term)`: Searches contacts in the database based on name, phone, email, or address.

`main` Module (`main.py`)

The `main` module provides an interactive command-line interface for users to interact with the Contact Management System.

- Functions:
  - `add_contact(manager)`: Prompts the user to input contact details and adds a new contact to the database after validation.
  - `update_contact(manager)`: Prompts the user to input contact ID and new details to update an existing contact.
  - `main()`: The main function that initializes `ContactManager`, displays a menu of options, and calls appropriate functions based on user input.

Usage Instructions

1. Run the Program: Execute `main.py` to start the Contact Management System.
2. Choose an Option: Select an option from the menu by entering the corresponding number.
3. Follow Prompts: Enter details as prompted to add, view, update, delete, or search contacts.
4. Exit: Choose the "Exit" option to close the application.

This documentation provides an overview of the design and usage of the Contact Management System, enabling users to effectively manage their contacts using the provided command-line interface.

