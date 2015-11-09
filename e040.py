import numpy as np

def solve(n=6, verbose=False): 
    counter, result  = 1, 1
    length = 0
    interesting = []
    for e in range(1,n+1):
        interesting.append(10**e)
    i = 0
    if verbose:
        print "interesting: ", interesting
    #while length < max( interesting ):
    while i < len(interesting):
    #    if verbose:
    #        print counter
        length += len(str(counter))
    #    if verbose:
    #        print length, interesting[i]
        if length >= interesting[i]:
            digit =  int( str( counter)[::-1][length - interesting[i] ]  ) 
            result *= digit
            if verbose:
                print "found it: length: ", length," new number: ", 
                print counter," result so far: ", result, "digit that was added: ", digit 
            i += 1
        counter += 1
    return result
