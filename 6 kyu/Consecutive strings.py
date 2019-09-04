def longest_consec(strarr, k):
    n, lst = len(strarr), []
    if n * k < 1 or k > n:
        return ''
    lst = [''.join(strarr[i:i + k]) for i in range(n - k + 1)]
    return max(lst, key=len)
