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

def pf_factorial(p,n):
    s = 0
    a = p
    d = 1
    while d != 0:
        d = n // a
        s += d
        a *= p
    return s

def R(pf,mod):
    tr = -pf[0]
    for power in range(1,pf[0] + 1):
        s = 1
        for p in pf:
            m = p // power + 1
            if m == 1:
                break
            s = s*m % mod
        tr += s % mod
    return tr % mod

pf = []
for p in all_primes_below_n(10**7):
    pf.append(pf_factorial(p,10**7))

print(R(pf,10**9 + 7))

#answer = 40410219