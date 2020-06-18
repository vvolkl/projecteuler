import numpy as np


def sum_multiples_numpy(n):
  d = np.arange(n)
  return np.sum(d[(d % 3 == 0) + (d % 5 == 0)])

def sum_multiples_loop(n):
  result = 0
  for i in range(1000):
    if (i % 3 == 0) or (i % 5 == 0):
      result += i
  return result
  


def solve(n=1000):
    return sum_multiples_numpy(n)
