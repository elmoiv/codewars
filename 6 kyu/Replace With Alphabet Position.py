def alphabet_position(text):
    return ' '.join(str(ord(i)-96) for i in filter(str.isalpha, text.lower()))
