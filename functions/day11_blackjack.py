
import random
from art import logo


def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards):
    """Calculates the score of a hand, adjusting aces when necessary."""
    score = sum(cards)

    if score == 21 and len(cards) == 2:
        return 0

    aces = cards.count(11)

    while score > 21 and aces > 0:
        score -= 10
        aces -= 1

    return score


def compare(user_score, computer_score):
    """Compares the user's score against the computer's score."""
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game():
    """Runs one complete game of Blackjack."""
    print(logo)

    user_cards = [deal_card(), deal_card()]
    computer_cards = [deal_card(), deal_card()]

    game_over = False

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            while True:
                choice = input(
                    "Type 'y' to get another card, or 'n' to pass: "
                ).strip().lower()

                if choice in ("y", "n"):
                    break

                print("Please enter 'y' or 'n'.")

            if choice == "y":
                user_cards.append(deal_card())
            else:
                game_over = True

    user_score = calculate_score(user_cards)

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(
        f"Computer's final hand: {computer_cards}, "
        f"final score: {computer_score}"
    )

    print(compare(user_score, computer_score))


while True:
    play_choice = input(
        "Do you want to play a game of Blackjack? Type 'y' or 'n': "
    ).strip().lower()

    if play_choice == "n":
        print("Goodbye!")
        break

    elif play_choice == "y":
        print("\n" * 20)
        play_game()

    else:
        print("Please enter 'y' or 'n'.")
