# ==========================================
# Project: Password Generator
# Developed by: Rahul
# Description:
# This program generates a secure random password
# based on the user's preferred length and complexity.
# ==========================================

import random
import string


def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    """Generate a random password based on user preferences."""

    characters = ""

    if use_upper:
        characters += string.ascii_uppercase

    if use_lower:
        characters += string.ascii_lowercase

    if use_digits:
        characters += string.digits

    if use_symbols:
        characters += "!@#$%^&*()_-+=<>?/"

    if not characters:
        return None

    password = ""

    for _ in range(length):
        password += random.choice(characters)

    return password


def main():
    print("=" * 45)
    print("         PASSWORD GENERATOR")
    print("=" * 45)

    # Get password length
    while True:
        try:
            length = int(input("Enter password length (minimum 4): "))

            if length < 4:
                print("Password should be at least 4 characters long.\n")
            else:
                break

        except ValueError:
            print("Please enter a valid number.\n")

    print("\nSelect password components:")
    upper = input("Include Uppercase Letters? (y/n): ").lower() == "y"
    lower = input("Include Lowercase Letters? (y/n): ").lower() == "y"
    digits = input("Include Numbers? (y/n): ").lower() == "y"
    symbols = input("Include Special Characters? (y/n): ").lower() == "y"

    password = generate_password(length, upper, lower, digits, symbols)

    if password:
        print("\nGenerated Password")
        print("-" * 25)
        print(password)
    else:
        print("\nError: Please select at least one character type.")


if __name__ == "__main__":
    main()