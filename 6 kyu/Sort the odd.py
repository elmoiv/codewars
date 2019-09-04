def sort_array(arr):
    ods = sorted(i for i in arr if i % 2)
    return [ods.pop(0) if e % 2 else e for e in arr]
