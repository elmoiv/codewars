# Works only under python 2.7
def triple_double(n1, n2):
    return any(`n1`.count(i) > `n2`.count(i) > 1 for i in `n1`)
