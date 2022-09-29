class Person:
    def __init__(self, name):
        self.name = name
    
    def __add__(self, other):
        return (f'{self.name} {other.name}')