'''

@Author: Ayush Prajapati
@Date: 04-09-2024
@Last Modified by: Ayush Prajapati
@Last Modified time: 04-09-2024
@Title: Address Book System Using Python

'''


def main():
    print("**** Welcome to Address Book System ****")
    print("\nEnter the following details\n")

    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    address = input("Enter your address: ")
    state = input("Enter your state: ")

    while True:
        try:
            zip_code = int(input("Enter your ZIP code: "))
            break
        except ValueError:
            print("Invalid input! Please enter a numeric ZIP code.")

    while True:
        try:
            phone_number = int(input("Enter your phone number: "))
            break
        except ValueError:
            print("Invalid input! Please enter a numeric phone number.")
            
    email = input("Enter your email: ")

    print("\nThe contact details are:\n")
    print(f"The First name is {first_name}")
    print(f"The Last name is {last_name}")
    print(f"The Address is {address}")
    print(f"The State is {state}")
    print(f"The Zipcode is {zip_code}")
    print(f"The Phone number is {phone_number}")
    print(f"The email is {email}")


if __name__ == '__main__':
    main()