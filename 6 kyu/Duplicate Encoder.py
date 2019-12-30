def duplicate_encode(word):
    return ''.join(')' if word.lower().count(i)>1 else '(' for i in word.lower())

# Second hit:
def duplicate_encode(w):
    w = w.lower()
    return ''.join(['(', ')'][w.count(i) > 1] for i in w)
