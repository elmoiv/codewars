def get_length_of_missing_array(a):
    try:
        b = sorted(map(len, a))
        return 0 if [] in a or None in a else list(set(range(b[0], b[-1] + 1)) - set(b))[0]
    except: return 0
