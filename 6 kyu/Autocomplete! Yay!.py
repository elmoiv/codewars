def autocomplete(n, d):
    return [i for i in d if i.lower().startswith(''.join(i for i in n if i.isalpha()))][:5]
