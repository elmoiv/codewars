import re
def increment_string(strng):
    num = strng.replace(re.split(r'\d+$', strng)[0], '')
    if num == '':
        return strng + '1'
    return strng[:-len(num)] + str(int(num) + 1).rjust(len(num), '0')