def next_bigger(n):
    s = str(n)
    for i in range(-1, -len(s), -1):
        if int(s[i-1]) < int(s[i]):
            main, rest = ''.join(s[:i]), ''.join(sorted(s[i:]))
            for d in range(len(rest)):
                if int(main[-1]) < int(rest[d]):
                    f = int(main[:-1] + rest[d] + ''.join(sorted(main[-1] + rest[:d] + rest[d + 1:])))
                    return f if f > n and len(str(f)) == len(s) else -1
    return -1
