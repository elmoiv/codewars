from functools import reduce
def persistence(n):
    s = 0
    while n//10:
        n = reduce(lambda x, y: x*y, map(int, str(n)))
        s+=1
    return s
