
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    if n2 == 0:
        raise ValueError("Cannot divide by zero.")
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


def calculator():
    print("=== PYTHON CALCULATOR ===")

    while True:
        num1 = get_number("What is the first number?: ")

        while True:
            print("\nAvailable operations: +  -  *  /")
            operation_symbol = input("Pick an operation: ")

            if operation_symbol not in operations:
                print("Invalid operation. Please try again.")
                continue

            num2 = get_number("What is the next number?: ")

            try:
                answer = operations[operation_symbol](num1, num2)
            except ValueError as error:
                print(error)
                continue

            print(f"{num1} {operation_symbol} {num2} = {answer}")

            choice = input(
                f"Type 'y' to continue with {answer}, "
                "or 'n' to start a new calculation: "
            ).lower()

            if choice == "y":
                num1 = answer
            else:
                break

        restart = input(
            "\nType 'yes' to use the calculator again "
            "or 'no' to exit: "
        ).lower()

        while restart not in ["yes", "no"]:
            restart = input("Please type 'yes' or 'no': ").lower()

        if restart == "no":
            print("Goodbye!")
            break


if __name__ == "__main__":
    calculator()

