import math

# for file parsing, look at pokerHands.py

def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def sieve(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0], is_prime[1] = False, False 
    for i in range(2, int(math.sqrt(limit)) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return is_prime

def divisors(n):
    divs = set()
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divs.add(i)
            divs.add(n // i)
    return divs


def listProd(l):
    ret = 1
    for elem in l:
        ret *= elem
    return ret