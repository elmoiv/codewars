def fold_array(a, r):
    l, o = len(a) // 2, len(a) % 2
    return fold_array(list(map(sum, zip(a[:l], a[l + o:][::-1]))) + [a[l]] * o, r - 1) if r else a
