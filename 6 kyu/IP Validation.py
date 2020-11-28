import re

def is_valid_IP(strng):
    return bool(re.match(r'^(((1?[1-9]?|10|2[0-4])\d|25[0-5])($|\.(?!$))){4}$', strng))
