def disemvowel(s):
    return ''.join(filter(lambda x: x.lower() not in 'aeiou', s))
