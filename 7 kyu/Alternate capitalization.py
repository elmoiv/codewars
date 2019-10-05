def capitalize(s):
    s = ''.join(x.upper() if not n % 2 else x for n, x in enumerate(s))
    return [s, s.swapcase()]
