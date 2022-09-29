c = 0
a = 10
b = 0

try:
    c = a/b # ZeroDivisionError
except Exception as e:
    print(f'Error: {e}')

print(f'result: {c}')
print('running...') # Working
