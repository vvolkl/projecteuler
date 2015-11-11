
def solve(n=10000, verbose=True):
    result = 0
    lycrels = []
    for i in range(n):
        temp = i
        j = 0
        done = 0
        if verbose:
            print 'checking ', i
        while j < 50  and not done:
            if verbose:
                print '\riteration ', j
            temp = temp + int(str(temp)[::-1])
            if str(temp)[::-1] == str(temp): 
                done = 1
                if verbose:
                    print 'found palindrome: ', temp
            j = j + 1 
        if done == 0:
            result += 1
            lycrels.append(i)
            if verbose:
                print 'found lycrel:', i
    return result
