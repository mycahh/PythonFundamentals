def toSquareNumbers(nums):
    
    for i in nums:
        yield(i*i)
        print('...')

squaredNumbers = toSquareNumbers((1, 2, 3, 4, 5))

for num in squaredNumbers:
    print(num)