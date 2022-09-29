from NoDuplicity import NoDuplicity

c = 0

try:
    a = int(input('First Number: '))
    b = int(input('Secound Number: '))

    if a == b:
        # raise ValueError('Generic message') # Any Exception
        raise NoDuplicity('Don\'t allow identical number')

    c = a/b

except ZeroDivisionError as e:
    print(f'Error: {e} - {type(e)}')
except TypeError as e:
    print(f'Error: {e} - {type(e)}')
except Exception as e:
    print(f'Error: {e} - {type(e)}')
else:
    print('Ok')


print(f'result: {c}')
print('running...') # Working
