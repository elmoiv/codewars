import math

def code(t):
    n = math.ceil(len(t)**0.5)
    t += chr(11) * (n*n - len(t))
    return '\n'.join(t[i:][::n][::-1] for i in range(n))

def decode(s):
    n = len(s.split('\n')[0])
    ch11 = n*n - len(s.replace('\n', '').replace(chr(11), ''))
    return ''.join(s.replace('\n','')[n-i-1:][::n] for i in range(n))[:-ch11]
