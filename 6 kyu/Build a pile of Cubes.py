def find_nb(m, t=0, n=1):
    while t < m: t, n = t + n ** 3, n + 1
    return [n - 1, -1][t != m]
