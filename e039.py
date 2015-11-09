import numpy as np

def solve(n=1000, verbose=True):
    result = 0
    results = np.zeros(n +1)
    for p in range(2,n + 1):
        #if verbose:
            #print 'checking p:',p
        for a in range(1,p+1):
            for b in range(1,p-a):
                c = p - a - b
                #if verbose:
                 #   print 'checking sides ', a,b,c
                if a ** 2 + b ** 2 == c**2:
                    if verbose:
                        print "\t found one: ", a, b, c, p
                    results[ p ] += 1
    result = np.where(results == np.amax(results))[0]
    return result

