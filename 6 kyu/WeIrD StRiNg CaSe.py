def to_weird_case(s):
    return ' '.join(''.join(i.lower() if n % 2 else i.upper() for n, i in enumerate(w)) for w in s.split())
