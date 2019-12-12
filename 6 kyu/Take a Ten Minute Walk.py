def isValidWalk(walk):
    a = walk.count('n') - walk.count('s')
    b = walk.count('w') - walk.count('e')
    return len(walk) == 10 and a == b == 0
