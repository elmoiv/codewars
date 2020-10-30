def shortener(m):
    r,s=160-len(m),m.split()
    return' '.join(s[:r])+''.join(map(lambda i:i[0].upper()+i[1:],s[r:]))if r<0and' 'in m else m
