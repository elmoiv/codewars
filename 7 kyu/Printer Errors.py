def printer_error(s):
    return "{}/{}".format(len([x for x in s if ord(x) > 109]), len(s))
