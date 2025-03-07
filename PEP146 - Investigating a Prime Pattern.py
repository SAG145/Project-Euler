import math

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

def prime_pattern(n,primes,steps):
    not_allowed = [15,21,25]
    for p in primes:
        if p > n + 2:
            return len(not_allowed) == 0
        m = ((n % p)**2) % p
        for s in steps:
            if (m + s) % p == 0:
                return False
        for k in not_allowed:
            if (m + k) % p == 0:
                not_allowed.remove(k)

def such_integers(maxi):
    primes = all_primes_below_n(maxi)
    steps = [1,3,7,9,13,27]
    sum1 = 0
    for a in range(4,maxi,42):
        if prime_pattern(a,primes,steps):
            sum1 += a
    for b in range(10,maxi,42):
        if prime_pattern(b,primes,steps):
            sum1 += b
    for c in range(32,maxi,42):
        if prime_pattern(c,primes,steps):
            sum1 += c
    for d in range(38,maxi,42):
        if prime_pattern(d,primes,steps):
            sum1 += d
    return sum1

print(such_integers(150*10**6))

#answer = 676333270
#5 minutes
