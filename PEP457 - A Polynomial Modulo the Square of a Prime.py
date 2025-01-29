import math
import random

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

def max_power_divides(n,p):
    m = 0
    while n % p == 0:
        n //= p
        m += 1
    return m

def is_qua_res(n,p):
    return pow(n,(p - 1) // 2,p) == 1

def square_root(n,p,power):
    if power == 1:
        if p % 4 == 3:
            return pow(n,(p + 1) // 4,p)
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
    else:
        r = square_root(n,p,1)
        s = r - (r**2 - 13)*inverse(2*r,p)
        return s % p**power

s = 5
for p in all_primes_below_n(10**7)[6:]:
    if pow(13,(p - 1) // 2,p) == 1:
        sols = []
        sr13 = square_root(13,p,2)
        srl = [sr13,p**2 - sr13]
        for sr1 in srl:
            t = ((3 + sr1)*(p**2 + 1) // 2) % p**2
            if (t**2 - 3*t - 1) % p**2 == 0:
                sols.append(t)
        s += min(sols)

print(s)

#answer = 2647787126797397063