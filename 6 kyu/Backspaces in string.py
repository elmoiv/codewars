import re

def clean_string(s):
    return clean_string(re.sub(r'[^#]#|^#+', '', s)) if '#' in s else s
