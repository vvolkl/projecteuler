from __future__ import division
import sys

def bruteforce(n):
    # the largest factor can be at most n / 2
    cand = int(n / 2)
    # decrease f until it becomes a factor
    while (n % cand):
        print n
        cand = cand - 1
    return f


def findLargestFactor(n):
    factor = 1 
    while n > 1:
      factor = factor + 1
      if n % factor == 0:
          n = int(n / factor)
    return factor

def solve(n=600851475143):
    return findLargestFactor(n)
