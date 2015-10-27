import numpy as np

def rot(arr):
    return [arr[1],-arr[0]]
    



def bruteforce(n=1001, verbose=False):
    spiral = np.zeros((n,n))
    #fill the spiral
    pos = np.array([np.floor(n / 2)] * 2 )
    vec = np.array([0, 1])
    i = 0
    while 0<=pos[0]<n and 0<=pos[1]<n: 
        i = i + 1
        spiral[pos[0], pos[1]] = i
        pos = pos + vec 
        rotvec = rot(vec)
        if verbose:
            print spiral
        try:
            if not spiral[pos[0]+rotvec[0], pos[1] + rotvec[1]]:
                vec = rotvec
        except IndexError:
            break
    result = np.sum(np.diagonal(spiral))
    result = result + np.sum(np.diagonal(np.rot90(spiral)))
    # the center entry is counted twice
    return result - 1

def solve(n=1001, verbose=False):
    return bruteforce(n=n, verbose=verbose)
