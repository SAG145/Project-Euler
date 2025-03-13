import math

def bool_all_primes_below_n(n):
    primes_bool = [False, False] + [True] * (n - 2)
    for k in range(2, int(math.sqrt(n)) + 1):
        if primes_bool[k]:
            for l in range(2*k,n,k):
                primes_bool[l] = False
    return primes_bool

def prime_factors_with_repetitions(n,primes_list = [],m = 2):
    if n % 2 == 0:
        return prime_factors_with_repetitions(n // 2,primes_list + [2])
    else:
        if m == 2:
            m = 3
        for k in range(m,int(math.sqrt(n)) + 1,2):
            if n % k == 0:
                return prime_factors_with_repetitions(n // k,primes_list + [k],m)
        return primes_list + [n]

def power_mod(base,power,mod):
    if power == 1:
        return base % mod
    a = power_mod(base,power // 2,mod)
    return base**(power % 2)*a**2 % mod

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

def factorials_max_pf(n,prime):
    pf = [0]*(n + 1)
    a = prime
    while a < n:
        for pp in range(a,n + 1,a):
            pf[pp] += 1
        a *= prime
    fmpf = [0]*(n + 1)
    for i in range(1,n + 1):
        fmpf[i] = fmpf[i - 1] + pf[i]
    return fmpf

def S(n):
    mod = 10**9 + 7
    primes = bool_all_primes_below_n(n + 1)
    factorials_pf = []
    factorial_sum_pf = []
    inverses = [0]*3
    for i in range(n + 1):
        if primes[i]:
            factorials_pf.append(factorials_max_pf(n + 1,i))
            if i > 2:
                inverses.append(inverse(i - 1,mod))
        else:
            factorials_pf.append(-1)
            if i > 2:
                inverses.append(0)

    for i in range(n + 1):
        if primes[i]:
            fspf = [0]
            for j in range(1,n + 1):
                fspf.append(fspf[-1] + factorials_pf[i][j])
            factorial_sum_pf.append(fspf)
        else:
            factorial_sum_pf.append(-1)

    for i in range(n + 1):
        if primes[i]:
            primes.append(i)
    primes = primes[n + 1:]

    s = 0
    for k in range(1,n + 1):
        pfB = []
        for p in primes:
            if p > k:
                break
            pfB.append((p,(k + 1)*factorials_pf[p][k] - 2*(factorial_sum_pf[p][k])))
        divi_sum = 1
        for pf in pfB:
            if pf[1] != 0:
                if pf[0] == 2:
                    divi_sum *= (power_mod(2,pf[1] + 1,mod) - 1)
                else:
                    divi_sum *= (power_mod(pf[0],pf[1] + 1,mod) - 1)*inverses[pf[0]]
            divi_sum %= mod
        s += divi_sum
    return s % mod

print(S(20000))

#Answer = 538319652

#Time: 3:00
