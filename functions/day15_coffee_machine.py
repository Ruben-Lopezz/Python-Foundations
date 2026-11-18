
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    """Checks whether there are enough resources for the drink."""
    for item, amount in order_ingredients.items():
        if amount > resources.get(item, 0):
            print(f"Sorry, there is not enough {item}.")
            return False

    return True


def get_coin_count(coin_name):
    """Gets and validates the number of coins inserted."""
    while True:
        try:
            count = int(input(f"How many {coin_name}?: "))

            if count < 0:
                print("Please enter a non-negative number.")
                continue

            return count

        except ValueError:
            print("Please enter a valid whole number.")


def process_coins():
    """Calculates the total value of the inserted coins."""
    print("Please insert coins.")

    total = get_coin_count("quarters") * 0.25
    total += get_coin_count("dimes") * 0.10
    total += get_coin_count("nickels") * 0.05
    total += get_coin_count("pennies") * 0.01

    return total


def is_transaction_successful(money_received, drink_cost):
    """Checks payment and returns whether the transaction succeeded."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change:.2f} in change.")
        return True

    print("Sorry, that's not enough money. Money refunded.")
    return False


def make_coffee(drink_name, order_ingredients):
    """Deducts the ingredients and prepares the drink."""
    for item, amount in order_ingredients.items():
        resources[item] -= amount

    print(f"Here is your {drink_name}. Enjoy!")


def print_report(profit):
    """Displays the remaining resources and current profit."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit:.2f}")


def coffee_machine():
    """Runs the coffee machine program."""
    profit = 0

    while True:
        choice = input(
            "What would you like? (espresso/latte/cappuccino): "
        ).strip().lower()

        if choice == "off":
            print("Coffee machine shutting down.")
            break

        elif choice == "report":
            print_report(profit)

        elif choice not in MENU:
            print("Invalid selection. Please choose a drink.")

        else:
            drink = MENU[choice]

            if is_resource_sufficient(drink["ingredients"]):
                payment = process_coins()

                if is_transaction_successful(payment, drink["cost"]):
                    profit += drink["cost"]
                    make_coffee(choice, drink["ingredients"])


coffee_machine()
