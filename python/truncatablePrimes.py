import math
from functools import lru_cache

@lru_cache(None)
def isPrime(n):
    if n == 2:
        return True
    if n<=1 or not n%2:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if not (n % i):
            return False
    return True

def isTP(p):
    div = 10
    while div < p:
        if not isPrime(p % div) or not isPrime(p // div):  
            return False
        div *= 10
    return True

count, i, totalSum = 0, 11, 0

while count < 11:
    if isPrime(i) and isTP(i):
        totalSum += i
        count += 1
    i += 2

print(totalSum)