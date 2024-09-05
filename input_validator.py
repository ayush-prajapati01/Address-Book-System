'''

@Author: Ayush Prajapati
@Date: 05-09-2024
@Last Modified by: Ayush Prajapati
@Last Modified time: 05-09-2024
@Title: Python Program to validate user input using regex

'''


import re


def is_valid(data):
    """
    Description: 
        This function validates data of the user
    Parameters:
        data : data of the user
    Return:
        bool: Whether valid or not
    """
    ## Pattern: Last name starts with Cap and has minimum 3 characters
    data_pattern = r"\D{3,}$"
    return bool(re.match(data_pattern, data))


def is_valid_email(email):
    """
    Description: 
        This function validates email of the user
    Parameters:
        email: email of the user
    Return:
        bool: Whether valid or not
    """
    email_pattern = r"^(?!.*\.\.)(?!^\.)([a-zA-Z0-9._%+-])+(?<!\.)@([a-zA-Z0-9-]+\.[a-zA-Z]{2,})(\.[a-zA-Z]{2,})?$"
    return bool(re.match(email_pattern, email))


def is_valid_phone_number(phone_number):
    """
    Description: 
        This function validates phone number of the user
    Parameters:
        phone_number: phone number of the user
    Return:
        bool: Whether valid or not
    """
    phone_number_pattern = r"^(\d{2,3}\s?)?\d{10}$"
    return bool(re.match(phone_number_pattern, phone_number))


def is_valid_zip(zip_code):
    """
    Description: 
        This function validates zip code of the user
    Parameters:
        zip_code: zip code of the user
    Return:
        bool: Whether valid or not
    """
    zip_code_pattern = r"\d{6}"
    return bool(re.match(zip_code_pattern, zip_code))


def main():
    print("This file contains input validation for name, email and phone number")


if __name__ == "__main__":
    main()