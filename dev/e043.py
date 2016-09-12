#TODO: performance

from itertools import permutations
from Primes import sieve

def check43(num, div):
    num = str(num)
    res = 1
    for i in range(len(div)):
        res *=  int(num[i+1:i+4]) % div[i] == 0
    return res
        
def solve(n=100, verbose=True):
    div = sieve(18)
    if verbose:
        assert check43(1406357289, div)
    pan = ''.join([str(a) for a in range(10)])
    result = 0
    for e in permutations(pan):
        e = ''.join(e)
        if check43(e, div):
            if verbose:
                print "found it!: ", e
            result = result + int( e )
    return result

