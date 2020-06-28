def binary_array_to_number(arr):
    return int(str(arr).replace(', ','')[1:-1], 2)
