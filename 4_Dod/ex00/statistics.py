def ft_statistics(*args, **kwargs) -> None:
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

    def quartiles(data):
        n = len(data)
        mid = n // 2
        if n % 2 == 0:
            q1 = median(data[:mid])
            q3 = median(data[mid:])
        else:
            q1 = median(data[:mid])
            q3 = median(data[mid + 1:])
        return [q1, q3]

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
