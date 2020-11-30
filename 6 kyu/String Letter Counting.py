def string_letter_count(s):
    return''.join(y+x for x,y in{i:str(s.lower().count(i))for i in sorted(filter(str.isalpha,s.lower()))}.items())
