# As Tuple
def function(*args):
    print(*args)
    # print(*kwargs)

function('Daniel', 'Alice', 'Peter')

# As Dictionary
def function(**kwargs):
    print(kwargs.items())

function(Type='Acc', Component='Button')

# As tuple and Dictionary

def function(*args, **kwargs):
    print(kwargs.items())
    print(args)

function('Daniel', 'Alice', 'Peter', Type='Acc', Component='Button')
