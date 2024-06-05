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

def remainder(n,primes):
    p = primes[n - 1]
    return 2*p*n % p**2

primes = all_primes_below_n(10**6)
n = 10**3 + 1
while remainder(n,primes) < 10**10 + 1:
    n += 2
print(n)

#answer = 21035
