def tribonacci(sig, n):
    if n < 3:return sig[:n]
    for i in range(n-3):sig.append(sum(sig[i:i+4]))
    return sig