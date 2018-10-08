
from math import factorial

def solve(n=100, verbose=False):
    result = 0
    for num in xrange(3,100000):
        s = str(num)
        if sum(map(factorial, map(int,s))) == num:
            if verbose:
                print "found it! %i" % num
            result = result + num
    return result

