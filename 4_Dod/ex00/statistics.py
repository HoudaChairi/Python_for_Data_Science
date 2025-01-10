def ft_statistics(*args, **kwargs) -> None:
    """
    A function that calculates various statistical measures such as mean,
    median, quartiles, variance, and standard deviation on a list of numbers
    provided as positional arguments. The specific measure to compute
    is determined by the keyword argument passed ('mean', 'median',
    'quartile', 'var', 'std').

    Parameters:
    *args: A list of numbers for statistical computation.
    **kwargs: A keyword argument specifying the statistical operation ('mean',
              'median', 'quartile', 'var', 'std') to be performed.

    Returns:
    None: Prints the result of the selected statistical operation.
    """
    try:

        numbers = [float(arg) for arg in args]
        numbers.sort()
    except (BaseException):
        print("ERROR")
        return

    def mean(data):
        return sum(data) / len(data)

    def median(data):
        n = len(data)
        mid = n // 2
        if n % 2 == 0:
            return (data[mid - 1] + data[mid]) / 2
        return data[mid]

    def quartiles(args):
        num_list = list(args)
        num_list.sort()
        median_num = median(num_list)

        one = median(list(filter(lambda x: x <= median_num, num_list)))
        two = median(list(filter(lambda x: x >= median_num, num_list)))

        return [one, two]

    def variance(data):
        m = mean(data)
        return sum((x - m) ** 2 for x in data) / len(data)

    def std(data):
        return variance(data) ** 0.5

    operations = {
        "mean": mean,
        "median": median,
        "quartile": quartiles,
        "var": variance,
        "std": std,
    }

    for key, value in kwargs.items():
        if value in operations:
            if len(args) > 0:
                result = operations[value](numbers)
                print(value, ":", result)
            else:
                print("ERROR")
