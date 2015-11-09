
from Primes import is_pent, is_hex

def solve(n=100, verbose=True):
    result = 0
    test = [1, 6, 15, 28, 45]
    testp =[1, 5, 12, 22, 35]
    if verbose:
        print "check for known numbers:"
        print test,map(is_hex,test)
        print testp, map(is_pent,test)
    def triangle(num):
        return num*(num + 1) / 2
    i = 0
    while not result:
        i += 1
        num = triangle(i)
        if is_pent(num) and is_hex(num):
            if verbose:
                print "found one: ", num
            #we're looking for the next bigger one
            if num > triangle(285):
                result = num
    return result
