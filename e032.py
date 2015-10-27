import itertools
import math
import numpy as np

def find_factor_candidates(charSet):
    """
    Generate suitable factors for a pandigital product.
    This function respects the constraints that no digit is repeated,
    and the number of digits of factors and product is constant.
    The multiplication of the factor is assumed to yield a product
    with as many digits as both factors taken together or one less.

    Parameters
    ----------
    charSet:  list
        digits from which factor may be chosen

    Yields
    ------
    a, b: strings
        candidate factors for a pandigital product

    Examples
    --------
    >>> [ a for a in find_factor_candidates('1234') ]
    ['123', 
     '124',
     ....

    """
    charSetLength = int(math.floor(len(charSet) / 2))
    for l in range(2, charSetLength + 1):
        for _a in itertools.combinations(charSet, l):
            for a in itertools.permutations(_a):
                remainingCharSet = charSet
                for char in a:
                    remainingCharSet = remainingCharSet.replace(char, '')
                for l2 in [charSetLength - l + 1]:
                    for _b in itertools.combinations(remainingCharSet, l2):
                        for b in itertools.permutations(_b):
                            yield map(''.join, [a, b])



def solve(verbose=False):
    results = []
    # take all reasonable value for the two
    # factors a b
    digit_set = '123456789'
    for a, b in find_factor_candidates(digit_set):
        t = a + b
        #first check: there are no repeat digits
        # in the factors
        assert len(set(t)) == len(t)
        prod  = int(a) * int(b)
        t = t + str(prod)
        if verbose:
            print  t
        # checks on all three numbers together:
        if '0' not in t:
            if len(t) == len(digit_set):
                if len(set(t)) == len(digit_set):
                    if verbose:
                        print ("found pandigital "
                               "%s * %s = %i" % (a, b, prod))
                    # found one, store it, repeat ...
                    results.append(prod)
    # count all pandigital lists only once
    result = np.sum(np.unique(results))
    return result

