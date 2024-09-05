'''

@Author: Ayush Prajapati
@Date: 04-09-2024
@Last Modified by: Ayush Prajapati
@Last Modified time: 04-09-2024
@Title: Address Book System Using Python

'''


from logging_helper import create_logger
from input_validator import is_valid, is_valid_email, is_valid_phone_number, is_valid_zip


class Contact:
    def __init__(self, first_name, last_name, address, state, zip_code, phone_number, email):
        """
        Description:
            This function initializes a new object with the user's information. 
        Parameters:
            first_name (str): The user's first name.
            last_name (str): The user's last name.
            address (str): The user's residential address.
            state (str): The user's state of residence.
            zip_code (int): The user's postal zip code.
            phone_number (int): The user's phone number.
            email (str): The user's email address.
        Returns:
            None
        """
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.state = state
        self.zip_code = zip_code
        self.phone_number = phone_number
        self.email = email


    def __str__(self):
        return (f"\nFirst Name: {self.first_name}\n"
                f"Last Name: {self.last_name}\n"
                f"Address: {self.address}\n"
                f"State: {self.state}\n"
                f"ZIP Code: {self.zip_code}\n"
                f"Phone Number: {self.phone_number}\n"
                f"Email: {self.email}")


class AddressBook:
    def __init__(self, logger):
        """
        Description:
            Initializes a new address book with an empty list of contacts.
        Parameters:
            None
        Returns:
            None
        """
        self.contacts = []
        self.logger = logger


    def add_contact(self, contact):
        """
        Description:
            Adds a given contact to the address book.
        Parameters:
            contact (Contact): The contact object to be added.
        Returns:
            None
        """
        self.contacts.append(contact)
        self.logger.info("Contact added successfully!")


    def display_contacts(self):
        """
        Description:
            Displays all the contacts stored in the address book.
        Parameters:
            None
        Returns:
            None
        """
        if not self.contacts:
            self.logger.info("No contacts found.")
        else:
            self.logger.info("\nContacts in Address Book:")
            for contact in self.contacts:
                self.logger.info(contact)
                self.logger.info("\n" + "-" * 40)


def main():
    print("**** Welcome to Address Book System ****")

    logger = create_logger("address-book")
    address_book = AddressBook(logger)
    
    while True:
        print("\nOptions:")
        print("1. Add Contact")
        print("2. Display Contacts")
        print("3. Exit")
        choice = input("Choose an option: ")

        match choice:
            case "1":
                while True:
                    first_name = input("\nEnter the First name: ")
                    if is_valid(first_name):
                        break
                    else:
                        logger.info(f"\nThe first name '{first_name}' is Invalid. Please try again.")

                while True:
                    last_name = input("Enter the Last name: ")
                    if is_valid(last_name):
                        break
                    else:
                        logger.info(f"\nThe Last name '{last_name}' is Invalid. Please try again.")

                while True:
                    address = input("Enter the Address: ")
                    if is_valid(address):
                        break
                    else:
                        logger.info(f"\nThe address '{address}' is Invalid. Please try again.")

                while True:
                    city = input("Enter the City: ")
                    if is_valid(city):
                        break
                    else:
                        logger.info(f"\nThe city '{city}' is Invalid. Please try again.")

                while True:
                    state = input("Enter the State: ")
                    if is_valid(state):
                        break
                    else:
                        logger.info(f"\nThe state '{state}' is Invalid. Please try again.")                          

                while True:
                    zip_code = input("Enter your ZIP code: ")
                    if is_valid_zip(zip_code):
                        break
                    else:
                        logger.info(f"\nThe zip '{zip_code}' is Invalid. Please enter a numeric 6 digit ZIP code.")

                while True:
                    phone_number = input("Enter your Phone Number: ")
                    if is_valid_phone_number(phone_number):
                        break
                    else:
                        logger.info(f"The Phone number '{phone_number}' is Invalid. Please enter a numeric phone number.")

                while True:
                    email = input("Enter your email: ")
                    if is_valid_email(email):
                        break
                    else:
                        logger.info(f"The Email '{email}' is Invalid. Please enter a valid email.")
                
                new_contact = Contact(first_name, last_name, address, state, zip_code, phone_number, email)
                address_book.add_contact(new_contact)

            case "2":
                address_book.display_contacts()

            case "3":
                logger.info("Exiting the Address Book System. \nThank you for using the system!")
                break

            case _:
                logger.info("Invalid option! Please choose again.")


if __name__ == "__main__":
    main()