
import csv
import turtle
from pathlib import Path


FONT = ("Arial", 10, "normal")

BASE_DIR = Path(__file__).resolve().parent
MAP_FILE = BASE_DIR / "blank_states_img.gif"
OUTPUT_FILE = BASE_DIR / "states_to_learn.csv"

STATE_DATA = [
    ("Alabama", 100, -71), ("Alaska", -320, -190), ("Arizona", -189, -47),
    ("Arkansas", 36, -36), ("California", -279, 3), ("Colorado", -115, 34),
    ("Connecticut", 263, 78), ("Delaware", 231, 34), ("Florida", 151, -142),
    ("Georgia", 139, -74), ("Hawaii", -230, -190), ("Idaho", -220, 125),
    ("Illinois", 73, 51), ("Indiana", 106, 49), ("Iowa", 23, 85),
    ("Kansas", -33, 25), ("Kentucky", 118, 8), ("Louisiana", 40, -102),
    ("Maine", 303, 142), ("Maryland", 217, 34), ("Massachusetts", 273, 90),
    ("Michigan", 116, 124), ("Minnesota", 14, 157), ("Mississippi", 67, -73),
    ("Missouri", 35, 25), ("Montana", -163, 169), ("Nebraska", -50, 76),
    ("Nevada", -243, 39), ("New Hampshire", 275, 113), ("New Jersey", 240, 52),
    ("New Mexico", -122, -44), ("New York", 231, 100), ("North Carolina", 186, -25),
    ("North Dakota", -55, 178), ("Ohio", 146, 58), ("Oklahoma", -23, -24),
    ("Oregon", -288, 118), ("Pennsylvania", 206, 66), ("Rhode Island", 277, 80),
    ("South Carolina", 168, -52), ("South Dakota", -54, 125), ("Tennessee", 106, -19),
    ("Texas", -44, -93), ("Utah", -186, 39), ("Vermont", 263, 118),
    ("Virginia", 192, 8), ("Washington", -288, 176), ("West Virginia", 172, 27),
    ("Wisconsin", 65, 129), ("Wyoming", -138, 102),
]


def create_state_dictionary():
    return {
        state.casefold(): (state, x, y)
        for state, x, y in STATE_DATA
    }


def save_missing_states(guessed_states, state_dictionary):
    missing_states = [
        state_data[0]
        for key, state_data in state_dictionary.items()
        if key not in guessed_states
    ]

    with open(OUTPUT_FILE, mode="w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["State"])
        for state in missing_states:
            writer.writerow([state])

    print(f"Saved {len(missing_states)} states to learn.")


def main():
    if not MAP_FILE.exists():
        print(
            "Map image not found. "
            "Please place blank_states_img.gif next to this Python file."
        )
        return

    state_dictionary = create_state_dictionary()
    guessed_states = set()

    screen = turtle.Screen()
    screen.title("U.S. States Game")
    screen.setup(width=725, height=491)
    screen.bgpic(str(MAP_FILE))

    writer = turtle.Turtle()
    writer.hideturtle()
    writer.penup()

    while len(guessed_states) < len(state_dictionary):
        answer = screen.textinput(
            title=f"{len(guessed_states)}/{len(state_dictionary)} States Correct",
            prompt="Enter a state name (or type 'exit' to finish):"
        )

        if answer is None or answer.strip().casefold() == "exit":
            save_missing_states(guessed_states, state_dictionary)
            break

        answer = answer.strip().casefold()

        if not answer:
            screen.title("Please enter a state name.")
            continue

        if answer in guessed_states:
            screen.title("You have already guessed that state!")
            continue

        if answer in state_dictionary:
            state_name, x, y = state_dictionary[answer]
            guessed_states.add(answer)

            writer.goto(x, y)
            writer.write(state_name, align="center", font=FONT)

            screen.title(
                f"{len(guessed_states)}/50 States Correct"
            )

        else:
            screen.title("That's not a valid state. Try again!")

    if len(guessed_states) == len(state_dictionary):
        screen.title("Congratulations! You found all 50 states!")
        print("Congratulations! You found all 50 states!")

    screen.exitonclick()


if __name__ == "__main__":
    main()

