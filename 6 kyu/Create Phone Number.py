def create_phone_number(n):
    s = ''.join(str(e) for e in n)
    return f'({s[:3]}) {s[3:6]}-{s[6:]}'
