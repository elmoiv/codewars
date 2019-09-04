def reverse_letter(text):
    for i in list(r'!#$"%&()*+, -./:;'+"'"+'<=>?@[\]^_`{|}~0123456789'):
        text = text.replace(i,'')
    return ''.join(list(reversed(text)))
