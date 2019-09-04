def snail(array):
    final = []
    for n in range(len(array)):
        final += array[n][n:len(array) - n]
        for e in range(n + 1, len(array) - n):
            final += [array[e][- n - 1]]
        final += array[- n - 1][n:len(array) - n - 1][::-1]
        for j in range(n + 2, len(array) - n):
            final += [array[-j][n]]
    return final
