class Person:
    
    def __init__(self, name):
        self.__name = name
    
    def greet(self):
        print(f'Nice to meet you, my name is {self.__name}')

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name

class PersonOnlyRead:
    
    def __init__(self, name):
        self.__name = name
    
    def greet(self):
        print(f'Nice to meet you, my name is {self.__name}')

    @property
    def name(self):
        return self.__name
    
    