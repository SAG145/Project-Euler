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

def extended_Euclid(n,mod):
    if n < mod:
        return extended_Euclid(mod,n)[::-1]
    while n % mod != 0:
        i = extended_Euclid(mod,n % mod)
        q = n // mod
        return (i[1],i[0] - q*i[1])
    return (0,1)

def inverse(n,mod):
    return extended_Euclid(n,mod)[0] % mod

def modi_inverse(p,pow2):
    return pow(p,2**pow2 - 1,2**pow2)

def f(p):
    mod = 2**p
    return (-(pow(2,pow(2,p,p - 1),p)*inverse(p,mod))) % mod

def g(p):
    return f(p) % p

def G(N):
    summ = 0
    primes = all_primes_below_n(N)
    for i in range(len(primes) - 1,0,-1):
        summ += g(primes[i])
    return summ

print(G(10**7))

#answer = 1603036763131
#זמן הרצה - 4 שעות ו 48 דקות