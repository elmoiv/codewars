def find_outlier(integers):
    arr = sorted(integers, key = lambda n: n%2)
    return arr[0] if arr[1]%2 and arr[2]%2 else arr[-1]
