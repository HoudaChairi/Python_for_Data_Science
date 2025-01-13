
import sys

def main():
    """
    A script that determines whether a given command-line argument is even or odd.

    - Accepts a single integer as input via command-line arguments.
    - Prints "I'm Even." if the number is even and "I'm Odd." if odd.
    - Handles errors for missing arguments, multiple arguments, and non-integer input.
    """
    try:
        if len(sys.argv) == 1:
            return
        assert len(sys.argv) == 2, "more than one argument is provided"
        
        try:
            number = int(sys.argv[1])
        except ValueError:
            raise AssertionError("The argument must be an integer.")

        if number % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
        
    except AssertionError as e:
        print(f"AssertionError: {e}")

if __name__ == '__main__':
    main()