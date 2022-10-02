def decoratorClass(cls):
    print('Execute Decorator')
    print(f'Received Object Type - {cls.__name__}')
    return cls

@decoratorClass
class Person:

    def __init__(self, name):
        print('Execute Constructor')
        self.__name = name
    
    @property
    def name(self):
        return self.__name
    
Person1 = Person('Peter')