'''Contact schema and validation'''

import re

class Contact:
    '''Class Contact to create contacts and validation'''

    #Intitalizing contact details
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    #Returning contacts as string
    def __str__(self):
        return f"{self.name}, {self.phone}, {self.email}, {self.address}"

    #Phone number validation using regex
    @staticmethod
    def validate_phone(phone):
        '''Phone number validation using regex
        
        Args:
            phone: The phone number
        '''

        pattern = r'^(\+\d{10,15})$|^(\(\d{3}\)\s\d{3}-\d{4})$'
        return bool(re.match(pattern, phone))

    #Email validation using regex
    @staticmethod
    def validate_email(email):
        '''Email validation using regex
        
        Args:
            phone: The email address
        '''

        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return bool(re.match(pattern, email))
