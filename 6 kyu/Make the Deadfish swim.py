def parse(data):
    res = []
    s = { 'i': lambda x: x + 1,
          'd': lambda x: x - 1,
          's': lambda x: x ** 2}
    n = 0
    for char in data:
        try:
            n = s[char](n)
        except:
            if char == 'o':
                res.append(n)
    return res
