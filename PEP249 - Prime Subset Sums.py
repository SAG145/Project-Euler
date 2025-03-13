import math
import copy

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

def next_prime(p,sums,limit,mod):
    new = copy.copy(sums)
    for m in range(limit + 1):
        new[(m + p)] = (new[m + p] + sums[m]) % mod
    return new

mod = 10**16
primes = all_primes_below_n(5000)
sums = [1] + [0]*(sum(primes))
limit = 0
for p in primes:
    print(p,limit,len(sums))
    sums = next_prime(p,sums,limit,mod)
    limit += p

poss = 0
for p in all_primes_below_n(sum(primes)):
    poss += sums[p]
print(poss % mod)

#Answer = 9275262564250418

#Time: 1:30
