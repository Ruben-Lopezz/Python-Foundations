
import art

print(art.logo)

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]


def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    shift_amount %= len(alphabet)

    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter in alphabet:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
        else:
            output_text += letter

    return output_text


should_continue = True

while should_continue:
    direction = input(
        "Type 'encode' to encrypt, type 'decode' to decrypt:\n"
    ).strip().lower()

    if direction not in ("encode", "decode"):
        print("Invalid direction. Please choose encode or decode.")
        continue

    text = input("Type your message:\n").lower()

    try:
        shift = int(input("Type the shift number:\n"))
    except ValueError:
        print("Invalid shift. Please enter a whole number.")
        continue

    result = caesar(
        original_text=text,
        shift_amount=shift,
        encode_or_decode=direction
    )

    print(f"Here is the {direction}d result: {result}")

    restart = input(
        "Type 'yes' if you want to go again. Otherwise, type 'no'.\n"
    ).strip().lower()

    if restart != "yes":
        should_continue = False
        print("Goodbye!")
