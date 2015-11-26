
def solve(n=100, verbose=True):
    result = 0
    num = 1
    found_one = True
    while  num < n:
        curr_result = result
        for i in range(1, n):
            if len(str(i**num)) > num:
                num = num + 1
                break
            if len(str(i**num)) == num:
                result = result + 1
        if result == curr_result:
            found_one = False
    return result            
    


