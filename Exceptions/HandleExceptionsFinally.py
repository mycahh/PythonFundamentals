c = 0

try:
    a = int(input('First Number: '))
    b = int(input('Secound Number: '))

    c = a/b

except ZeroDivisionError as e:
    print(f'Error: {e} - {type(e)}')
except TypeError as e:
    print(f'Error: {e} - {type(e)}')
except Exception as e:
    print(f'Error: {e} - {type(e)}')
finally:
    print('Finished')


print(f'result: {c}')
print('running...') # Working
