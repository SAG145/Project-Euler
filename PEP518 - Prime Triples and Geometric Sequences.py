import math

def bool_all_primes_below_n(n):
    primes_bool = [False, False] + [True] * (n - 2)
    for k in range(2, int(math.sqrt(n)) + 1):
        if primes_bool[k]:
            for l in range(2*k,n,k):
                primes_bool[l] = False
    return primes_bool

def prime_factors_with_repetitions(n,primes_list = [],m = 2):
    if n == 1:
        return primes_list
    if n % 2 == 0:
        return prime_factors_with_repetitions(n // 2,primes_list + [2])
    else:
        if m == 2:
            m = 3
        for k in range(m,int(math.sqrt(n)) + 1,2):
            if n % k == 0:
                return prime_factors_with_repetitions(n // k,primes_list + [k],m)
        return primes_list + [n]

def odd_pf(pf):
    opf = []
    i = 1
    p = pf[0]
    pp = 1
    while i < len(pf) + 1:
        if i == len(pf) or pf[i] != p:
            if pp % 2 != 0:
                opf.append(p)
            if i != len(pf):
                p = pf[i]
                pp = 1
        else:
            pp += 1
        i += 1
    return tuple(opf)

def S(n):
    sigma = 0
    bool_primes = bool_all_primes_below_n(n)
    opti_list = []
    for i in range(len(bool_primes)):
        if bool_primes[i]:
            opti_list.append((odd_pf(prime_factors_with_repetitions(i + 1)),i + 1))
    opti_list.sort()
    for j in range(len(opti_list) - 1):
        k = j + 1
        while opti_list[k][0] == opti_list[j][0]:
            b = math.isqrt(opti_list[j][1]*opti_list[k][1])
            if bool_primes[b - 1]:
                sigma += b + opti_list[j][1] + opti_list[k][1] - 3
            k += 1
    return sigma

print(S(10**8))

#Answer = 100315739184392

#Time: 4:00
