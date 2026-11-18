
import csv
from pathlib import Path


def load_phonetic_dictionary():
    file_path = Path(__file__).with_name(
        "nato_phonetic_alphabet.csv"
    )

    with open(file_path, mode="r", encoding="utf-8", newline="") as file:
        data = csv.DictReader(file)

        phonetic_dict = {
            row["letter"].upper(): row["code"]
            for row in data
        }

    return phonetic_dict


def generate_phonetic_spelling(word, phonetic_dict):
    word = word.strip().upper()

    if not word:
        raise ValueError("Please enter a word.")

    output_list = []

    for letter in word:
        if letter == " ":
            continue

        if letter not in phonetic_dict:
            raise ValueError(
                "Please use letters from the English alphabet only."
            )

        output_list.append(phonetic_dict[letter])

    return output_list


def main():
    phonetic_dict = load_phonetic_dictionary()

    while True:
        word = input(
            "\nEnter a word or phrase (or type 'exit' to quit): "
        ).strip()

        if word.lower() == "exit":
            print("Goodbye!")
            break

        try:
            result = generate_phonetic_spelling(
                word, phonetic_dict
            )
            print("Phonetic spelling:", " - ".join(result))

        except ValueError as error:
            print(error)


if __name__ == "__main__":
    main()

