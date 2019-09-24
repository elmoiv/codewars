def likes(names):
    n = len(names)
    if not n:
        return 'no one likes this'
    if n == 1:
        return names[0] + ' likes this'
    if n == 2:
        return ' and '.join(names) + ' like this'
    if n == 3:
        return ', '.join(names[:2]) + ' and ' + names[2] + ' like this'
    return ', '.join(names[:2]) + ' and ' + str(n - 2) + ' others like this'
