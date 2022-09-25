from Person import Person

class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary
    
    def doThing(self):
        print('Working...')
