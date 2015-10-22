from __future__ import division
import numpy as np
import re
import time

def bruteforce():
    dat = np.loadtxt('e013.txt')
    num = '%i' % np.sum(dat)
    return int(num[:10])

def smarter():
    start = time.time()
    dat = []
    with open('e013.txt') as f:
        for line in f:
            l = []
            #print line
            for char in line.strip():
                #print char
                l.append(int(char))
            dat.append(l)

    dat = np.array(dat)
    #print dat
    tot = 0
    corr = int( np.log10( np.sum(dat[:,0]))) + 1
    print corr
    for i in range(n - corr):
        print n-corr -i,i
        tot = tot +  np.sum(dat[:,i]) * 10 ** (n-corr - i)
        print np.sum(dat[:,i])

    print tot

    jump, hurdle = 1, 0
    i = 1
    remainder = 0
    while (100 * jump > hurdle):
        hurdle = 10 ** i
        jump = np.sum(dat[:,n-corr+i]) + remainder * 10
        remainder = jump % hurdle
        
        print 'i, hurdle,np.sum(dat[:,9+i]),  jump, remainder, int(jump / hurdle)'
        print i, hurdle,np.sum(dat[:,9+i]),  jump, remainder, int(jump / hurdle)
        tot  = tot + int((jump) / hurdle)
        i = i + 1



    print 'result:'
    print tot
    print 'elapsed time:'
    print time.time()-start
    return tot

def solve():
    return bruteforce()



