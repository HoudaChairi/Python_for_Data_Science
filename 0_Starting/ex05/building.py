import sys


def main():
    '''
      This function processes a string passed
      as a command-line argument and counts:
        - Uppercase letters
        - Lowercase letters
        - Punctuation marks
        - Spaces
        - Digits
        The function then prints a summary of the counts for each category,
        as well as the total number of characters in the input string.
    '''
    try:
        assert len(sys.argv) <= 2, "more than one argument is provided"

        if len(sys.argv) == 1:
            sentence = input("What is the text to count?\n")
        else:
            sentence = sys.argv[1]

        uppercase_count = 0
        lowercase_count = 0
        punctuation_count = 0
        space_count = 0
        digit_count = 0
        punctuation_chars = """!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"""

        for char in sentence:
            if char.isupper():
                uppercase_count += 1
            elif char.islower():
                lowercase_count += 1
            elif char in punctuation_chars:
                punctuation_count += 1
            elif char.isspace():
                space_count += 1
            elif char.isdigit():
                digit_count += 1

        count_chars = len(sentence)

        print(f"The text contains {count_chars} characters:")
        print(f"{uppercase_count} upper letters")
        print(f"{lowercase_count} lower letters")
        print(f"{punctuation_count} punctuation marks")
        print(f"{space_count} spaces")
        print(f"{digit_count} digits")

    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == '__main__':
    main()
