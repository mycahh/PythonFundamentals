def operation(a, b):

    return lambda: a + b

closure_function = operation(5, 3)
print(closure_function())

print(operation(5, 3)())