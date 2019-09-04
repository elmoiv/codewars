def sum_of_intervals(lst):
    lst, i = [sorted(set([i for i in lst if i[1] > i[0]])), 0]
    while True:
        if i == len(lst) - 1:
            return sum([r[1] - r[0] for r in lst])
        elif lst[i + 1][1] < lst[i + 0][1]:
            del lst[i + 1]
        elif lst[i + 0][1] > lst[i + 1][0]:
            lst = lst[:i] + [(lst[i + 0][0], lst[i + 1][1])] + lst[i + 2:]
        else:
            i += 1