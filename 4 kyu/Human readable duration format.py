def format_duration(s):
    if not s: return 'now'
    now = [('year', 31536000),('day', 86400),('hour', 3600),('minute', 60),('second', 1)]
    for n, t in enumerate(now):
        now[n] = (t[0], s//t[1])
        s -= s//t[1] * t[1]
    txt = ["{} {}{}".format(j, i, 's'*(j > 1)) for i, j in now if j]
    return "{} and {}".format(', '.join(txt[:-1]), txt[-1]) if len(txt) > 1 else txt[0]
