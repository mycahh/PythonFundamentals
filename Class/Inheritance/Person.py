class Person:
    
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        print(f'Nice to meet you, my name is {self.name}')

    def doThing(self):
        print('Reading...')