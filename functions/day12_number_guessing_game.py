
from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(user_guess, actual_answer, turns):
    """Checks the guess and returns the remaining attempts."""
    if user_guess > actual_answer:
        print("Too high.")
        return turns - 1

    elif user_guess < actual_answer:
        print("Too low.")
        return turns - 1

    else:
        print(f"You got it! The answer was {actual_answer}.")
        return turns


def set_difficulty():
    """Sets the number of attempts based on the chosen difficulty."""
    while True:
        level = input(
            "Choose a difficulty. Type 'easy' or 'hard': "
        ).strip().lower()

        if level == "easy":
            return EASY_LEVEL_TURNS
        elif level == "hard":
            return HARD_LEVEL_TURNS
        else:
            print("Invalid choice. Please type 'easy' or 'hard'.")


def game():
    """Runs one complete number guessing game."""
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    answer = randint(1, 100)
    turns = set_difficulty()

    while turns > 0:
        print(f"You have {turns} attempts remaining.")

        try:
            guess = int(input("Make a guess: "))
        except ValueError:
            print("Please enter a valid whole number.")
            continue

        if not 1 <= guess <= 100:
            print("Please guess a number between 1 and 100.")
            continue

        turns = check_answer(guess, answer, turns)

        if guess == answer:
            return

        if turns > 0:
            print("Guess again.")

    print(f"You've run out of guesses. The answer was {answer}.")
    print("You lose.")


game()
