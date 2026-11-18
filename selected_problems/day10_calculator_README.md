# Python Calculator

## Overview

This project is a command-line calculator developed using Python.

It performs four basic mathematical operations: addition, subtraction, multiplication and division.

The calculator also allows users to continue calculations using the previous result.

## Learning Objectives

Through this project, I practised:

- Defining and calling functions.
- Using parameters and return statements.
- Working with dictionaries.
- Using functions as dictionary values.
- Implementing while and for loops.
- Using conditional statements.
- Handling exceptions with try and except.
- Validating user input.

## Features

- Addition, subtraction, multiplication and division.
- Continuous calculations using previous results.
- Input validation for numbers.
- Validation of mathematical operations.
- Protection against division by zero.
- Option to restart or exit the calculator.

## How It Works

The program defines four mathematical functions and stores them in a dictionary called `operations`.

The user selects an operation, enters two numbers and receives the result.

The program can then use that result as the first number in another calculation.

## Project Structure

- `day10_calculator.py`: Main calculator program.

## Testing

The following cases were tested:

| Test | Expected behaviour |
|---|---|
| Addition | Returns the correct sum |
| Subtraction | Returns the correct difference |
| Multiplication | Returns the correct product |
| Division | Returns the correct quotient |
| Division by zero | Displays an error message |
| Invalid numerical input | Requests a valid number |
| Invalid operation | Requests a valid operation |
| Continuous calculation | Reuses the previous result |

## Limitations

- The calculator runs in the command line.
- It supports basic mathematical operations only.
- It does not currently include advanced mathematical functions.

## What I Learned

This project helped me understand how functions can be stored and accessed through dictionaries.

I also improved my understanding of exception handling, input validation and program flow.

## Future Improvements

- Add exponentiation and square roots.
- Develop a graphical user interface.
- Add automated unit tests.
- Improve the display of mathematical results.
