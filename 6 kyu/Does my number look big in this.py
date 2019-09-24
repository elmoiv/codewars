def narcissistic(val):
    return val == sum(int(i)**len(str(val)) for i in str(val))
