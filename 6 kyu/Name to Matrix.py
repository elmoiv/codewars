import math, re
def matrixfy(st):
    if st:
        l = int(math.ceil(len(st) ** .5))
        return map(list, re.findall('.' * l, st.ljust(l * l, '.')))
    return "name must be at least one letter"
