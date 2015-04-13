from __future__ import division
import sys

def findLargestFactor():
    f = int(n / 2)
    while (n % f):
        f = f - 1
    return f

def solve(n=600851475143):
    return findLargestFactor(n)
