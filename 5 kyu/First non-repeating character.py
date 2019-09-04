def first_non_repeating_letter(string):
    for i in string:
        if string.lower().count(i.lower()) < 2:
            return i
    return ''
