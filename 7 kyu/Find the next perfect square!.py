def find_next_square(sq):
    n = sq ** .5
    return (int(n) + 1) ** 2 if n == int(n) else -1
