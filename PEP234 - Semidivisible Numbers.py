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

t = 999966663333
primes = all_primes_below_n(math.floor(math.sqrt(t)) + 100)
lst = []
s = 0
a = 0
for i in range(len(primes) - 1):
    p = primes[i]
    q = primes[i + 1]
    for n in range(p + 1,q**2 // p + 1):
        a = p*n
        if a < t + 1:
            if a != p*q:
                lst.append(a)
        else:
            break
    for m in range(math.ceil(p**2 / q),q):
        a = q*m
        if a < t + 1:
            if a != p*q:
                lst.append(a)
        else:
            break

lst = list(dict.fromkeys(lst))
print(sum(lst))

#answer = 1259187438574927161