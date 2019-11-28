def most_money(s):
    d = {i.fives * 5 + i.tens * 10 + i.twenties * 20: i.name for i in s}
    return 'all' if len(d) == 1 and len(s) > 1 else d[max(d)]
