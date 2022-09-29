class Car:
    numberOfRubbers = 4

    def __init__(self, model):
        self.model = model

    def showInfo(self):
        print(f'This car have {Car.numberOfRubbers} rubbers and its model is {self.model}')

    @staticmethod
    def showInfoStatic():
        ### Static Method don't access to self
        ### print(f'This car have {Car.numberOfRubbers} rubbers and its model is {self.model}') # ERROR
        print(f'This car have {Car.numberOfRubbers} rubbers')

    @classmethod
    def showInfoClass(cls):
        ### Static Method don't access to self
        ### print(f'This car have {Car.numberOfRubbers} rubbers and its model is {self.model}') # ERROR
        print(f'This car have {cls.numberOfRubbers} rubbers')