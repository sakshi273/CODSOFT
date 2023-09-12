import random
import string


def generate_password(length):
    # character sets for password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generating random password using given lenth
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password


if __name__ == "__main__":
    try:
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            print("Password length must be a positive integer.")
        else:
            password = generate_password(length)
            print(f"Generated Password: {password}")
    except ValueError:
        print("Invalid input. Please enter a valid positive integer for the password length.")
