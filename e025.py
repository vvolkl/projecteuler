def solve(verbose=False):
    result = 2 
    a, b = 1, 1
    c = 2
    while c < 10**999:
        c = a + b
        result = result + 1
        a = b
        b = c
        if verbose:
            print result, c
    return result
