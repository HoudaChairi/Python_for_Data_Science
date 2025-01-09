

class calculator:
    """
    A Calculator class to perform element-wise addition,
    subtraction, multiplication, and division between
    a vector and a scalar.
    """
    def __init__(self, vector):
        self.vector = vector

    def __add__(self, object) -> None:
        self.vector = [x + object for x in self.vector]
        print(self.vector)

    def __mul__(self, object) -> None:
        self.vector = [x * object for x in self.vector]
        print(self.vector)

    def __sub__(self, object) -> None:
        self.vector = [x - object for x in self.vector]
        print(self.vector)

    def __truediv__(self, object) -> None:
        try:
            if object == 0:
                raise ValueError("Cannot divide by zero")
            self.vector = [x / object for x in self.vector]
            print(self.vector)
        except ValueError as e:
            print(f"ValueError: {e}")
