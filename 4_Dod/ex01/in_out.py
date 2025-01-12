

def square(x: int | float) -> int | float:
    """Returns the square of the input value."""
    return x * x


def pow(x: int | float) -> int | float:
    """Returns the result of raising the input value to its own power."""
    return x ** x


def outer(x: int | float, function) -> object:
    """Returns a function that applies 'function' to 'x' and updates 'x'."""
    count = 0

    def inner() -> float:
        nonlocal x, count
        result = function(x)
        x = result
        count += 1
        return result
    return inner
