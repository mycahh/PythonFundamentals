import time

def function():
    
    for i in range(10000):
        print(i)
    
t1 = time.process_time()
function()
t2 = time.process_time()

function()
print(f'Before Function: {t1}')
print(f'After Function: {t2}')
