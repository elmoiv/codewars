def move_zeros(arr):
    _arr = [i for i in arr if not (i == 0 and i is not False)]
    return _arr + [0] * (len(arr) - len(_arr))
    

# This was a good hit in one-line
# @anter69

def move_zeros(array):
    return sorted(array, key=lambda x: x == 0 and x is not False)
