
print(r'''
*******************************************************************************
|                                                                              |
|________________.=""_;=.______________|_____________________|_______        |
|             ,-"_,="" `"=.|                                                  |
|___________________|__"=._o`"-._ `"=.______________|___________________     |
|        `"=._o`"=._ _`"=._                                                   |
|_____________________:=._o "=._."_.-="'"=.__________________|_______        |
|   __.--" , ; `"=._o." ,-"""-._ ".                                           |
|___________________|._" ,. .` ` `` , `"-._"-._ ". '__|___________________   |
|o`"=._` , "` `; .". , "-._"-._; ;                                            |
|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______        |
|o ; `"-.o`"=._`` '` " ,__.--o;                                               |
|___________________|_| ; (#) `-.o `"=.`_.--"_o.-; ;___|___________________  |
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input(
    'You\'re at a crossroad, where do you want to go? '
    'Type "left" or "right".\n'
).strip().lower()

if choice1 == "left":
    choice2 = input(
        'You\'ve come to a lake. There is an island in the middle. '
        'Type "wait" to wait for a boat or "swim" to swim across.\n'
    ).strip().lower()

    if choice2 == "wait":
        choice3 = input(
            "You arrive at the island unharmed. "
            "There is a house with 3 doors: red, yellow and blue. "
            "Which colour do you choose?\n"
        ).strip().lower()

        if choice3 == "yellow":
            print("You found the treasure. You Win!")
        elif choice3 == "red":
            print("It's a room full of fire. Game Over.")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("Invalid choice. Game Over.")

    elif choice2 == "swim":
        print("You got attacked by an angry trout. Game Over.")
    else:
        print("Invalid choice. Game Over.")

elif choice1 == "right":
    print("You fell into a hole. Game Over.")

else:
    print("Invalid choice. Game Over.")
