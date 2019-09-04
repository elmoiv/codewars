def cakes(r,a):
    for i in list(r.keys()):
        if i not in list(a.keys()):
            return 0
    return sorted([int(round(a[i]/r[i])) for i in list(r.keys())])[0]
