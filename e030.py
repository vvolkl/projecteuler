def sumdigits(num,power):
    return sum([int(a)**power for a in str(num)])

def solve(n=400000):
    return sum([e for e in xrange(2,400000) if sumdigits(e,5) == e])

