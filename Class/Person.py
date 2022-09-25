class Person:
    
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f'Name: {self.name}'

    def __del__(self):
        print('This object has been destroyed')
    
    def greet(self):
        print(f'Nice to meet you, my name is {self.name}')


