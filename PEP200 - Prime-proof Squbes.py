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

def all_squbes_200(n):
    psqu = all_primes_below_n(math.isqrt(n) + 1)
    pcube = all_primes_below_n(math.floor(math.cbrt(n)) + 1)
    sqube200 = []
    for p in psqu:
        for q in pcube:
            if p != q:
                s = p**2*q**3
                if "200" in str(s):
                    sqube200.append(s)
    sqube200.sort()
    return sqube200

def prob_prime(n):
    for k in range(10):
        if pow(random.randrange(2,n),n - 1,n) != 1:
            return False
    return True

def insert(s,index,a):
    return s[:index] + a + s[index + 1:]

def prime_proof(n):
    s = str(n)
    for i in range(len(s)):
        if i == 0:
            for d in range(1,10):
                if prob_prime(int(insert(s,i,str(d)))):
                    return False
        else:
            for d in range(10):
                if prob_prime(int(insert(s,i,str(d)))):
                    return False
    return True

c = 0
i = 0
for s in all_squbes_200(10**11):
    i += 1
    if prime_proof(s):
        c += 1
    if c == 200:
        print(s)
        break

#answer = 229161792008