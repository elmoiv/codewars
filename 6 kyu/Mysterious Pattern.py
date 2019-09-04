def fib(m):
    lst = [1, 1]
    for i in range(m-2): lst.append(sum(lst[i:i+3]))
    return lst[:m]

def mysterious_pattern(m, n):
    n = [i % n for i in fib(m)]
    pat = ''
    for i in range(max(n)+1):
        for j in n:
            if j != i:
                pat += ' '
            else:
                pat += 'o'
        pat = pat.rstrip(' ') + '\n'
    return pat.strip('\n')
