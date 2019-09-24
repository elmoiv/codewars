def to_camel_case(text):
    s = text.replace('-','_').split('_')
    return ''.join(s[:1]) + ''.join(i.title() for i in s[1:])
