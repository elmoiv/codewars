def meeting(s):
    return ''.join(f'({a}, {b})' for a, b in sorted([i.split(':')[::-1] for i in s.upper().split(';')]))
