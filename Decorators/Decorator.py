def functionA(functionB):
    
    def functionC():
        print('Init...')
        functionB()
        print('Finish...')

    return functionC

@functionA
def show_message():
    print('Hello from function show_message')

show_message()