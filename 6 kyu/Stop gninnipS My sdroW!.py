def spin_words(sent):
    lst = sent.split(' ')
    for i in lst:
        if len(i) >= 5:
            g = list(i)
            g.reverse()
            lst[lst.index(i)] = ''.join(g)
    return ' '.join(lst)