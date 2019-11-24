def flatten(*args):
    args = list(args)
    while any(type(i) is list for i in args):
        for n, i in enumerate(args):
            if type(i) is list:
                for j in args.pop(n)[::-1]:
                    args.insert(n, j)
    return args
