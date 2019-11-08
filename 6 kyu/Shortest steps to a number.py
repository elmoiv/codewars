def shortest_steps_to_num(n):
    steps = -1
    while n:
        n = n - 1 if n % 2 else n / 2
        steps += 1
    return steps
