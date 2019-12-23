def remove_vowels(strng):
    return strng.translate(str.maketrans('', '', 'aeiou'))

# Could ave been (Python 2.7):
def remove_vowels(s):
    return s.translate(None, 'aeiou')
