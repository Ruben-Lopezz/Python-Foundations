
from art import logo, vs
from game_data import data
import random


def format_data(account):
    """Formats account data into a readable description."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]

    return f"{account_name}, a {account_descr}, from {account_country}"


def check_answer(user_guess, a_followers, b_followers):
    """Checks whether the user's guess is correct."""
    if a_followers > b_followers:
        return user_guess == "a"
    elif b_followers > a_followers:
        return user_guess == "b"
    else:
        return None


def get_guess():
    """Gets and validates the user's choice."""
    while True:
        guess = input(
            "Who has more followers? Type 'A' or 'B': "
        ).strip().lower()

        if guess in ("a", "b"):
            return guess

        print("Invalid choice. Please type 'A' or 'B'.")


def play_game():
    """Runs the Higher or Lower game."""
    score = 0
    account_b = random.choice(data)
    game_should_continue = True

    while game_should_continue:
        account_a = account_b

        available_accounts = [
            account for account in data if account != account_a
        ]

        if not available_accounts:
            print("Not enough accounts to continue the game.")
            return

        account_b = random.choice(available_accounts)

        print(logo)
        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Against B: {format_data(account_b)}.")

        guess = get_guess()

        a_followers = account_a["follower_count"]
        b_followers = account_b["follower_count"]

        is_correct = check_answer(
            guess, a_followers, b_followers
        )

        print("\n" * 20)

        if is_correct is None:
            print("It's a tie! No point awarded.")
        elif is_correct:
            score += 1
            print(f"You're right! Current score: {score}")
        else:
            print(f"Sorry, that's wrong. Final score: {score}.")
            game_should_continue = False


play_game()
