from Car import Car

### Static Variable ###

Car1 = Car('Tesla X')
Car2 = Car('BMX X5')

if id(Car1.numberOfRubbers) == id(Car2.numberOfRubbers):
    print('Shared Memory Address')

if id(Car1.model) == id(Car2.model):
    print('Shared Memory Address')
else:
    print('NOT Shared Memory Address')

Car2.showInfo()

### Static Method ###

Car3 = Car('Araguaney 5000')
Car3.showInfoStatic()

### Class Method ###

Car4 = Car('Tesla 3')
Car3.showInfoClass()