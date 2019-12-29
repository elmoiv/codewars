# Works only under Python 2.7

def solution(args):
    l, t = [], []
    for i in args:
        if i + 1 in args:
            t += [`i`]
        else:
            l += ['{}-{}'.format(t[0], i)] if len(t) > 1 else t + [`i`]
            t = []
    return ','.join(l)
