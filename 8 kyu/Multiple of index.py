def multiple_of_index(arr):
    return [i for n, i in enumerate(arr) if n and not i%n]
