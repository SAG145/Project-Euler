import math
import random

def all_primes_below_n(n):
    primes_bool = [True]*n
    for k in range(2, math.isqrt(n) + 1):
        if primes_bool[k]:
            # print(k)
            for l in range(k**2,n,k):
                primes_bool[l] = False
    primes_list = []
    for k in range(2,n):
        if primes_bool[k]:
            primes_list.append(k)
    return primes_list

def prob_prime(n):
    for _ in range(10):
        if pow(random.randrange(2,n),n - 1,n) != 1:
            return False
    return True

def valid(n,divi):
    for d in divi:
        if prob_prime(n*d + 1):
            if prob_prime(n*d + 1):
                if prob_prime(n*d + 1):
                    return False
    return True

divi = [2, 4, 14, 22, 28, 44, 154, 308]
good_primes = []
for p in all_primes_below_n(10**9 // 308):
    if valid(p,divi):
        good_primes.append(p)
    if len(good_primes) == 10**5:
        break

good_numbers = []
i = 0
while i < len(good_primes):
    j = 0
    while j <= i and good_primes[i]*good_primes[j] < good_primes[-1]:
        if valid(good_primes[i]*good_primes[j],divi):
            good_numbers.append(good_primes[i]*good_primes[j])
        k = 0
        while k <= j and good_primes[i]*good_primes[j]*good_primes[k] < good_primes[-1]:
            if valid(good_primes[i]*good_primes[j]*good_primes[k],divi) and valid(good_primes[i]*good_primes[j],divi) and valid(good_primes[i]*good_primes[k],divi) and valid(good_primes[j]*good_primes[k],divi):
                good_numbers.append(good_primes[i]*good_primes[j]*good_primes[k])
            k += 1
        j += 1
    i += 1
    if j == 0:
        break

print(308*sorted(good_primes + good_numbers)[99998])

#Answer = 921107572

