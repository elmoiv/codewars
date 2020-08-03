def namelist(n):
    l = len(n)
    n = list(map(lambda d: d['name'], n))
    return n[0]*(l<3)+', '.join(n[:-1])*(l>2)+(f' & {n[-1]}')*(l>1)if n else''
