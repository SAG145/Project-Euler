import math

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

def f(K,primes):
    m = 1
    sigma = 0
    limit = 10**20
    for p in primes:
        if p**K > limit:
            break
        for power in range(2,math.floor(math.log(limit,p))):
            sigma += (m / p**power - m / p**(power + 1))*(power - 1) / (p**K)
        m *= (p - 1) / p
    return sigma

sigma = 0
primes = all_primes_below_n(2*10**7)
K = 1
fK = 1
while fK > 10**-14:
    fK = f(K,primes)
    sigma += fK
    K += 1
print(round(sigma,12))

#Answer = 0.547326103833