from __future__ import division
import numpy as np
import re
import time

n=1000000
lengths = np.zeros(n)

def lenCollatz(b):
    global lengths
    l = 0
    a = b
    seq = []
    while a > 1 :
        if a & 0x01 :
            a = 3 * a + 1
            seq.append(a)
            l = l + 1
        elif a<b:
            lengths[b] = l + lengths[a >> 1] + 1 
            seq.append(a)
            return lengths[b], seq            
        else:
            a = a >> 1
            l = l + 1
            seq.append(a)
            
    lengths[a] = l
    return l, seq 

def solve(n=1000000):
    global lengths
    maxl = 0
    maxj = 0
    l = 0
    j = 0
    i = np.arange(n)
    for jlen in i:
        l, j = lenCollatz(jlen)
        print jlen,l , maxl
        if l > maxl:
            maxl = l
            maxj = j
    result = np.where(lengths == np.max(lengths))[0]
    return result
