def solution(a):
    l, i, t = len(a), 0, 0
    
    while 0 <= i < l and t <= l:
        i += a[i]
        t += 1
    
    return -1 if t > l else t
