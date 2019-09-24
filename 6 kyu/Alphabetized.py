def alphabetized(s):
    return ''.join(sorted([l for l in s if l.isalpha()], key=str.lower))
