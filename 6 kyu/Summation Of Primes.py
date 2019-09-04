def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False
    for divisor in range(3, int(n**0.5)+ 1, 2):
        if n % divisor == 0:
            return False
    return True

def summationOfPrimes(primes):
  res = 0
  for i in range(primes+1):
      if is_prime(i):
         res += i
  return res