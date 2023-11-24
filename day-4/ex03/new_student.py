import random
import string
from dataclasses import dataclass, field
def generate_id() -> str:
    """ generate ramdom id 15 char long
        https://docs.python.org/3/library/dataclasses.html"""
    return "".join(random.choices(string.ascii_lowercase, k = 15))



@dataclass
class Student:
    name: str = field(init=True)
    surname: str = field(init=True)
    active: bool = field(default=True)
    login: str = field(init=False)
    id: str = field(init=False, default=generate_id())

    def __post_init__(self):
        self.login = self.name[0].capitalize() + self.surname.lower()
