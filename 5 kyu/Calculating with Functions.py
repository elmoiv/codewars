funcs = {'zero': 0, 'one': 1 ,'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
for n in funcs:
    exec('def {}(a=""):return int(eval("{}"+str(a)))'.format(n, funcs[n]))

opers = {'plus': '+', 'minus': '-', 'times': '*', 'divided_by': '/'}
for o in opers:
    exec('def {}(a):return "{}"+str(a)'.format(o, opers[o]))
