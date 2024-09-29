import math

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

mod = 10**9 + 7
k = 10**8
x = 2
for p in all_primes_below_n(k):
    x = (x*p**math.floor(math.log(k,p))) % mod

print(x)

#answer = 83985379