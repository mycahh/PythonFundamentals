from Person import Person

class Employee(Person):
    
    def __init__(self, name, job):
        super().__init__(name)
        self.job = job
    
    def __str__(self):
        return f'{super().__str__()} and I work as {self.job}'
