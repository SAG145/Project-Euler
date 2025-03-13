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

def log(x,y):
    return math.log(y,int(x))

def hamming(limit,primes):
    list = []
    if limit == 1:
        return list
    if len(primes) == 1:
        for k in range(math.floor(log(primes[0],limit)) + 1):
            list.append(primes[0]**k)
        return list

    for k in range(math.floor(log(primes[0],limit)) + 1):
        lst = hamming(limit / primes[0]**k,primes[1:])
        for n in lst:
            list.append(n*primes[0]**k)
    return list

h = hamming(10**13 + 1,all_primes_below_n(48))
print(len(h))
h.sort()
s = 0
for i in range(len(h) - 1):
    if h[i] + 1 == h[i + 1]:
        s += h[i]
print(s)

#Answer = 2227616372734
#I found the upper bound (10^13) through trial and error.
