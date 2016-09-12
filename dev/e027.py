import numpy as np
from Primes import sieve
from bisect import bisect_left


#TODO: rewrite is_prime to make do without global

def solve(n=1000, verbose=False):
  #http://stackoverflow.com/questions/4545114
  # sqrt(1000000000) = 31622
  __primes = sieve(31622)
  def is_prime(n):
      # if prime is already in the list, just pick it
      if n <= 31622:
          i = bisect_left(__primes, n)
          return i != len(__primes) and __primes[i] == n
      # Divide by each known prime
      limit = int(n ** .5)
      for p in __primes:
          if p > limit: return True
          if n % p == 0: return False
      # fall back on trial division if n > 1 billion
      for f in range(31627, limit, 6): # 31627 is the next prime
            if n % f == 0 or n % (f + 4) == 0:
                return False
        return True

    result = 0
    winner = [0,0]
    for sign_a in [-1, 1]:
        for sign_b in [-1, 1]:
            for b in np.arange(0,1000):
                for a in np.arange(0, b):
                    b = sign_b * b
                    a = sign_a * a
                    stillprime = True
                    i = 0
                    while stillprime:
                        stillprime = is_prime(i*i + a*i + b)
                        i = i + 1
                    if i > result:
                        result = i
                        winner = a, b
                    if verbose:
                        print b, a, result, i
    return winner[0] * winner[1]


