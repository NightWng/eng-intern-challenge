import sys


# Will utilize key value pairs to hold corresponding braille and english mappings
# Braille to English mapping
braille_to_english = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e", "OOO...": "f",
    "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j", "O...O.": "k", "O.O.O.": "l",
    "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o", "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r",
    ".OO.O.": "s", ".OOOO.": "t", "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x",
    "OO.OOO": "y", "O..OOO": "z", "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4",
    "O..O..": "5", "OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0",
    "..OO.O": ".", "..O...": ",", "..O.OO": "?", "..OOO.": "!", "..OO..": ":", "..O.O.": ";",
    "....OO": "-", ".O..O.": "/", ".OO..O": "<", "O..OO.": ">", "O.O..O": "(", ".O.OO.": ")",
    ".....O": "capital", ".O.OOO": "number", "......": "space"
}

# English to Braille mapping
english_to_braille = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..", "f": "OOO...",
    "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..", "k": "O...O.", "l": "O.O.O.",
    "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.", "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.",
    "s": ".OO.O.", "t": ".OOOO.", "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO",
    "y": "OO.OOO", "z": "O..OOO", ' ': "......", '0': ".OOO..", '1': "O.....", '2': "O.O...",
    '3': "OO....", '4': "OO.O..", '5': "O..O..", '6': "OOO...", '7': "OOOO..", '8': "O.OO..",
    '9': ".OO...", '.': "..OO.O", ",": "..O...", "?": "..O.OO", "!": "..OOO.", ":": "..OO..",
    ";": "..O.O.", "-": "....OO", "/": ".O..O.", "<": ".OO..O", ">": "O..OO.", "(": "O.O..O", ")": ".O.OO.",
}

# Checks if given input is Braille
def is_braille(input_text):
    return all(c in "O." for c in input_text)

# Braille -> Text Converter
def braille_to_text(braille):

    english_output = []
    capitalize_next = False
    number_mode = False

    for i in range(0, len(braille), 6):
        braille_char = braille[i:i + 6]

        if braille_char == "......":
            english_output.append(' ')
            number_mode = False  # reset number mode on space
        elif braille_char == ".O.OOO":
            number_mode = True
        elif braille_char == ".....O":
            capitalize_next = True
        else:
            if number_mode:
                # Numbers are in the range 1-0 as per Braille standard mapping
                number = braille_to_english.get(braille_char, '?')
                english_output.append(number)
            else:
                letter = braille_to_english.get(braille_char, '?')
                if capitalize_next:
                    letter = letter.upper()
                    capitalize_next = False
                english_output.append(letter)

    return ''.join(english_output)

# English -> Braille Converter
def text_to_braille(text):

    braille_output = []
    number_mode = False

    for char in text:
        if char.isdigit():
            if not number_mode:
                braille_output.append(".O.OOO")  # "number follows" indicator
                number_mode = True
            braille_output.append(english_to_braille[char])
        else:
            if number_mode:
                number_mode = False  # reset number mode when encountering a non-digit
            if char.isalpha():
                if char.isupper():
                    braille_output.append(".....O")  # "capital follows" indicator
                    char = char.lower()
                braille_output.append(english_to_braille[char])
            else:
                braille_output.append(english_to_braille.get(char, "......"))

    return ''.join(braille_output)


def main():
    # Read input from command-line arguments
    input_text = ' '.join(sys.argv[1:])

    if not input_text:
        return

    # Determine if input is Braille or English
    if is_braille(input_text):
        result = braille_to_text(input_text)
    else:
        result = text_to_braille(input_text)

    # Output the result without any extra formatting
    print(result)


if __name__ == "__main__":
    main()