'''

@Author: Ayush Prajapati
@Date: 04-09-2024
@Last Modified by: Ayush Prajapati
@Last Modified time: 06-09-2024
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
    def __init__(self, logger, name):
        """
        Description:
            Initializes a new address book with an empty list of contacts.
        Parameters:
            None
        Returns:
            None
        """
        self.name = name
        self.contacts = []
        self.logger = logger
        self.city_person_dict = {}
        self.state_person_count = {} 


    def add_contact(self, contact):
        """
        Description:
            Adds a given contact to the address book.
        Parameters:
            contact (Contact): The contact object to be added.
        Returns:
            None
        """
        for existing_contact in self.contacts:
            if existing_contact.first_name == contact.first_name and \
                existing_contact.last_name == contact.last_name:
                self.logger.info(f"Contact with the name {contact.first_name} {contact.last_name} already exists!")
                return

        self.contacts.append(contact)
        self.logger.info("Contact added successfully!")

        # Updating the city-person dictionary
        if contact.city not in self.city_person_dict:
            self.city_person_dict[contact.city] = []
        self.city_person_dict[contact.city].append(contact)

         # Updating the state-person count dictionary
        if contact.state not in self.state_person_count:
            self.state_person_count[contact.state] = 0
        self.state_person_count[contact.state] += 1


    def sort_contacts_by_first_name(self):
        """
        Description:
            Sorts the contacts alphabetically by the person's first name.
        Parameters:
            None
        Returns:
            None
        """
        if not self.contacts:
            self.logger.info("No contacts to sort.")
        else:
            # Sort contacts by the first name
            self.contacts.sort(key=lambda contact: contact.first_name)
            self.logger.info("Contacts sorted alphabetically by first name.")


    def sort_contacts(self, criteria):
        """
        Description:
            Sorts contacts by the given criteria: 'city', 'state', or 'zip'.
        Parameters:
            criteria (str): The field by which to sort the contacts (city, state, or zip).
        Returns:
            None
        """
        if not self.contacts:
            self.logger.info("No contacts to sort.")
            return
        
        if criteria == 'city':
            self.contacts.sort(key=lambda contact: contact.city)
        elif criteria == 'state':
            self.contacts.sort(key=lambda contact: contact.state)
        elif criteria == 'zip':
            self.contacts.sort(key=lambda contact: contact.zip_code)
        else:
            self.logger.info("Invalid sorting criteria! Please choose 'city', 'state', or 'zip'.")
            return
        
        self.logger.info(f"Contacts sorted by {criteria}.")


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


    def search_via_name(self, name):
        """
        Description:
            Searhes and display contact of a person
        Parameters:
            name(str): The name to be searched
        Returns:
            str: contact of a person
        """
        first_name, last_name = name.split()
        for contact in self.contacts:
            if contact.first_name == first_name and contact.last_name == last_name:
                self.logger.info(contact)
                return
            

    def search_via_state(self, state):
        """
        Description:
            Searches all the person belonging to a state
        Parameters:
            state(str): The state to be searched
        Returns:
            None
        """
        person_in_state = []
        for contact in self.contacts:
            if contact.state == state :
                person_in_state.append(contact.first_name + " " + contact.last_name)
        
        return person_in_state


    def display_persons_by_city(self):
        """
        Description:
            Displays all the persons grouped by city.
        Parameters:
            None
        Returns:
            None
        """
        if not self.city_person_dict:
            self.logger.info("No contacts found.")
        else:
            for city, persons in self.city_person_dict.items():
                self.logger.info(f"\nCity: {city}")
                for person in persons:
                    self.logger.info(f"  - {person.first_name} {person.last_name}")
            self.logger.info("\n" + "-" * 40)


    def display_contact_count_by_state(self):
        """
        Description:
            Displays the number of contacts grouped by state.
        Parameters:
            None
        Returns:
            None
        """
        if not self.state_person_count:
            self.logger.info("No contacts found.")
        else:
            self.logger.info("\nContact Count by State:")
            for state, count in self.state_person_count.items():
                self.logger.info(f"State: {state}, Count: {count}")
            self.logger.info("\n" + "-" * 40)


class ManageAddressBook:
    def __init__(self, logger):
        """
        Description:
            Initializes the to manage multiple address books.
        Parameters:
            None
        Return:
            None
        """
        self.address_books = {}
        self.logger = logger


    def create_address_book(self, name):
        """
        Description:
            Creates a new address book with a unique name.
        Parameters:
            None
        Return:
            None
        """
        if name in self.address_books:
            self.logger.info(f"Address book '{name}' already exists.")
        else:
            self.address_books[name] = AddressBook(self.logger, name)
            self.logger.info(f"Address book '{name}' created successfully.")


    def delete_address_book(self, name):
        """
        Description:
            Deletes an address book by its unique name.
        Parameters:
            name: name of the address book
        Return:
            None
        """
        if name in self.address_books:
            del self.address_books[name]
            self.logger.info(f"Address book '{name}' deleted successfully.")
        else:
            self.logger.info(f"Address book '{name}' not found.")


    def select_address_book(self, name):
        """
        Description:
        Selects an address book by its unique name.
        Parameters:
            name: name of the address book
        Return:
            None
        """
        if name in self.address_books:
            return self.address_books[name]
        else:
            self.logger.info(f"Address book '{name}' not found.")
            return None
        

    def list_address_books(self):
        """
        Description:
            Lists all available address books.
        Parameters:
            name: name of the address book
        Return:
            None
        """
        if not self.address_books:
            self.logger.info("No address books available.")
        else:
            self.logger.info("Available Address Books:")
            for name in self.address_books:
                self.logger.info(f"- {name}")


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
    address_book_manager = ManageAddressBook(logger)

    # Main AddressBook menu
    while True:
        print("\nOptions:")
        print("1. Add Address Book")
        print("2. Display All Address Books")
        print("3. Delete Address Book")
        print("4. Go to Contacts Menu")
        print("5. Exit")
        
        choice = input("Choose an option: ")

        match choice:
            case "1":
                address_book_name = get_valid_input(logger,"\nEnter name of the address book: ", is_valid)
                address_book_manager.create_address_book(address_book_name)
            
            case "2":
                address_book_manager.list_address_books()
            
            case "3":
                address_book_name = input("Enter name of the address book to delete: ")
                address_book_manager.delete_address_book(address_book_name)
            
            case "4":
                print(f"Available Address Books:")
                address_book_manager.list_address_books()
                address_book_name = input("Enter name of the address book to manage contacts: ")
                address_book = address_book_manager.select_address_book(address_book_name)
                if address_book:
                    print(f"Managing contacts for Address Book: {address_book_name}")
                    
                    # Contacts menu
                    while True:
                        print("\nOptions:")
                        print("1. Add Contact")
                        print("2. Display Contacts")
                        print("3. Update Contact by name")
                        print("4. Delete Contact by name")
                        print("5. Add Multiple Contacts")
                        print("6. Search via Name")
                        print("7. Search via State")
                        print("8. View by City")
                        print("9. Count by State")
                        print("10. Sort by first name")
                        print("11. Sort by Criteria")
                        print("12. Go Back to Main Menu")
                        contact_choice = input("Choose an option: ")

                        match contact_choice:
                            case "1":
                                new_contact = create_contact(logger)
                                address_book.add_contact(new_contact)

                            case "2":
                                address_book.display_contacts()

                            case "3":
                                name = input("Enter the first and last name separated by space (ex: joe lee): ")
                                address_book.update_contacts(name)

                            case "4":
                                name = input("Enter the first and last name separated by space (ex: joe lee): ")
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
                                    except ValueError:
                                        logger.info("Please enter a valid number.")

                            case "6":
                                name = input("Enter the first and last name separated by space (ex: joe lee): ")
                                address_book.search_via_name(name)

                            case "7":
                                state_name = get_valid_input(logger,"\nEnter name of state to search: ", is_valid)
                                person_in_state = []
                                person_in_state = address_book.search_via_state(state_name)
                                logger.info(f"Person in State {state_name} is/are:")
                                for person in person_in_state:
                                    logger.info(person)

                            case "8":
                                address_book.display_persons_by_city()

                            case "9":
                                address_book.display_contact_count_by_state()

                            case "10":
                                address_book.sort_contacts_by_first_name()
                                address_book.display_contacts()
                            
                            case "11":
                                criteria = input("Sort contacts by city, state, or zip: ").lower()
                                address_book.sort_contacts(criteria)
                                address_book.display_contacts()
   
                            case "12":
                                logger.info("Switching to the Main menu.")
                                break

                            case _:
                                logger.info("Invalid option! Please choose again.")
                else:
                    print(f"Address Book '{address_book_name}' not found.")
            
            case "5":
                print("Exiting the Address Book System.\nThank You for using our system")
                break

            case _:
                print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    main()