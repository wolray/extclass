from dataclasses import dataclass
from extclass import extension
from typing import cast
from pydantic import BaseModel


@dataclass
class Person1:
    first_name: str
    last_name: str


class Person2(BaseModel):
    first_name: str
    last_name: str


@extension
class PersonExt1(Person1):
    age: int = 10

    def full_name(self):
        return f'{self.first_name} {self.last_name}'


@extension
class PersonExt2(Person2):
    age: int = 10

    def full_name(self):
        return f'{self.first_name} {self.last_name}'


if __name__ == '__main__':
    person1 = Person1(first_name='rick', last_name='sanchez')
    person1 = cast(PersonExt1, person1)
    person2 = Person2(first_name='rick', last_name='sanchez')
    person2 = cast(PersonExt2, person2)
    print(person1.full_name())
    print(person1.age)
    print()
    print(person2.full_name())
    print(person2.age)
