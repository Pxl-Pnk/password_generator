import string
import secrets

def generate_password(length, use_uppercase=True, use_lowercase=True, use_numbers=True, use_special_chars=True, exclude_chars=""):
    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_numbers:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    characters = ''.join(filter(lambda c: c not in exclude_chars, characters))

    if not characters:
        raise ValueError("No characters selected for password generation.")

    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def get_yes_no_input(prompt):
    while True:
        user_input = input(prompt).strip().lower()
        if user_input == "y":
            return True
        elif user_input == "n":
            return False
        else:
            print("Please enter 'y' for yes or 'n' for no.")

def get_string_input(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input:
            return user_input
        else:
            print("Please enter a valid string.")

if __name__ == "__main__":
    try:
        num_passwords = int(input("Enter the number of passwords to generate: "))
        min_password_length = int(input("Enter the minimum password length: "))
        max_password_length = int(input("Enter the maximum password length: "))
        exclude_chars = get_string_input("Enter any characters to exclude (e.g., l1I0O): ")

        include_uppercase = get_yes_no_input("Include uppercase letters? (y/n): ")
        include_lowercase = get_yes_no_input("Include lowercase letters? (y/n): ")
        include_numbers = get_yes_no_input("Include numbers? (y/n): ")
        include_special_chars = get_yes_no_input("Include special characters? (y/n): ")

        for _ in range(num_passwords):
            password_length = max_password_length
            generated_password = generate_password(password_length, include_uppercase, include_lowercase, include_numbers, include_special_chars, exclude_chars)
            print("Generated Password: " + generated_password)
    except ValueError:
        print("Please enter valid input.")
