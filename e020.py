import math

def solve(n=100):
    digits = str(math.factorial(n))
    result = reduce(lambda x,y: x+y, [int(d) for d in digits])
    return result 

