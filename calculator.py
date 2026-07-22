# ==========================================================
# Project Name : Simple Calculator
# Developed By : Rahul godika
# Language     : Python
# Description  :  A simple calculator that performs basic arithmetic
# operations such as Addition, Subtraction,
# Multiplication, and Division.
# ==========================================================

def display_menu():
    """Displays the calculator menu."""
    print("\n========== SIMPLE CALCULATOR ==========")
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")
    print("=======================================")


def get_numbers():
    """Takes two numbers as input from the user."""
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            return num1, num2
        except ValueError:
            print("❌ Invalid input! Please enter numeric values.\n")


def calculate(choice, num1, num2):
    """Performs the selected arithmetic operation."""

    if choice == "1":
        return num1 + num2

    elif choice == "2":
        return num1 - num2

    elif choice == "3":
        return num1 * num2

    elif choice == "4":
        if num2 == 0:
            return "Error! Division by zero is not allowed."
        return num1 / num2

    else:
        return None


def main():
    """Main function of the calculator."""

    print("Welcome to the Python Calculator!")

    while True:
        display_menu()

        choice = input("Enter your choice (1-5): ")

        if choice == "5":
            print("\nThank you for using the calculator!")
            print("Program terminated successfully.")
            break

        elif choice in ["1", "2", "3", "4"]:

            number1, number2 = get_numbers()

            result = calculate(choice, number1, number2)

            print("\n----------- RESULT -----------")

            if choice == "1":
                print(f"{number1} + {number2} = {result}")

            elif choice == "2":
                print(f"{number1} - {number2} = {result}")

            elif choice == "3":
                print(f"{number1} * {number2} = {result}")

            elif choice == "4":
                print(f"{number1} / {number2} = {result}")

            print("------------------------------")

        else:
            print("❌ Invalid choice! Please select between 1 and 5.")


# Program Execution
if __name__ == "__main__":
    main()