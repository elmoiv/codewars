def part(word):
    if word in adjectives:
        return "adjective"
    if word in nouns:
        return "common"
    for end in nouns:
        if word.endswith(end):
            for start in list(nouns) + list(adjectives):
                if start + end == word:
                    return "compound"
    return "neither"
