import math
import random

def all_primes_below_n(n):
    primes_bool = [True]*n
    for k in range(2, math.isqrt(n) + 1):
        if primes_bool[k]:
            for l in range(k**2,n,k):
                primes_bool[l] = False
    primes_list = []
    for k in range(2,n):
        if primes_bool[k]:
            primes_list.append(k)
    return primes_list

def prob_prime(n):
    for _ in range(20):
        if pow(random.randrange(2,n),n - 1,n) != 1:
            return False
    return True

def lowest_prime_factor(n,primes):
    if prob_prime(n):
        return n
    for p in primes:
        if n % p == 0:
            return p

def next(n,primes):
    return n + (lowest_prime_factor(2*n - 1,primes) - 1) // 2

primes = all_primes_below_n(math.isqrt(10**15) + 1)
p = 0
n = 17
while n <= 10**15:
    p = n
    n = next(n,primes)

print(3*p + 10**15 - p)

#Answer = 2744233049300770

#The code is based on patterns that the sequence contains.