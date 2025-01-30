import math

def all_primes_below_n(n):
    primes_bool = [True]*n
    for k in range(2,math.isqrt(n) + 1):
        if primes_bool[k]:
            for l in range(k**2,n,k):
                primes_bool[l] = False
    primes_list = []
    for k in range(2,n):
        if primes_bool[k]:
            primes_list.append(k)
    return primes_list

def car(p,power):
    if p != 2 or (p == 2 and power <= 2):
        return (p - 1)*p**(power - 1)
    return (p - 1)*p**(power - 1) // 2

def L(n):
    primes = all_primes_below_n(n)
    max_car = [1]*(n // 2 + 1)
    for p in primes:
        for power in range(math.floor(math.log(n,p)),0,-1):
            q = p**power
            lam = car(p,power)
            lam1 = car(p,power + 1)
            for i in range(lam - (n // 2) % lam,len(max_car),lam):
                # if p**power == 5:
                #     print(i,lam)
                if (i + n // 2) % lam1 != 0:
                    max_car[i] *= q
    return (max(max_car) + 1) % 10**9

print(L(2*10**7))

#answer = 789453601