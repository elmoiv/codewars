def pattern(n):
    a = ('1234567890' * 100)[:n]
    return '\n'.join(i.rjust(n) for i in list(a[:-1]) + [a + a[:-1][::-1]] + list(a[:-1][::-1])) + '\n'
