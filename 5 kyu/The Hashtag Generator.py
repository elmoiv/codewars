def generate_hashtag(s):
    return '#' + s.title().replace(' ', '') if len(s) in range(1, 140) else False
