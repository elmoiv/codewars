# factors function https://stackoverflow.com/users/4279/jfs modified version of the 
# original user https://stackoverflow.com/users/166949/steveha from the answer to 
# https://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python

def sol_equa(n):
    sols = []
    for fac in sorted(set(f for i in range(1, int(n**0.5) + 1) if not n%i for f in [i, n//i])):
        x = (fac + n/fac)/2
        y = (n/fac - x)/2
        sols.append([x, y])
    return [list(map(int, i)) for i in sols if sum(i).is_integer() and i[1] >= 0]
