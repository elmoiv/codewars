def rgb(r, g, b):
    z = lambda x: max(0, min(x, 255))
    return ('%02x%02x%02x' % (z(r), z(g), z(b))).upper()
