
import sys

def main():
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