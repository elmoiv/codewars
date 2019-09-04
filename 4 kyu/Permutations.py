from itertools import permutations as pr
def permutations(s):
    return [''.join(i) for i in sorted(set(pr(s)))]
