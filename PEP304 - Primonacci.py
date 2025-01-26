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

def fib_mod(n):
    fib = [0,1]
    poss_p = []
    for i in range(2,4*(n + 1)):
        fib.append((fib[-1] + fib[-2]) % n)
        if fib[-1] == 0:
            poss_p.append(i)
    for p in poss_p:
        if fib[:p] == fib[p:2*p]:
            return fib[:p]

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

def fn_mod(n,pf):
    equ1 = []
    equ2 = []
    for p in pf:
        fmn = fib_mod(p)
        equ1.append((p,fmn[n % len(fmn)]))
        equ2.append((p,fmn[(n + 1) % len(fmn)]))

    return [chinese_reminder(equ1),chinese_reminder(equ2)]

bool_primes = [True]*(35*10**5)
bool_primes[0] = False
n = 10**14

for p in all_primes_below_n(10**7):
    for i in range(p - n % p,len(bool_primes),p):
        bool_primes[i] = False

sb = 0
np = 0
mod = 1234567891011
fib_mod_mod = fn_mod(n,[3,7,13,67,107,630803])
for i in range(len(bool_primes)):
    fib_mod_mod.append((fib_mod_mod[-1] + fib_mod_mod[-2]) % mod)
    if bool_primes[i]:
        np += 1
        sb += fib_mod_mod[-3]
        if np == 100000:
            break

print(sb % mod)

#answer = 283988410192