def dig_pow(n, p):
    res = sum([int(i) ** (p + e) for e, i in enumerate(str(n))])
    if res % n == 0:
        return int(res / n)
    return -1
