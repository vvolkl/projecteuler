from itertools import chain, combinations
import numpy as np

def factors2(n): 
    result = []
    # test 2 and all of the odd numbers
    # xrange instead of range avoids constructing the list
    for i in chain([2],xrange(3,n+1,2)):
        s = 0
        while n%i == 0:  #a good place for mod
            n /= i
            s += 1
        result.extend([i]*s) #avoid another for loop
        if n==1:
            return result

def allsubsets(n):
    return list(chain(*[combinations(np.arange(0,n), ni) for ni in np.arange(1,n)]))

def divisorsum(a):
    a = factors2(a)
    na = len(a)
    h = np.array([list(e) for e in allsubsets(na)])
    return np.sum(np.unique( map(np.prod, [[a[e] for e in f] for f in h]))) + 1

def gen_abundant(): 
    abundant = []
    for i in np.arange(1,28123):
        e = divisorsum(i)
        if e > i:
            if verbose:
                print i,e
            abundant.append(i)
    np.savetxt('e023abundant.txt',np.array(abundant))
    return abundant

def gen_sums():
    sums = []
    i = 0
    for e in abundant:
        i = i + 1
        if verbose:
            print i
        for f in abundant[0:i]:
            sums.append(f+e)

    sums = np.unique(sums)
    sums = np.sort(sums)
    np.savetxt('e023sums.txt', sums)

def solve(verbose=False):
    abundant = np.loadtxt('e023abundant.txt')
    result = 0
    sums = np.loadtxt('e023sums.txt')
    if verbose:
        print len(sums)
        print sums[0:10]

    for e in np.arange(0,28124):
        if e not in sums:
            if verbose:
                print e
            result = result + e
    return result


