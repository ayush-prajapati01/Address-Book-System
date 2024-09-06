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
    def __init__(self, first_name, last_name, address, city, state, zip_code, phone_number, email):
        """
        Description:
            This function initializes a new object with the user's information. 
        Parameters:
            first_name (str): The user's first name.
            last_name (str): The user's last name.
            address (str): The user's residential address.
            city (str): The user's city of residence.
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
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone_number = phone_number
        self.email = email


    def __str__(self):
        return (f"\nFirst Name: {self.first_name}\n"
                f"Last Name: {self.last_name}\n"
                f"Address: {self.address}\n"
                f"City: {self.city}\n"
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
    

    def update_contacts(self, name):
        """
        Description:
            Update contacts by their name
        Parameters:
            name: Name of the person whose contact to be updated
        Returns:
            None
        """
        first_name, last_name = name.split()
        for contact in self.contacts:
            if contact.first_name == first_name and contact.last_name == last_name:
                self.logger.info("Updating Contact...")
                while True:
                    print("\nWhich field would you like to update?")
                    print("1. First Name")
                    print("2. Last Name")
                    print("3. Address")
                    print("4. City")
                    print("5. State")
                    print("6. ZIP Code")
                    print("7. Phone Number")
                    print("8. Email")
                    print("9. Back to Main Menu")

                    choice = input("Enter your choice (1-8): ")

                    if choice == "1":
                        print(f"Old First Name: {contact.first_name}")
                        contact.first_name = get_valid_input(self.logger, "Enter new first name: ", is_valid)
                    elif choice == "2":
                        print(f"Old Last Name: {contact.last_name}")
                        contact.last_name = get_valid_input(self.logger, "Enter new last name: ", is_valid)
                    elif choice == "3":
                        print(f"Old Address: {contact.address}")
                        contact.address = get_valid_input(self.logger, "Enter new address: ", is_valid)
                    elif choice == "4":
                        print(f"Old City: {contact.city}")
                        contact.city= get_valid_input(self.logger, "Enter new city: ", is_valid)
                    elif choice == "5":
                        print(f"Old state: {contact.state}")
                        contact.state = get_valid_input(self.logger, "Enter new state: ", is_valid)
                    elif choice == "6":
                        print(f"Old Zip code: {contact.zip_code}")
                        contact.zip_code = get_valid_input(self.logger, "Enter new ZIP code: ", is_valid_zip)
                    elif choice == "7":
                        print(f"Old Phone number: {contact.phone_number}")
                        contact.phone_number = get_valid_input(self.logger, "Enter new phone number: ", is_valid_phone_number)
                    elif choice == "8":
                        print(f"Old Email: {contact.email}")
                        contact.email = get_valid_input(self.logger, "Enter new email: ", is_valid_email)
                    elif choice == "9":
                        self.logger.info("Update process completed.")
                        return
                    else:
                        self.logger.info("Invalid choice, please try again.")

            else:
                self.logger.info("No contacts found.")


    def delete_contacts(self, name):
        """
        Description:
            Delete contact by their name
        Parameters:
            name: Name of the person whose contact to be deleted
        Returns:
            None
        """
        first_name, last_name = name.split()
        for contact in self.contacts:
            if contact.first_name == first_name and contact.last_name == last_name:
                self.logger.info("Deleting Contact...")
                self.contacts.remove(contact)
                self.logger.info("\nSuccessfully Deleted Contact...")
                break
            else:
                self.logger.info("Contact NOT found.")


def get_valid_input(logger, prompt, validation_func):
    """
    Description:
        Gets the valid user input
    Parameters:
        logger: logger object
        prompt: prompt for the user
        validation_func: validation func to be used
    Returns:
        user_input: validated user input
    """
    while True:
        user_input = input(prompt)
        if validation_func(user_input):
            return user_input
        else:
            logger.info(f"The input '{user_input}' is invalid. Please try again.")


def create_contact(logger):
    """
    Description:
        Takes the user input and creates a contact
    Parameters:
        logger: logger object
    Returns:
        object: contact object
    """
    first_name = get_valid_input(logger,"\nEnter the First name: ", is_valid)
    last_name = get_valid_input(logger,"Enter the Last name: ", is_valid)
    address = get_valid_input(logger,"Enter the Address: ", is_valid)
    city = get_valid_input(logger,"Enter the City: ", is_valid)
    state = get_valid_input(logger,"Enter the State: ", is_valid)
    zip_code = get_valid_input(logger,"Enter your ZIP code: ", is_valid_zip)
    phone_number = get_valid_input(logger,"Enter your Phone Number: ", is_valid_phone_number)
    email = get_valid_input(logger,"Enter your email: ", is_valid_email)

    new_contact = Contact(first_name, last_name, address, city, state, zip_code, phone_number, email)

    return new_contact


def main():
    print("**** Welcome to Address Book System ****")

    logger = create_logger("address-book")
    address_book = AddressBook(logger)
    
    while True:
        print("\nOptions:")
        print("1. Add Contact")
        print("2. Display Contacts")
        print("3. Update Contact by name")
        print("4. Delete Contact by name")
        print("5. Add Multiple Contacts")
        print("6. Exit")
        choice = input("Choose an option: ")

        match choice:
            case "1":
                new_contact = create_contact(logger)
                address_book.add_contact(new_contact)

            case "2":
                address_book.display_contacts()
            
            case "3":
                name = input("Enter the first and last name seperated by space(ex:joe lee): ")
                address_book.update_contacts(name)
            
            case "4":
                name = input("Enter the first and last name seperated by space(ex:joe lee): ")
                address_book.delete_contacts(name)
            
            case "5":
                while True:
                    try:
                        no_of_contacts = int(input("Enter number of contacts to be added: "))
                        for count in range(no_of_contacts):
                            logger.info(f"\nPlease enter contact {count+1}")
                            new_contact = create_contact(logger)
                            address_book.add_contact(new_contact)
                        break
                    except:
                        logger.info("Please enter a Valid number")

            case "6":
                logger.info("Exiting the Address Book System. \nThank you for using the system!")
                break

            case _:
                logger.info("Invalid option! Please choose again.")


if __name__ == "__main__":
    main()