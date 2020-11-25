import re

def unpack_sausages(t):
    x = re.findall(r'\[(.)\1{3}\]', str(t))
    del x[4::5]
    return ' '.join(' '.join([i] * 4) for i in x)
