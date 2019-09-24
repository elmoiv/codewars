import string, random

def generateName():
    a = list(string.printable)
    while not photoManager.nameWasUnique(a[:6]):
        random.shuffle(a)
    return ''.join(a[:6])
