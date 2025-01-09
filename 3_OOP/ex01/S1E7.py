from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""
    def __init__(self, first_name, is_alive=True):
        """Initialize a Baratheon family member with given attributes."""
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        """Change the Baratheon's state to dead."""
        self.is_alive = False

    def __str__(self):
        """Return a string representation of the Baratheon family member."""
        return str((self.family_name, self.eyes, self.hairs))

    def __repr__(self):
        """Return an official string representation
        of the Baratheon family member."""
        return str((self.family_name, self.eyes, self.hairs))


class Lannister(Character):
    """Representing the Lannister family."""
    def __init__(self, first_name, is_alive=True):
        """Initialize a Lannister family member with given attributes."""
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        """Change the Lannister's state to dead."""
        self.is_alive = False

    def __str__(self):
        """Return a string representation of the Lannister family member."""
        return str((self.family_name, self.eyes, self.hairs))

    def __repr__(self):
        """Return an official string representation
        of the Lannister family member."""
        return str((self.family_name, self.eyes, self.hairs))

    @classmethod
    def create_lannister(self, first_name, is_alive):
        """Create and return a new Lannister family member."""
        return Lannister(first_name, is_alive)
