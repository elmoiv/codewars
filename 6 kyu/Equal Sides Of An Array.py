def find_even_index(arr):
    for n,i in enumerate(arr):
        if sum(arr[:n]) == sum(arr[n+1:]):
            return n
    return -1
