def operation(a, b):

    def Addition():
        return a + b

    return Addition 

closure_function = operation(5, 3)
print(closure_function())

print(operation(5, 3)())