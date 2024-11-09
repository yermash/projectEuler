
from helpers import *

def isBouncy(n):
    n = list(str(n))
    return not (n == sorted(n) or n == sorted(n, reverse=True))

def numUntilPercentBouncy(limPercent):
    numBouncy = 0
    i = 100
    while True:
        if isBouncy(i):
            numBouncy+=1
            if numBouncy/i >= limPercent:
                break
        i+=1
    return i

def numNonBouncy(n):
    count = 0
    for i in range(1,n+1):
        count += nCr(8+i,i)
        count += nCr(9+i,i)
        count -= 10
    print(count)

numNonBouncy(6)

