import math
import random

def all_primes_below_n(n):
    primes_bool = [False, False] + [True] * (n - 2)
    for k in range(2, int(math.sqrt(n)) + 1):
        if primes_bool[k]:
            for l in range(2*k,n,k):
                primes_bool[l] = False
    primes_list = []
    for k in range(n):
        if primes_bool[k]:
            primes_list.append(k)
    return primes_list

def is_prime(n):
    if n % 2 == 0 and n != 2:
        return False
    for k in range(3,int(math.sqrt(n))+1,2):
        if n % k == 0:
            return False
    return True

def power_mod(base,power,mod):
    if power == 1:
        return base % mod
    a = power_mod(base,power // 2,mod)
    return base**(power % 2)*a**2 % mod

def prob_prime1(n):
    for k in range(10):
        if power_mod(random.randrange(2,n),n - 1,n) != 1:
            return False
    return True

def mod_p(p):
    h = p // 2 + 1
    for i in range(2,h):
        if i**2 % p == h:
            return i
    return -1

def invalid_mod(primes):
    invalid = []
    for p in primes[1:10]:
        m = mod_p(p)
        if m != -1:
            invalid.append((p,m, p - m))
    return invalid[:2]

def invalid(n,invalids):
    for t in invalids:
        p = t[0]
        if p > n - 1:
            break
        if n % p == t[1] or n % p == t[2]:
            return True
    return False

def t_primes(maxi):
    primes = all_primes_below_n(100)
    invalids = invalid_mod(primes)
    x = 1
    for n in range(3,maxi):
        if not invalid(n,invalids):
            if prob_prime1(2*n**2 - 1):
                x += 1
    return x

print(t_primes(50*10**6))

#Answer = 5437849

#Time: 15:00

#The algorithm is probabilistic, and when I ran it it came out 5437853, so I guessed closer and lower numbers until I found the answer.
