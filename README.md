# Ext-Class
Adding fields/methods to existing classes. 

A Python approach to the great `extensions` feature in C# and Kotlin, and probably the closest.

## How to use
```
pip install extclass 
```
Suppose you have a `Person` class in an already installed package:
```python
from dataclasses import dataclass

@dataclass
class Person:
    first_name: str
    last_name: str
```
Then, you could add an extra method outside the source package somewhere in your project.
```python
from extclass import extension

@extension
class PersonExt(Person):
    age: int = 10

    def full_name(self):
        return f'{self.first_name} {self.last_name}'
```
With the help of the `@extension` decorator, new field `age` and `full_name` are added to the origin `Person` class. You can just call them as usual.
```python
if __name__ == '__main__':
    person = Person(first_name='rick', last_name='sanchez')
    print(person.full_name())
    print(person.age)
```
which print as
```text
rick sanchez
10
```
However, the IDE cannot know the dynamic informations of the added attributes, so there would be a warning message:
```text
Unresolved attribute reference 'full_name' for class 'Person' 
```
And no autocomplete for the attributes in the IDE.

To handle the warnings also enabling autocomplete, you can simply `typing.cast` the origin object to the new extended type.
```python
from typing import cast

person = cast(PersonExt, person)
```
In this case, `person` is still the old object but only marked as the extended type in order to cheat the IDE for better programming experiences.

### No Override
Same method/field name in the extending class will not affect the origin class. So this package is very safe in any use-cases.

### Pydantic issues
Classes of `pydantic.BaseModel` can only attach new methods. Dynamic fields are internally forbidden by the pydantic package. So please do **NOT** extend fields for pydantic models, or an `AttributeError` would be raised during runtime.

### Full examples
See [test.py](tests/test.py)