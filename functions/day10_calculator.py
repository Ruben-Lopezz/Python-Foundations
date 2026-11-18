
import art


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


def calculator():
    print(art.logo)

    while True:
        try:
            num1 = float(input("What is the first number?: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        while True:
            print("\nAvailable operations:")
            for symbol in operations:
                print(symbol)

            operation_symbol = input("Pick an operation: ").strip()

            if operation_symbol not in operations:
                print("Invalid operation. Please try again.")
                continue

            try:
                num2 = float(input("What is the next number?: "))

                answer = operations[operation_symbol](num1, num2)

            except ValueError as error:
                print(error)
                continue

            print(f"{num1} {operation_symbol} {num2} = {answer}")

            while True:
                choice = input(
                    f"Type 'y' to continue calculating with {answer}, "
                    "or type 'n' to start a new calculation: "
                ).strip().lower()

                if choice in ("y", "n"):
                    break

                print("Please enter 'y' or 'n'.")

            if choice == "y":
                num1 = answer
            else:
                print("\n" * 3)
                break


calculator()
