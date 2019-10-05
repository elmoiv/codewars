def sort_transform(arr):
    t = lambda lst: ''.join(chr(i) if type(i) != str else i for i in lst[:2] + lst[-2:])
    return '-'.join([t(arr), t(sorted(arr)), t(sorted(arr, reverse = True)), t(sorted([chr(i) for i in arr]))])
