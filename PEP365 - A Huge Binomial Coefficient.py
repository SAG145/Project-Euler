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

def chinese_reminder(equ):
    m = 1
    for e in equ:
        m *= e[0]
    s = 0
    for i in range(len(equ)):
        mi = m // equ[i][0]
        s += mi*inverse(mi,equ[i][0])*equ[i][1]
    return s % m

def max_power_divides_fac(n,p):
    s = 0
    power = 1
    while p**power <= n:
        s += n // p**power
        power += 1
    return s

def fac_mod(n,p):
    if n <= p:
        m = 1
        for i in range(2,n + 1):
            m *= i
        m %= p
        return m
    t = n // p
    return ((-1)**t*fac_mod(n % p,p)*fac_mod(t,p)) % p

primes = all_primes_below_n(5000)
while primes[0] < 1000:
    primes.pop(0)

mods = []
for p in primes:
    if max_power_divides_fac(10**18,p) - max_power_divides_fac(10**9,p) - max_power_divides_fac(10**18 - 10**9,p) > 0:
        mods.append(0)
    else:
        mods.append(fac_mod(10**18,p)*inverse(fac_mod(10**9,p),p)*inverse(fac_mod(10**18 - 10**9,p),p) % p)

s = 0
for i in range(2,len(mods)):
    for j in range(1,i):
        if mods[i] == mods[j] == 0:
            c = 0
        else:
            c = chinese_reminder([[primes[i],mods[i]],[primes[j],mods[j]]])
        for k in range(j):
            if c != 0 or mods[k] != 0:
                s += chinese_reminder([[primes[i]*primes[j],c],[primes[k],mods[k]]])

print(s)

#Answer = 162619462356610313