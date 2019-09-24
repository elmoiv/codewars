from __future__ import division

def collatz(x, lst = None):
    if lst is None:
        lst = [str(x)]
    if x < 2:
        return '->'.join(lst)
    else:
        n = int(((7 - 5 * (pow(-1, x))) / 4) * x + (1 - pow(-1, x)) / 2)
        lst.append(str(n))
        return collatz(n, lst)
