# Inmutable Lists or tuples

FruitsBasket = ('Apples', 'Oranges', 'Pears')

# NO MODIFY, NO APPEND, NO INSERT, NO POP

# Length
len(FruitsBasket)

# How to modify?
FruitsBasket = list(FruitsBasket)
FruitsBasket.append('Banana')
FruitsBasket = tuple(FruitsBasket)

# Iter
for fruit in FruitsBasket:
    print(fruit, end=' ')

# Delete
del FruitsBasket