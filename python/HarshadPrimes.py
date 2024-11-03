from helpers import *
import time 

def rightTruncatableHarshads(limit, current=0):
    results = []
    for digit in range(10):
        candidate = current * 10 + digit
        if candidate == 0 or candidate >= limit:  
            continue
        if candidate % sumDigits(candidate) == 0:
            results.append(candidate)
            results.extend(rightTruncatableHarshads(limit, candidate))
    
    return results
    
def find_strong_harshad_numbers(harshad_numbers):
    strong_harshads = []
    for n in harshad_numbers:
        sum_d = sumDigits(n)
        if sum_d > 0 and (n // sum_d) > 1 and isPrime(n // sum_d):
            strong_harshads.append(n)
    return strong_harshads

def find_strong_right_truncatable_harshad_primes(limit):
    harshad_numbers = rightTruncatableHarshads(limit // 10)
    strong_harshads = find_strong_harshad_numbers(harshad_numbers)
    
    sum_strong_harshad_primes = 0
    
    for strong_harshad in strong_harshads:
        for last_digit in [1, 3, 7, 9]: 
            candidate_prime = strong_harshad * 10 + last_digit
            if candidate_prime < limit and isPrime(candidate_prime):
                sum_strong_harshad_primes += candidate_prime
    
    return sum_strong_harshad_primes

start_time = time.time()
result = find_strong_right_truncatable_harshad_primes(10**14)
end_time = time.time()
print(result)
print(f"Time taken: {end_time - start_time} seconds")
