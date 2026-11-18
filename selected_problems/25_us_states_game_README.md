# Day 25 — U.S. States Game

## Description

This project is an interactive geography quiz built with Python.

The program displays a map of the United States and challenges the user to identify all 50 states. When a correct answer is entered, the state name appears in its corresponding location on the map.

If the user exits before finding all 50 states, the program saves the remaining states to a CSV file for later study.

## Features

- Interactive map using Python Turtle.
- Checks answers against a dictionary of U.S. states.
- Accepts state names regardless of capitalization.
- Prevents duplicate guesses.
- Tracks the number of correctly identified states.
- Saves missing states to a CSV file.
- Displays a completion message when all 50 states are found.

## Technologies and Concepts

- Python
- Turtle graphics
- CSV file handling
- Dictionaries and dictionary comprehension
- Sets
- Functions
- File paths with `pathlib`
- Input validation
- Exception-free program flow using conditional statements

## Project Files

- `day25_us_states_game.py` — Main game.
- `blank_states_img.gif` — Map image used by the game.
- `states_to_learn.csv` — Generated file containing the states not yet identified.

## How to Run

1. Make sure Python is installed.
2. Make sure `blank_states_img.gif` is in the same directory as the Python file.
3. Open a terminal in the project directory.
4. Run:

```bash
python day25_us_states_game.py
```

5. Enter state names in the input window.
6. Type `exit` to finish and save the remaining states.

## What I Learned

Through this project, I practised using dictionaries and sets, handling user input, working with CSV files and creating interactive graphical applications with Turtle.

I also learned how to organize data and use file paths to manage project resources.
