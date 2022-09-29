multiplication = (value * value for value in range(1, 10))

print(type(multiplication)) # Class Generator
print(next(multiplication))
print(next(multiplication))