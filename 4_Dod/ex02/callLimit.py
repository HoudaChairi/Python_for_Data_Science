

def callLimit(limit: int):
    """
    A decorator to limit the number of times
    a function can be called.
    """

    count = 0

    def callLimiter(function):
        """
        A function wrapper that tracks the number of times
        the target function is called.
        """

        def limit_function(*args, **kwds):
            """
            The wrapped function that enforces the call limit.
            """
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwds)
            else:
                print(f"Error: {function} call too many times")
        return limit_function
    return callLimiter
