def anagrams(word, words):
    word = sorted(word)
    return filter(lambda w: sorted(w) == word, words)
