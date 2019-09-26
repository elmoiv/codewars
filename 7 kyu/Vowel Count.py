def getCount(inputStr):    
    return sum(list(map(lambda x: x in 'aeiou', inputStr)))
