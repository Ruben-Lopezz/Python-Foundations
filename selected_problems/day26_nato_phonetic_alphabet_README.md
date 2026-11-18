# Day 26 — NATO Phonetic Alphabet

## Description

This project converts a word or phrase into its NATO phonetic alphabet equivalent.

The program reads the NATO alphabet from a CSV file and uses a Python dictionary to translate each letter into its corresponding code word.

For example:

- `HELLO` → Hotel - Echo - Lima - Lima - Oscar
- `PYTHON` → Papa - Yankee - Tango - Hotel - Oscar - November

## Features

- Reads data from a CSV file.
- Builds a dictionary using dictionary comprehension.
- Converts words and phrases into phonetic code words.
- Ignores spaces between words.
- Validates user input.
- Handles empty input and invalid characters.
- Allows the user to convert multiple words until they choose to exit.

## Technologies and Concepts

- Python
- CSV file handling
- `csv.DictReader`
- Dictionaries
- Dictionary comprehension
- Functions
- List comprehension and list manipulation
- Exception handling (`try` / `except`)
- File paths with `pathlib`
- Input validation

## Project Files

- `day26_nato_phonetic_alphabet.py` — Main program.
- `nato_phonetic_alphabet.csv` — NATO phonetic alphabet data.

Both files must be in the same directory.

## How to Run

1. Make sure Python is installed.
2. Make sure both project files are in the same folder.
3. Run the following command:

```bash
python day26_nato_phonetic_alphabet.py
```

4. Enter a word or phrase.
5. Type `exit` to close the program.

## What I Learned

Through this project, I practised reading external data from CSV files, building dictionaries dynamically, working with functions, validating user input and handling exceptions.

I also learned how to organize a Python project using separate data and code files.
