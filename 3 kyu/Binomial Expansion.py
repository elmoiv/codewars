import re
from math import factorial as f

def expand(expr):
	form = re.compile(r'\((-?)?(\d+)?(\w)([+-]?\d+)\)\^(\d+)').split(expr)[1:-1]
	if None in form:
        form[form.index(None)] = '1'
	if form[0] in ['-', '']:
        form = [form[0] + form[1]] + form[2:]
	a, b, n, x = [int(z) for z in form if not z.isalpha()] + [form[1]]
	if n == 0:
        return '1'
	if b == 0:
        return '-' * (a < 0) + x + '^' + str(n) if a in [1, -1] else str(a ** n) + x + '^' + str(n) 
	lst = [str(int((f(n) / (f(n - i) * f(i))) * (a ** (n - i)) * (b ** i))) + (x + '^' + str(n - i)) for i in range(n + 1)]
	lst = ''.join(['+' * (e[0] != '-' and lst.index(e) > 0) + e.replace(x + '^0', '').replace(x + '^1', x) for e in lst])
	return lst.replace('1' + x, x) if lst.startswith('-1' + x) or lst.startswith('1' + x) else lst
