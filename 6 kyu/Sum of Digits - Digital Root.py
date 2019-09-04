def digital_root(n):
    return digital_root(sum(int(i) for i in str(n))) if n // 10 else n
