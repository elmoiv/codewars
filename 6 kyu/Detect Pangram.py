def is_pangram(s):
    return not len(set(filter(str.isalpha, s.lower()))) ^ 26
