def solution(n):
    return sum(set(list(range(3, n, 3)) + list(range(5, n, 5))))
