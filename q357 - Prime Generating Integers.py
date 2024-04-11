import math
def all_primes_below_n(n):
    primes_bool = [False, False] + [True] * (n - 2)
    for k in range(2, int(math.sqrt(n)) + 1):
        if primes_bool[k]:
            for l in range(2*k,n,k):
                primes_bool[l] = False
    return primes_bool

def prime_divisors_sum(n):
    for k in range(2,int(math.sqrt(n)) + 1):
        if n % k == 0:
            if not bool_primes[k + n//k]:
                return False
    return True


bool_primes = all_primes_below_n(10**8)
primes = []
for k in range(10**8):
    if bool_primes[k]:
        primes.append(k)
sum = 0
for p in primes:
    if prime_divisors_sum(p - 1):
        sum += p - 1
print(sum)

#answer = 1739023853137