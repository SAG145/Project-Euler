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

def num_sols(limit,e,mod):
    a = limit // mod
    if e != 0 and limit % mod >= e:
        a += 1
    return a

def U(N):
    primes = all_primes_below_n(100)[1:]
    s = 2*(N // 2)
    sols_found = N // 2
    mod = 2
    sols = [0]
    for p in primes:
        new_sols = []
        t = 0
        for r7 in range(0,p,7):
            for sol in sols:
                new_sol = chinese_reminder([[p,r7],[mod,sol]])
                if new_sol <= N:
                    t += num_sols(N,new_sol,mod*p)
                    new_sols.append(new_sol)
        mod *= p
        s += p*(N - sols_found - t)
        sols_found += N - sols_found - t
        sols = new_sols
        if sols_found == N:
            return s

print(U(10**17))

#Answer = 292137809490441370
#Time: 1:30
