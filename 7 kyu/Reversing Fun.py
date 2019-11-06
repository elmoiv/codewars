def reverse_fun(n):
    for i in range(len(n) - 1):
        n = n[:i] + n[i:][::-1]
    return n
