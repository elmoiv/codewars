def make_password(phrase):
    return ''.join({'i':'1', 'o':'0', 's':'5'}[l[0].lower()] if l[0].lower() in 'ios' else l[0] for l in phrase.split())
