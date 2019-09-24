def in_array(array1, array2):
    return sorted(set([x for y in array2 for x in array1 if x in y]))
