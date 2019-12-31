def high(x):
    return max(x.split(), key = lambda w: sum(ord(c) % 96 for c in w))
