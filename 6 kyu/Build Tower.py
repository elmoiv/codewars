def tower_builder(n):
    return [('*' * i).center(n * 2 - 1) for i in range(1, 2 * n + 1, 2)]
