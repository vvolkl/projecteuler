import math as gmpy2

def fermat_factor(n):
    assert n % 2 != 0  # Odd integers only

    a = gmpy2.ceil(gmpy2.sqrt(n))
    b2 = a * a - n
    while not is_square(b2):
        a += 1
        b2 = a * a - n

    factor1 = a + gmpy2.sqrt(b2)
    factor2 = a - gmpy2.sqrt(b2)
    return int(factor1), int(factor2) 

def is_square(n):
    root = gmpy2.sqrt(n)
    return root % 1 == 0  # '4.0' will pass, '4.1212' won't

firstFactor = 1001
palindromeHalf = 999
while( firstFactor > 1000):
	palindromeHalf = palindromeHalf - 1	
	fullPalindrome = 1000 * palindromeHalf + int(str(palindromeHalf)[::-1])
	firstFactor, secondFactor = fermat_factor(fullPalindrome)
	print fullPalindrome, firstFactor, secondFactor 


