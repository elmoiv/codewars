def find_missing_letter(chars):
    l = list(map(ord, chars))
    return chr(l[[y - x for x, y in zip(l, l[1:])].index(2)] + 1)
