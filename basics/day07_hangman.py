
import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

display = ["_" for _ in chosen_word]

print("Welcome to Hangman!")

guess = input("Guess a letter: ").lower().strip()

if len(guess) != 1 or not guess.isalpha():
    print("Please enter a single letter.")

else:
    for index, letter in enumerate(chosen_word):
        if letter == guess:
            display[index] = letter

    if guess in chosen_word:
        print("Right!")
    else:
        print("Wrong!")

    print(" ".join(display))
