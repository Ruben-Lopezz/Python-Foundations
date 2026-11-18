
from art import logo

print(logo)


def find_highest_bidder(bidding_record):
    winner = ""
    highest_bid = -1

    for bidder, bid_amount in bidding_record.items():
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    return winner, highest_bid


bids = {}
continue_bidding = True

while continue_bidding:
    name = input("What is your name?: ").strip()

    if not name:
        print("Please enter a valid name.")
        continue

    try:
        price = int(input("What is your bid?: $"))

        if price < 0:
            print("The bid cannot be negative.")
            continue

    except ValueError:
        print("Please enter a valid whole number.")
        continue

    bids[name] = price

    while True:
        should_continue = input(
            "Are there any other bidders? Type 'yes' or 'no'.\n"
        ).strip().lower()

        if should_continue in ("yes", "no"):
            break

        print("Please answer 'yes' or 'no'.")

    if should_continue == "no":
        continue_bidding = False
    else:
        print("\n" * 20)


winner, highest_bid = find_highest_bidder(bids)

print(f"The winner is {winner} with a bid of ${highest_bid}.")
