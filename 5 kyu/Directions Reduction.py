def dirReduc(arr):
    i = 0
    while True:
        if sorted(arr[i:i+2]) == ['NORTH', 'SOUTH'] or sorted(arr[i:i+2]) == ['EAST', 'WEST']:
            del arr[i:i+2]
            i = 0
        else:
            i += 1
        if i > len(arr):
            return arr