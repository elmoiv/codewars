def expanded_form(n):
    return ' + '.join([i + '0' * (len(str(n)) - (x + 1)) for x, i in enumerate(str(n)) if i != '0'])
