def iq_test(numbers):
    n = map(lambda x:x % 2 ,map(int, numbers.split()))
    return n.index(0) + 1 if not n.count(0) - 1 else n.index(1) + 1
