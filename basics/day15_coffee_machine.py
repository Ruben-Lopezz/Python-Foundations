
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

profit = 0


def print_report():
    print("\n----- RESOURCE REPORT -----")
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit:.2f}")
    print("---------------------------\n")


def is_resource_sufficient(order_ingredients):
    for item, amount in order_ingredients.items():
        if amount > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def get_coin_count(coin_name):
    while True:
        try:
            count = int(input(f"How many {coin_name}?: "))
            if count < 0:
                print("Please enter zero or a positive number.")
                continue
            return count
        except ValueError:
            print("Please enter a valid whole number.")


def process_coins():
    print("Please insert coins.")

    total = get_coin_count("quarters") * 0.25
    total += get_coin_count("dimes") * 0.10
    total += get_coin_count("nickels") * 0.05
    total += get_coin_count("pennies") * 0.01

    return round(total, 2)


def is_transaction_successful(money_received, drink_cost):
    if money_received < drink_cost:
        print("Sorry, that's not enough money. Money refunded.")
        return False

    change = round(money_received - drink_cost, 2)
    print(f"Here is ${change:.2f} in change.")
    return True


def make_coffee(drink_name, order_ingredients):
    for item, amount in order_ingredients.items():
        resources[item] -= amount

    print(f"Here is your {drink_name}. Enjoy! ☕")


def coffee_machine():
    global profit

    is_on = True

    while is_on:
        choice = input(
            "What would you like? (espresso/latte/cappuccino): "
        ).lower().strip()

        if choice == "off":
            print("Coffee machine shutting down.")
            is_on = False

        elif choice == "report":
            print_report()

        elif choice not in MENU:
            print("Invalid choice. Please select a drink from the menu.")

        else:
            drink = MENU[choice]

            if is_resource_sufficient(drink["ingredients"]):
                payment = process_coins()

                if is_transaction_successful(payment, drink["cost"]):
                    profit += drink["cost"]
                    make_coffee(choice, drink["ingredients"])


if __name__ == "__main__":
    coffee_machine()

