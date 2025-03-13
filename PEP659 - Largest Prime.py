import math
import random

def prob_prime(n):
    for _ in range(10):
        if pow(random.randrange(2,n),n - 1,n) != 1:
            return False
    return True

def all_primes_below_n(n):
    primes_bool = [False, False] + [True] * (n - 2)
    for k in range(2, int(math.sqrt(n)) + 1):
        if primes_bool[k]:
            for l in range(2*k,n,k):
                primes_bool[l] = False
    primes_list = []
    for k in range(n):
        if primes_bool[k]:
            primes_list.append(k)
    return primes_list

def prime_factors(n,primes,primes_list = [],i = 0):
    if n == 1:
        return primes_list
    if prob_prime(n):
        if prob_prime(n):
            return primes_list + [n]
    if n % 2 == 0:
        return prime_factors(n // 2,primes_list + [2])
    else:
        if i == 0:
            i = 1
        while primes[i] < math.isqrt(n) + 1:
            if n % primes[i] == 0:
                return prime_factors(n // primes[i],primes,primes_list + [primes[i]],i)
            i += 1
        return primes_list + [n]

def max_power_divides(n,p):
    power = 0
    a = 1
    while n % a == 0:
        power += 1
        a *= p
    return power - 1

def update(factors,p,i):
    for j1 in range(i,len(factors),p):
        mp = max_power_divides(4*j1**2 + 1,p)
        factors[j1][0] *= p**mp
        factors[j1][1] = max(p,factors[j1][1])

    for j2 in range(p - i,len(factors),p):
        mp = max_power_divides(4*j2**2 + 1,p)
        factors[j2][0] *= p**mp
        factors[j2][1] = max(p,factors[j2][1])

factors = []
for i in range(10**7 + 1):
    factors.append([1,0])

found = [False]*(2*10**7 + 1010)
primes = all_primes_below_n(2*10**7 + 1000)

s = 0
for n in range(1,10**7 + 1):
    nf = factors[n][0]
    t = 4*n**2 + 1
    if nf == t:
        s += factors[n][1]
    else:
        pf = prime_factors(t // nf,primes)
        s += pf[-1]
        for p in pf:
            if p < len(found) and not found[p]:
                found[p] = True
                update(factors,p,n % p)

print(s % 10**18)

#Answer = 238518915714422000
#Time: 16:00

