def solve(arr):
    z = []
    for i in arr[::-1]:
        if i not in z:
            z.insert(0, i)
    return z
