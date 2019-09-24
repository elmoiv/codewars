def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False
    for divisor in range(3, int(abs(n)**0.5) + 1, 2):
        if n % divisor == 0:
            return False
    return True
