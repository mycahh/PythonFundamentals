from dataclasses import dataclass

@dataclass
class Person:
    name: str

Person1 = Person('Ness')

print(Person1)
print(Person1.name)