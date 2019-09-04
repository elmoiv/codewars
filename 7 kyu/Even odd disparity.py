def solve(a):
    return sum(1 if i==0 or not i % 2 else -1 for i in a if type(i) == int)
