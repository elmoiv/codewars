from math import factorial as f
from functools import reduce

def listPosition(word):
    # n : Letter in position
    
    tot = 0
    
    # Generating a list of letters real indexes without duplicates
    nlet = [sorted(set(list(word))).index(i) + 1 for i in word]
    
    for i in range(0, len(word)):
        
        # Number of all letters numbers after  n
        f1 = len([c for c in nlet[i:] if c < nlet[i]])
        
        # All factorials of repeated letters multiplied starting from  n
        f2 = reduce(lambda x, y: x*y, [f(a) for a in [word[i:].count(b) for b in sorted(set(list(word)))]])
        
        # Factorial of reversed zero based letters index in (word)
        f3 = f(len(word[i + 1:]))
        
        # Storing the result of (f1/f2)*f3 and using int() to prevent any approximate value
        # Trying to solve the approximate value problem
        if f2 < 5000 and len(str(f3)) >= 20:tot += int((f3/100)/f2)*f1*100
        else:
            tot += int(f3/f2)*f1
    
    # Final Result is the rank as Zero based index so we add 1
    return tot + 1
