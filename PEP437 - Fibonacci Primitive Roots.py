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

def prime_factors(primes,n):
    pf = []
    i = 0
    while i < len(primes) and n > 1:
        while n % primes[i] == 0:
            pf.append(primes[i])
            n //= primes[i]
        i += 1
    if n > 1:
        pf.append(n)
    return list(dict.fromkeys(pf))

def max_power_divides(n,p):
    m = 0
    while n % p == 0:
        n //= p
        m += 1
    return m

def is_qua_res(n,p):
    return pow(n,(p - 1) // 2,p) == 1

def square_root(n,p):
    s = max_power_divides(p - 1,2)
    q = (p - 1) // 2**s
    while True:
        z = random.randint(2,p - 1)
        if not is_qua_res(z,p):
            break
    c = pow(z,q,p)
    t = pow(n,q,p)
    r = pow(n,(q + 1) // 2,p)
    while t != 1:
        i = 0
        t1 = t
        while t1 != 1:
            t1 = t1**2 % p
            i += 1
        b = pow(c,2**(s - i - 1),p)
        s = i
        c = b**2 % p
        t = t*c % p
        r = (r*b) % p
    return r

def is_pr(facs,n,p):
    for f2 in facs:
        if pow(n,(p - 1) // f2,p) == 1:
            return False
    return True

sp = 5
primes = all_primes_below_n(10**4)
for p in all_primes_below_n(10**8):
    if is_qua_res(5,p) and p > 5:
        if p % 4 == 3:
            r = pow(5,(p + 1) // 4,p)
        else:
            r = square_root(5,p)
        facs = prime_factors(primes,p - 1)
        if is_pr(facs,((1 + r)*(p + 1) // 2) % p,p):
            sp += p
        elif is_pr(facs,((1 - r)*(p + 1) // 2) % p,p):
            sp += p
        elif is_pr(facs,((1 + p - r)*(p + 1) // 2) % p,p):
            sp += p
        elif is_pr(facs,((1 - (p - r))*(p + 1) // 2) % p,p):
            sp += p

print(sp)

#Answer = 74204709657207
#Time: 7:30
