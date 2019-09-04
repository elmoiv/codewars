def get_middle(s):
    n = int((len(s) - 1) / 2)
    return s[n: n + 2 - len(s) % 2]
