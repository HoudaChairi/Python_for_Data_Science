import sys


def main():
    '''
    Converts an input string to Morse code.

    The function takes a string as a command-line argument,
    converts it to uppercase, and then converts each character
    into its Morse code equivalent.
    It prints the Morse code with each character's
    Morse code separated by a space.
    '''
    try:
        assert len(sys.argv) == 2, "the arguments are bad"
        s = sys.argv[1]

        MORSE = {
            " ": "/",
            "A": ".-", "B": "-...", "C": "-.-.", "D": "-..",
            "E": ".", "F": "..-.", "G": "--.", "H": "....",
            "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
            "M": "--", "N": "-.", "O": "---", "P": ".--.",
            "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
            "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
            "Y": "-.--", "Z": "--..",
            "0": "-----", "1": ".----", "2": "..---", "3": "...--",
            "4": "....-", "5": ".....", "6": "-....",
            "7": "--...", "8": "---..", "9": "----."
        }

        s = s.upper()
        new_String = ""
        for i in s:
            if i in MORSE:
                new_String += MORSE[i] + ' '
            else:
                raise AssertionError("the arguments are bad")
        print(new_String.strip())

    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == '__main__':
    main()
