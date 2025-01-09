from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Class representing a King, inheriting from Baratheon and Lannister."""
    def __init__(self, first_name, is_alive=True):
        """Initialize a King with attributes
        from both Baratheon and Lannister."""
        Baratheon.__init__(self, first_name, is_alive)

    def set_eyes(self, color):
        """Set the eyes color of the King."""
        self.eyes = color

    def set_hairs(self, color):
        """Set the hairs color of the King."""
        self.hairs = color

    def get_eyes(self):
        """Return the eyes color of the King."""
        return self.eyes

    def get_hairs(self):
        """Return the hairs color of the King."""
        return self.hairs

    def __str__(self):
        """Return a string representation for debugging."""
        return str({
            'first_name': self.first_name,
            'is_alive': self.is_alive,
            'family_name': self.family_name,
            'eyes': self.eyes,
            'hairs': self.hairs
        })
