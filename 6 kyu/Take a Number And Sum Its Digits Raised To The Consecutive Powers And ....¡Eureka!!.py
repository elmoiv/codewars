def is_dig_pow(n):
    return n == sum(int(c) ** i for i, c in enumerate(str(n), 1))

def sum_dig_pow(a, b):
    return list(filter(is_dig_pow, range(a, b + 1)))
