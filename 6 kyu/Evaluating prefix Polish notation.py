import re
from operator import *

def calculate(e):
    op = {'+': add, '-': sub, '*': mul, '/': truediv}
    r = re.findall('([-+*/]) (-*\d+\.*\d*[-+e0-9]*) (-*\d+\.*\d*[-+e0-9]*)', e)
    for s, a, b in r:
        e = e.replace(' '.join((s, a, b)), str(op[s](float(a), float(b))))
    return calculate(e) if r else float(e)
