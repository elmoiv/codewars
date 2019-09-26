def high_and_low(numbers):
    n = sorted([int(i) for i in numbers.split()])
    return str(max(n)) + ' ' + str(min(n))
