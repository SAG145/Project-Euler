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

def all_min_pf_below_n(n):
    min_pf = [0]*n
    for k in range(2,int(math.sqrt(n)) + 1):
        if min_pf[k] == 0:
            for l in range(2*k,n,k):
                if min_pf[l] == 0:
                    min_pf[l] = k
    return min_pf

def all_prime_factorisations_below_n(n):
    min_pf = all_min_pf_below_n(n)
    pf = [0,[]]
    for k in range(2,n):
        mpf = min_pf[k]
        if mpf == 0:
            pf.append((k,))
        else:
            pf.append(pf[k // mpf] + (mpf,))
    return pf

def prime_factors(n,primes,pf,primes_list = [],i = 0):
    if n == 1:
        return primes_list
    if n < len(pf):
        return primes_list + list(pf[n])
    if n % 2 == 0:
        return prime_factors(n // 2,primes,pf,primes_list + [2])
    else:
        if i == 0:
            i = 1
        while primes[i] < math.isqrt(n) + 1:
            if n % primes[i] == 0:
                return prime_factors(n // primes[i],primes,pf,primes_list + [primes[i]],i)
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
        mp = max_power_divides(j1**2 - j1 + 1,p)
        factors[j1][0] *= p**mp
        factors[j1][1] = max(p,factors[j1][1])

    if p + 1 - i != i:
        for j2 in range(p + 1 - i,len(factors),p):
            mp = max_power_divides(j2**2 - j2 + 1,p)
            factors[j2][0] *= p**mp
            factors[j2][1] = max(p,factors[j2][1])

target = 2*10**6

factors = []
for i in range(target + 1):
    factors.append([1,0])

apf = all_prime_factorisations_below_n(target + 10)

found = [False]*(target + 1010)
primes = all_primes_below_n(target + 1000)

s = -target
for n in range(1,target + 1):
    if n > primes[0]:
        primes.pop(0)
    nf = factors[n][0]
    t = n**2 - n + 1
    if nf == t:
        s += max(apf[n + 1][0],factors[n][1])
    else:
        pf = prime_factors(t // nf,primes,apf)
        s += max(max(pf),factors[n][1],apf[n + 1][0])
        for p in pf:
            if p < len(found) and not found[p]:
                found[p] = True
                update(factors,p,n % p)
                if p <= primes[-1]:
                    primes.remove(p)

print(s)

#Answer = 269533451410884183
