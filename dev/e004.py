import math as gmpy2

def isSquare(n):
    root = gmpy2.sqrt(n)
    return root % 1 == 0  # '4.0' will pass, '4.1212' won't

def fermatFactor(n):
    assert n % 2 != 0  # Odd integers only
    a = gmpy2.ceil(gmpy2.sqrt(n))
    b2 = a * a - n
    while not isSquare(b2):
        a += 1
        b2 = a * a - n
    factor1 = a + gmpy2.sqrt(b2)
    factor2 = a - gmpy2.sqrt(b2)
    return int(factor1), int(factor2) 


def largestPalindromeProduct(numFactorDigits):
    lowerLim = 10**numFactorDigits
    firstFactor = lowerLim + 1
    halfPalindrome = 10**numFactorDigits - 1
    while( firstFactor > lowerLim):
        halfPalindrome = halfPalindrome - 1	
        fullPalindrome = lowerLim * halfPalindrome + int(str(halfPalindrome)[::-1])
        firstFactor, secondFactor = fermatFactor(fullPalindrome)
    return fullPalindrome 

def solve(n=2):
    return largestPalindromeProduct(3)

def test():
    assert largestPalindromeProduct(2) == 9009
    print 'test passed!'
