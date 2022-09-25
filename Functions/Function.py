# Simple Function
def helloWorld():
    print("Hello World")

# Default Parameter
def greet(name:str ='Peter'):
    print(f'Hello {name}')

greet('Daniel') # Print 'Hello Daniel'

# Return Function
def isNumber(value) -> bool:
    isInt = int == type(value)

    return isInt

Value1 = isNumber(10) 
Value2 = isNumber('10')

print(Value1) # True
print(Value2) # True