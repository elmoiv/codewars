def make_readable(s):
    return "{:02d}:{:02d}:{:02d}".format(s//3600, s//60%60, s%60)
