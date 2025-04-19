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

def sum_n(n):
    return n*(n + 1) // 2

def S(n,d):
    primes = all_primes_below_n(math.isqrt(n) + 1)
    div_bool = [True]*(n // (2*d) + 1)
    div = []
    divp = []
    for p in primes:
        if p != d and p != 2:
            for i in range(inverse(2*d,p),len(div_bool),p):
                if 2*d*i - 1 != p:
                    div_bool[i] = False

    for i in range(1,len(div_bool)):
        if div_bool[i]:
            div.append(2*d*i - 1)

    for p in primes:
        for power in range(2,math.floor(math.log(n,p)) + 1):
            if ((p**(power + 1) - 1) // (p - 1)) % d == 0:
                divp.append((p**power,p**(power + 1)))

    div.sort()

    s = 0
    for d1 in div:
        s += d1*sum_n(n // d1)

    for d2 in divp:
        s += d2[0]*sum_n(n // d2[0]) - d2[1]*sum_n(n // d2[1])

    for t in divp:
        div.append(t[0])
    div.sort()

    i = 0
    while div[i]*div[0] <= n:
        j = 0
        while div[j]*div[i] <= n and j <= i:
            s -= div[j]*div[i]*sum_n(n // (div[j]*div[i]))
            j += 1
        i += 1

    return s

print(S(10**11,2017))

#Answer = 2992480851924313898