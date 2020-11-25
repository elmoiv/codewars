import re
def remove_parentheses(s):
    return remove_parentheses(re.sub(r'\([^\(\)]*\)', '', s)) if ')' in s else s
