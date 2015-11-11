
def has_same_digits(a, b):
    for char in a:
        b = b.replace(char,'',1)
    return b == ''


def solve(n=6, verbose=False):
    number = 0
    result = 0
    while not result:
        multiplier = 1
        while ( has_same_digits(str(number*multiplier), str((multiplier+1)*number)) 
                and multiplier < n ):
            if multiplier == n - 1:
                result = number
            multiplier += 1
        if verbose:
            print number, multiplier
        number += 1
    return result
     
