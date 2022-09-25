number = 5

def getfactorial(int):
    if int == 1:
        return 1
    else:
        return int * getfactorial(int -1)
    
factorial = getfactorial(number)

print(f'The factorial of {number} is {factorial}')