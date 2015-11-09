
from __future__ import division
from itertools import combinations_with_replacement, permutations
from Primes import is_prime
import numpy as np

def solve(n=100, verbose=True):
    result = []
    for e in combinations_with_replacement(range(10),4):
        f = [reduce(lambda rst, d: rst * 10 + d, seq) for seq in permutations(e) if seq[0] != 0]
        truth = np.array(map(is_prime,f))
        if sum( truth ) > 2:
            f = np.array(f)[truth]
            diff = [[f[j]-f[i] for i in range(j)] for j in range(len(f))]
            if verbose:
                print "found candidates: ", f, 
            if sum([g.count(3330) for g in diff]) > 1:
                result.append(np.unique(np.array([[[f[i],f[j]] for i in range(j) if f[j] - f[i] == 3330] for j in range(len(f))] ).flatten()))
                if verbose:
                    print "found it: ", f
        if verbose:
            print e,f
        if len(result) > 2:
            break
    return int(result[-1] )
        

