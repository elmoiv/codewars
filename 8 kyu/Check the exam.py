def check_exam(a1,a2):
    s = sum([[4,-1,0][(a!=b)+(b=='')]for a,b in zip(a1,a2)])
    return [s, 0][s < 0]
