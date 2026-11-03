# Caesar Cipher

## Overview

This project is a Python implementation of the Caesar Cipher, a simple encryption and decryption technique.

It allows users to encode and decode messages by shifting letters through the alphabet.

## Learning Objectives

Through this project, I practised:

- Python functions and parameters.
- Lists and string manipulation.
- For loops and while loops.
- Conditional statements.
- The modulo operator.
- User input and validation.
- Exception handling with `try` and `except`.

## How It Works

The program shifts each letter in a message by a chosen number of positions.

For example, shifting `hello` by 5 positions produces `mjqqt`.

When decoding, the program reverses the shift.

Characters that are not in the alphabet, such as spaces and punctuation, remain unchanged.

## Project Structure

- `day8_caesar_cipher.py`: Main program containing the encryption and decryption logic.

## Testing

The following cases were tested:

| Operation | Input | Shift | Expected output |
|---|---|---:|---|
| Encode | hello | 5 | mjqqt |
| Decode | mjqqt | 5 | hello |
| Encode | xyz | 3 | abc |
| Encode | hello world! | 5 | mjqqt btwqi! |

Invalid directions and non-numeric shift inputs were also tested.

## Limitations

- The program currently works with lowercase English letters.
- It is an educational exercise, not secure encryption.
- It does not provide modern cryptographic protection.

## What I Learned

This project helped me understand how functions, loops, lists and mathematical operations can work together to solve a programming problem.

I also practised input validation and separating the main encryption logic from the user interface.

## Future Improvements

- Support uppercase letters.
- Improve the user interface.
- Add automated tests.
- Separate the encryption logic into a reusable module.
