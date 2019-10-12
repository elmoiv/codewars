def accum(s):
    return '-'.join(i.upper() + i.lower() * n for n, i in enumerate(s))
