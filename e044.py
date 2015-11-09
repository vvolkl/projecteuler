
import numpy as np

def is_pent(num):
    a = np.sqrt(1./36 + 2./3 * num)
    b = 1./6
    #if verbose:
    #    print "calculating n... ",np.ceil(a+b), a+b, b-a
    return np.ceil(b  +  a) - ( b +  a) < 0.00000001

def pent(n):
    n = n + 1
    return n * (3 * n - 1) // 2 

def solve(n=10000, verbose=True):
    result = 0
    results = []
    #pen = [a * (3 * a - 1) / 2 for a in range(1,n)]
    l = n 
    j = l 
    while not result:
        j += 1 
        if verbose:
            print "checking bigger pent number", j
        for i in range(0,j):
            if is_pent(abs(pent(j)-pent(i))):
                if is_pent(pent(j) + pent(i)):
                    result = (j,i)  

    return result


