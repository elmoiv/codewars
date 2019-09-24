def find_it(seq):
    return seq[list(map(lambda x: seq.count(x)%2, seq)).index(1)]
