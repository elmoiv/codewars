def unique_in_order(itr):
    l = []
    for i in itr:
        if l[-1:] != [i]:
            l.append(i)
    return l
