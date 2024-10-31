from helpers import *

def is_valid_prime_generating(n, is_prime):
    if not is_prime[1 + n]:      
        return False
    if not is_prime[2 + n // 2]:  
        return False

    for divisor in range(3, int(math.sqrt(n)) + 1):
        if n % divisor == 0:
            if not is_prime[divisor + n // divisor]:
                return False
    return True

def sum_prime_generating_integers(limit):
    is_prime = sieve(limit + limit // 2)  
    total_sum = 1  # Start with 1, since it's a valid number

    for n in range(2, limit + 1, 4):
        if is_valid_prime_generating(n, is_prime):
            total_sum += n
    return total_sum

result = sum_prime_generating_integers(100000000)
print(result)