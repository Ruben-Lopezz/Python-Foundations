# Day 24 — Mail Merge

## Description

This project automates the creation of personalized letters using a list of names and a letter template.

The program reads names from a text file, replaces the `[name]` placeholder in the letter template and generates a separate letter for each person.

## Features

- Reads names from a text file.
- Loads a letter template from another file.
- Replaces the `[name]` placeholder automatically.
- Generates a personalized letter for each name.
- Creates the output directory automatically if it does not exist.
- Handles missing files and invalid templates.
- Displays the total number of generated letters.

## Technologies and Concepts

- Python
- File handling (`open`)
- Reading and writing text files
- `pathlib` for file path management
- Functions
- String methods (`strip`, `replace`)
- Regular expressions (`re`)
- Exception handling (`try` / `except`)
- Directory creation with `mkdir`

## Project Structure

- `day24_mail_merge.py` — Main program.
- `Input/Names/invited_names.txt` — List of names.
- `Input/Letters/starting_letter.txt` — Letter template.
- `Output/ReadyToSend/` — Generated personalized letters.

## How to Run

1. Make sure Python is installed.
2. Make sure the input files are in their correct folders.
3. Open a terminal in the project directory.
4. Run:

```bash
python day24_mail_merge.py
```

5. Find the generated letters in `Output/ReadyToSend/`.

## What I Learned

Through this project, I practised working with files and directories, reading and writing text files, using functions to organize code and replacing text dynamically.

I also learned how to handle file errors and automate repetitive tasks with Python.
