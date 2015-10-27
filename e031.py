
def tryCoin(res, iSize, coins, verbose=False):
    global result
    if verbose:
        print "%i left, trying coin %i pence" % (res, coins[iSize])
    global result
    t = res - coins[iSize]
    if t == 0:
        result = result + 1
        if verbose:
            print "hit zero, registering possibility %i" % result
    elif t > 0:
        tryCoin(t, iSize, coins)
        while iSize < len(coins)-1:
            iSize = iSize + 1
            if verbose:
                print "moving to smaller coin %i with index %i" % (coins[iSize], iSize)
            tryCoin(t, iSize, coins)

#TODO: make do without global
result = 0

def solve(n=200, verbose=False):
    coins  = [1,2,5,10,20,50,100,200][::-1]
    c = len(coins)
    if verbose:
        print "%i coins available" % c
    for i in range(c):
        if verbose:
            print "trying coin %i" % coins[i]
        tryCoin(n, i, coins)
    return result



