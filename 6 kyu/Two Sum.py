def two_sum(ns, tg):
    for i in range(len(ns)):
        for j in range(i + 1, len(ns)):
            if ns[i] + ns[j] == tg:
                return [i, j]
