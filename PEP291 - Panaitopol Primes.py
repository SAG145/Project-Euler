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

limit = 5*10**15
sieve = [True]*(round(2 + math.sqrt(8*limit - 4) / 4) + 5)
for p in all_primes_below_n(10**4):
    if p % 4 == 1:
        r = 0
        for a in range(1,p // 2 + 1):
            if (a**2 + (a - 1)**2) % p == 0:
                r = a
                break
        if r != 0:
            for i in range(r,len(sieve),p):
                sieve[i] = False
            for j in range(p - r + 1,len(sieve),p):
                sieve[j] = False

pan_primes = 0
for s in range(2,100):
    if prob_prime(s**2 + (s - 1)**2):
        pan_primes += 1

for t in range(100,len(sieve)):
    if sieve[t]:
        if prob_prime(2*(t**2 - t + 1) - 1):
            pan_primes += 1

print(pan_primes)

#answer = 4037526
#17 minutes