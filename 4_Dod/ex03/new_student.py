import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """
    Generate a random 15-character student ID.
    """
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """
    A class to represent a student.

    Attributes:
        name (str): Student's first name.
        surname (str): Student's last name.
        active (bool): Student's active status (default is True).
        login (str): Student's login name.
        id (str): Unique student ID.
    """
    name: str = field(init=True)
    surname: str = field(init=True)
    active: bool = field(default=True)
    login: str = field(init=False)
    id: str = field(init=False, default=generate_id())

    def __post_init__(self):
        self.login = self.name[0].capitalize() + self.surname.lower()
