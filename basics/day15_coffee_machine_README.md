# Coffee Machine Simulator

## Overview

This project is a command-line coffee machine simulator developed using Python.

It allows users to order espresso, latte and cappuccino while managing ingredients, processing payments and tracking profits.

## Learning Objectives

Through this project, I practised:

- Working with nested dictionaries.
- Defining and calling functions.
- Using while and for loops.
- Applying conditional statements.
- Validating user input.
- Managing resources and program state.
- Handling exceptions with try and except.
- Organising code into reusable functions.

## Features

- Three available drinks: espresso, latte and cappuccino.
- Resource management for water, milk and coffee.
- Payment processing using different coin values.
- Change calculation.
- Protection against insufficient resources.
- Input validation for coin quantities.
- Resource and profit reports.
- Option to shut down the machine.

## How It Works

The program stores drink recipes and prices in a dictionary called `MENU`.

When a user selects a drink, the program checks whether enough ingredients are available.

If the resources are sufficient, the machine processes the payment. Once the payment is successful, the ingredients are deducted and the drink is prepared.

## Project Structure

- `day15_coffee_machine.py`: Main coffee machine program.

## Testing

The following cases were tested:

| Test | Expected behaviour |
|---|---|
| Resource report | Displays available ingredients and profit |
| Valid order | Prepares the selected drink |
| Exact payment | Completes the transaction |
| Insufficient payment | Refunds the payment |
| Invalid drink | Displays an error message |
| Invalid coin input | Requests a valid number |
| Shutdown command | Stops the program |

## Limitations

- The program runs in the command line.
- It uses simulated payments rather than real transactions.
- It offers only three types of coffee.

## What I Learned

This project helped me understand how dictionaries can represent structured data and how functions can work together to manage a larger program.

I also improved my understanding of resource management, input validation and program flow.

## Future Improvements

- Add more drinks.
- Introduce a graphical user interface.
- Add automated unit tests.
- Allow the machine to refill its resources.
- Improve payment and transaction management.
