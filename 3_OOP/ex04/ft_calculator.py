

class calculator:
    """
    A utility class for performing basic vector operations,
    including dot product, addition, and subtraction.
    """

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """
        Prints the dot product of two vectors.
        """
        result = float(sum(x * y for x, y in zip(V1, V2)))
        print(f"Dot product is: {result}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """
        Prints the sum of two vectors (element-wise).
        """
        result = [float(x + y) for x, y in zip(V1, V2)]
        print(f"Add Vector is : {result}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """
        Prints the difference of two vectors (element-wise).
        """
        result = [float(x - y) for x, y in zip(V1, V2)]
        print(f"Sous Vector is: {result}")
