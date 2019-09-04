def title_case(title, minor_words = ''):
    t = title.title()
    for i in minor_words.split():
        t = t.replace(i.title(), i.lower())
    return t[:1].upper() + t[1:]
