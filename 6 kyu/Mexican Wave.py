def wave(s):
    return [s[:n] + s[n:].capitalize() for n, i in enumerate(s) if i != ' ']
