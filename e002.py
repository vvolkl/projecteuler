import numpy as np

def sumEvenFibonacci(up_to=4e6)
    even_terms_sum = 0
    a = 1
    b = 1
    while(a < up_to and b < up_to):
        a = a + b
        if (a % 2 == 0):
            even_terms_sum = even_terms_sum + a
        b = a + b
        if (a % 2 == 0):
            even_terms_sum = even_terms_sum + b
    return even_terms_sum

def solve(n=4e6):
    return sumEvenFibonacci(n)


