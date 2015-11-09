
import numpy as np
from itertools import combinations_with_replacement, permutations
from itertools import chain
from Primes import is_prime

#TODO: wow, this is obnoxious, even after adding comments

def flatten(container):
    for i in container:
        if isinstance(i, list) or isinstance(i, tuple):
            for j in flatten(i):
                yield j
        else:
            yield i


def solve(verbose=True, n=1000): 
    result = []
    for e in combinations_with_replacement(range(10), 4):
        # convert tuples of digits in numbers
        f = [reduce(lambda rst, d: rst * 10 + d, seq) for seq in permutations(e) if seq[0] != 0]
        # check to see if the candidate numbers in list f are prime
        f = np.unique(f)
        truth = np.array(map(is_prime,f))
        # three prime numbers qualify 
        if sum( truth ) > 2:
            # select the primes from the permutations
            f = np.array(f)[truth]
            # create a list of differences of the 
            diff = [[f[j]-f[i] for i in range(j)] for j in range(len(f))]
            if verbose:
                print "found candidates: ", f, 
            if sum([g.count(3330) for g in diff]) > 1:
                result.append([[[f[i],f[j]] for i in range(j) if f[j] - f[i] == 3330] 
                                        for j in range(len(f))])
            if verbose:
                print "found it: ", f
        if len(result) > 2:
            break
    result = list(flatten(result[-1]))
    result = np.unique(result)
    result = int(''.join(map(str, result)))
    return result 
