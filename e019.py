import datetime

def solve():
    start_date = datetime.date(1901,1,1)
    end_date = datetime.date(2000,12,31)
    result = 0
    for n in range(int ((end_date - start_date).days) + 1):
        curr = start_date + datetime.timedelta(n)
        if curr.weekday() == 6 and curr.day == 1:
            result = result + 1
    return result

