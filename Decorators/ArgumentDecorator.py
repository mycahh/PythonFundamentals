def functionA(functionB):
    
    def functionC(*args, **kwargs):
        print('Init...')
        result = functionB(*args, **kwargs)
        return result

    return functionC

@functionA
def sumar(a, b):
    return a + b

print(sumar(5, 3))