def gap(g, m, n):
    if n-m > 90000:
        n = m + 2000
    elif n-m > 2000:
        n = m + 1000
    prims = [i for i in range(m,n) if all(i%j for j in range(2,int(i**.5)+1))]
    for i in range(1,len(prims)):
        if prims[i] - prims[i-1] == g:
            return [prims[i-1], prims[i]]
    return None
