from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract base class for characters in the game."""

    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        """Initialize a character with a first name and alive status."""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Change the character's state to dead."""
        pass


class Stark(Character):
    """Class representing a Stark character."""

    def __init__(self, first_name, is_alive=True):
        """Initialize a Stark character with a first name and alive status."""
        super().__init__(first_name, is_alive)

    def die(self):
        """Change the character's state to dead."""
        self.is_alive = False
