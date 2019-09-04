# n = m ^ k
# We should return [m, k]

import math

def isPP(n):

    # Getting max power (Rounding up)
    # thanks to: https://math.stackexchange.com/a/470758
    b = int(math.log(n, 2) + 1)

    # Lopping in powers from a minimum of 2
    for k in range(2, b + 1):

        # Rounding the k(th) root for n to test for possible [m] value
        m = round(n ** (1 / k))
        
        # Testing if m ^ k == n
        if m ** k == n:
            return [m, k]
    
    # If not return None
    return None
