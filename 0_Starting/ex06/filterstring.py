import sys
from ft_filter import ft_filter


def main():
    """
    Filters words from a given string based on their length.

    Usage:
        python script.py "<sentence>" <length>
    Example:
        python script.py "hello world python" 5
    Output:
        ['hello', 'python']
    """
    try:
        assert len(sys.argv) == 3, "the arguments are bad"

        s = sys.argv[1]
        try:
            N = int(sys.argv[2])
        except ValueError:
            raise AssertionError("the arguments are bad")

        words = s.split(" ")

        words_with_n = ft_filter(lambda word: len(word) > N, words)
        print(words_with_n)

    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == '__main__':
    main()
