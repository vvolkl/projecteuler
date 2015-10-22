from Primes import sieve

def solve(n=2000000):
    return sum(sieve(n))

