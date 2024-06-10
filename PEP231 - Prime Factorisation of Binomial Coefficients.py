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

def max_power(n,p):
    maxi = 0
    a = p
    while p < n + 1:
        maxi += n // p
        p *= a
    return maxi

def prime_facorisation_of_nCr(n,r):
    primes = all_primes_below_n(n)
    sum = 0
    for p in primes:
        sum += p*(max_power(n,p) - max_power(r,p) - max_power(n - r,p))
    return sum
print(prime_facorisation_of_nCr(20000000,15000000))

#answer = 7526965179680
