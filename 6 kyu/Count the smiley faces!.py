import re
def count_smileys(a):
    return len(re.findall(r'(:|;)(~|-)?(\)|D)', ''.join(a)))
